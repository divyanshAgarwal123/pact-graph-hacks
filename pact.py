"""A small, live FalkorDB feasibility slice for PACT's synthetic case."""

import argparse
import json
import os

from falkordb import FalkorDB
from redis.exceptions import ResponseError


GRAPH_NAME = "pact_demo"
GOAL_ID = "school-laptops"


def graph():
    db = FalkorDB(host=os.getenv("FALKORDB_HOST", "127.0.0.1"),
                  port=int(os.getenv("FALKORDB_PORT", "6389")),
                  socket_connect_timeout=3)
    return db.select_graph(GRAPH_NAME)


def seed(g):
    """Reset only the disposable synthetic demo graph."""
    try:
        g.delete()
    except ResponseError as error:
        # A new graph has no key to delete. Other failures must remain visible.
        if "Invalid graph operation on empty key" not in str(error):
            raise
    g.query("CREATE (:Goal {id:$id, label:$label, quantity:$quantity, deadline:$deadline})",
            {"id": GOAL_ID, "label": "20 prepared laptops and a class",
             "quantity": 20, "deadline": 900})

    requirements = [
        ("devices", "20 retired laptops", 20),
        ("wipe", "verified wiping capacity", 20),
        ("repair", "repair capacity", 20),
        ("room", "clinic room in Day 2 window", 1),
    ]
    for key, label, quantity in requirements:
        g.query("""MATCH (goal:Goal {id:$goal})
                   CREATE (goal)-[:REQUIRES]->(:Requirement
                     {id:$id, label:$label, quantity:$quantity})""",
                {"goal": GOAL_ID, "id": key, "label": label, "quantity": quantity})

    offers = [
        ("donor", "Donor D", "device-batch", "devices", 24, 0, 900, 0, 1, 0, 20, 30),
        ("wiper", "Wiping provider W", "wiping-slot", "wipe", 20, 540, 660, 10, 1, 0, 0, 0),
        ("repairer", "Repair group R", "repair-slot", "repair", 20, 540, 960, 0, 2, 12, 0, 0),
        ("school", "School S", "clinic-room", "room", 1, 1980, 2220, 0, 1, 0, 0, 0),
    ]
    for (org_id, org_name, offer_id, requirement_id, quantity, window_start,
         window_end, rate, parallelism, minutes_each, van_capacity, trip_minutes) in offers:
        g.query("""MATCH (r:Requirement {id:$requirement})
                   CREATE (org:Organization {id:$org_id, name:$org_name})
                     -[:MAKES]->(offer:Offer {id:$offer_id, quantity:$quantity,
                       window_start:$window_start, window_end:$window_end,
                       rate_per_hour:$rate, parallelism:$parallelism,
                       minutes_each:$minutes_each, van_capacity:$van_capacity,
                       trip_minutes:$trip_minutes})
                     -[:SATISFIES]->(r)""",
                {"requirement": requirement_id, "org_id": org_id,
                 "org_name": org_name, "offer_id": offer_id, "quantity": quantity,
                 "window_start": window_start, "window_end": window_end,
                 "rate": rate, "parallelism": parallelism,
                 "minutes_each": minutes_each, "van_capacity": van_capacity,
                 "trip_minutes": trip_minutes})
    for number in range(1, 25):
        g.query("CREATE (:Device {id:$id})", {"id": f"L{number:02d}"})


