"""Bounded schedule solver and independent checker for PACT's first scenario."""

from math import ceil

from ortools.sat.python import cp_model


def _terms(scenario):
    quantity = scenario["quantity"]
    completed_ids = scenario["completed_wipe_ids"]
    if len(completed_ids) != len(set(completed_ids)) or not set(completed_ids).issubset(scenario["device_ids"]):
        return None, "Invalid completed-device evidence"
    if len(completed_ids) > quantity:
        return None, "More completed wipes than required devices"
    remaining_wipes = quantity - len(completed_ids)
    offers = scenario["offers"]
    missing = sorted({"devices", "wipe", "repair", "room"} - offers.keys())
    if missing:
        return None, "Missing graph offers: " + ", ".join(missing)
    donor, wiper, repairer, room = (offers[key] for key in
                                    ("devices", "wipe", "repair", "room"))
    if quantity <= 0 or donor["quantity"] < quantity or wiper["quantity"] < remaining_wipes or repairer["quantity"] < quantity:
        return None, "Insufficient declared device, wiping, or repair quantity"
    if donor["van_capacity"] < quantity:
        return None, "One modeled van trip cannot carry the device batch"
    if wiper["rate_per_hour"] <= 0 or repairer["parallelism"] <= 0 or repairer["minutes_each"] <= 0:
        return None, "Missing positive processing capacity"
    if donor["trip_minutes"] <= 0:
        return None, "Missing transport duration"
    if not (room["window_start"] <= 1980 and room["window_end"] >= 2220):
        return None, "Day 2 clinic and introduction room window is unavailable"
    return {
        "wipe": ceil(remaining_wipes * 60 / wiper["rate_per_hour"]),
        "transfer": donor["trip_minutes"],
        "prepare": ceil(quantity * repairer["minutes_each"] / repairer["parallelism"]),
        "deliver": donor["trip_minutes"],
    }, None


def check_schedule(scenario, steps):
    """Validate a returned witness without trusting the solver's own status."""
    durations, reason = _terms(scenario)
    if reason:
        return False, reason
    offers = scenario["offers"]
    for name, duration in durations.items():
        step = steps[name]
        if step["end"] - step["start"] != duration:
            return False, f"Wrong {name} duration"
    if steps["wipe"]["start"] < offers["wipe"]["window_start"] or steps["wipe"]["end"] > offers["wipe"]["window_end"]:
        return False, "Wiping outside provider window"
    if steps["prepare"]["start"] < offers["repair"]["window_start"] or steps["prepare"]["end"] > offers["repair"]["window_end"]:
        return False, "Preparation outside repair window"
    for before, after in (("wipe", "transfer"), ("transfer", "prepare"), ("prepare", "deliver")):
        if steps[after]["start"] < steps[before]["end"]:
            return False, f"{after} starts before {before} finishes"
    if steps["transfer"]["start"] < offers["devices"]["window_start"] or steps["deliver"]["end"] > offers["devices"]["window_end"]:
        return False, "Transport outside donor window"
    if steps["deliver"]["end"] > scenario["deadline"]:
        return False, "Delivery misses goal deadline"
    if steps["clinic"] != {"start": 1980, "end": 2160} or steps["introduction"] != {"start": 2160, "end": 2220}:
        return False, "Day 2 room program is wrong"
    return True, None


def plan(scenario):
    durations, reason = _terms(scenario)
    if reason:
        return {"status": "blocked", "reason": reason}

    offers = scenario["offers"]
    model = cp_model.CpModel()
    starts = {}
    ends = {}
    for name in ("wipe", "transfer", "prepare", "deliver"):
        starts[name] = model.new_int_var(0, 2880, name + "_start")
        ends[name] = model.new_int_var(0, 2880, name + "_end")
        model.add(ends[name] == starts[name] + durations[name])
    model.add(starts["wipe"] >= offers["wipe"]["window_start"])
    model.add(ends["wipe"] <= offers["wipe"]["window_end"])
    model.add(starts["prepare"] >= offers["repair"]["window_start"])
    model.add(ends["prepare"] <= offers["repair"]["window_end"])
    model.add(starts["transfer"] >= offers["devices"]["window_start"])
    model.add(ends["deliver"] <= offers["devices"]["window_end"])
    model.add(ends["deliver"] <= scenario["deadline"])
    for before, after in (("wipe", "transfer"), ("transfer", "prepare"), ("prepare", "deliver")):
        model.add(starts[after] >= ends[before])
    model.minimize(ends["deliver"])
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = 3
    status = solver.solve(model)
    if status == cp_model.UNKNOWN:
        return {"status": "unresolved", "reason": "Solver timed out"}
    if status not in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        return {"status": "blocked", "reason": "No schedule fits the declared windows and deadline"}
    steps = {name: {"start": solver.value(starts[name]), "end": solver.value(ends[name])}
             for name in starts}
    steps["clinic"] = {"start": 1980, "end": 2160}
    steps["introduction"] = {"start": 2160, "end": 2220}
    valid, error = check_schedule(scenario, steps)
    if not valid:
        return {"status": "error", "reason": "Independent schedule check failed: " + error}
    return {"status": "feasible_within_model", "quantity": scenario["quantity"],
            "delivery_by_minute": steps["deliver"]["end"], "steps": steps,
            "retained_wipe_records": scenario["completed_wipe_ids"],
            "new_wipes": scenario["quantity"] - len(scenario["completed_wipe_ids"]),
            "organizations": {key: offer["organization"] for key, offer in offers.items()},
            "note": "A proposed schedule only; no approval, reservation, or real-world delivery"}