def simulate_withdrawal(g):
    """Idempotent demo event: preserve ten completed wipes and expose W2."""
    g.query("""MATCH (o:Offer {id:'wiping-slot'})
               SET o.active=false RETURN o.id""")
    g.query("""MATCH (r:Requirement {id:'wipe'})
               MERGE (org:Organization {id:'wiper2'})
               SET org.name='Backup wiping provider W2'
               MERGE (org)-[:MAKES]->(o:Offer {id:'backup-wiping-slot'})
               SET o.quantity=10, o.window_start=630, o.window_end=690,
                   o.rate_per_hour=10, o.parallelism=1, o.minutes_each=0,
                   o.van_capacity=0, o.trip_minutes=0, o.active=true
               MERGE (o)-[:SATISFIES]->(r)""")
    for number in range(1, 11):
        g.query("""MATCH (d:Device {id:$id})
                   MERGE (record:WipeRecord {device_id:$id})
                   SET record.completed_at=600, record.simulated=true
                   MERGE (d)-[:HAS_WIPE_RECORD]->(record)""",
                {"id": f"L{number:02d}"})
    g.query("MATCH (r:Requirement {id:'wipe'}) SET r.completed=10")
    g.query("""MERGE (episode:Episode {id:'wiper-withdrawal'})
               SET episode.kind='withdrawal', episode.minute=600,
                   episode.simulated=true""")


def candidates(g):
    result = g.query("""MATCH (goal:Goal {id:$goal})-[:REQUIRES]->(r:Requirement)
                         <-[:SATISFIES]-(offer:Offer)<-[:MAKES]-(org:Organization)
                      WHERE coalesce(offer.active,true) = true
                        AND offer.quantity >= r.quantity - coalesce(r.completed,0)
                      RETURN r.id, r.quantity, org.id, org.name, offer.id,
                             offer.quantity ORDER BY r.id, org.id""",
                     {"goal": GOAL_ID})
    rows = [{"requirement": row[0], "needed": row[1], "organization_id": row[2],
             "organization": row[3], "offer_id": row[4], "offered": row[5]}
            for row in result.result_set]
    required = {row[0] for row in g.query(
        "MATCH (:Goal {id:$goal})-[:REQUIRES]->(r:Requirement) RETURN r.id",
        {"goal": GOAL_ID}).result_set}
    covered = {row["requirement"] for row in rows}
    return {"goal": GOAL_ID, "requirements": sorted(required),
            "covered": sorted(covered), "all_covered": bool(required) and required == covered,
            "candidate_offers": rows}


def scenario(g):
    """Read the current quantity, deadline, and contribution terms from FalkorDB."""
    goals = g.query("MATCH (goal:Goal {id:$id}) RETURN goal.quantity, goal.deadline",
                    {"id": GOAL_ID}).result_set
    if len(goals) != 1:
        raise ValueError("Demo goal missing or duplicated in FalkorDB")
    rows = g.query("""MATCH (:Goal {id:$id})-[:REQUIRES]->(r:Requirement)
                      <-[:SATISFIES]-(o:Offer)<-[:MAKES]-(org:Organization)
                      WHERE coalesce(o.active,true) = true
                      RETURN r.id, o.id, o.quantity, o.window_start, o.window_end,
                             o.rate_per_hour, o.parallelism, o.minutes_each,
                             o.van_capacity, o.trip_minutes, org.name""",
                   {"id": GOAL_ID}).result_set
    completed = [row[0] for row in g.query("""MATCH (d:Device)-[:HAS_WIPE_RECORD]->(record:WipeRecord)
                                                  WHERE record.simulated=true RETURN d.id ORDER BY d.id""").result_set]
    inventory = [row[0] for row in g.query("MATCH (d:Device) RETURN d.id ORDER BY d.id").result_set]
    return {"quantity": goals[0][0], "deadline": goals[0][1],
            "completed_wipe_ids": completed, "device_ids": inventory,
            "offers": {row[0]: {"id": row[1], "quantity": row[2],
                                 "window_start": row[3], "window_end": row[4],
                                 "rate_per_hour": row[5], "parallelism": row[6],
                                 "minutes_each": row[7], "van_capacity": row[8],
                                 "trip_minutes": row[9], "organization": row[10]}
                       for row in rows}}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("seed", "candidates", "plan", "withdraw"))
    args = parser.parse_args()
    g = graph()
    if args.command == "seed":
        seed(g)
    elif args.command == "withdraw":
        simulate_withdrawal(g)
    if args.command == "plan":
        from planner import plan
        result = plan(scenario(g))
    else:
        result = candidates(g)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
