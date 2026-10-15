# PACT — Graph Hacks submission draft

**Track:** Agents That Act on Connected Data (Track 01)

**Project:** PACT — graph-grounded coalition recovery

**One-line pitch:** When a partner withdraws from a shared project, PACT finds a feasible replacement across connected offers while preserving work already completed.

**Description:** Four initial synthetic organizations contribute retired laptops, data wiping, preparation and a school room; two more provide backup wiping offers. Their capacities, windows and requirements live in FalkorDB. PACT traverses goal-to-requirement-to-offer-to-organization paths, compares available partner combinations, and uses a bounded schedule solver with an independent checker to explain which plan meets a 15:00 deadline. A simulated wiping-provider withdrawal keeps ten completed device records, activates two alternative offers, selects the one that fits and explains why the later offer misses the deadline. Live counterfactuals can change the winning partner or block the plan by changing only graph-stored offer terms. A local model calls three allowlisted graph tools and may request one guarded action: saving a revision-bound proposal for human review. No provider is contacted or approved.

**Why FalkorDB is central:** FalkorDB is the only current state store. It connects goals, requirements, offers, organizations, device work records, a historical failure episode, case revisions and pending proposals. The decision changes when an offer, window or completed-work path changes. Without the database, partner discovery and scheduling fail.

**Technical proof to demonstrate:** Reset to the 14:00 original witness; simulate withdrawal; show ten retained wipe records, W2 chosen for a 14:30 delivery, W3 rejected, old W2 failure judged obsolete against its current rate, and a pending proposal saved only at the current revision. Slow W2 to its historical failed rate to block the plan, then move W3 earlier to rescue the goal by 14:00 without discarding W2's applicable failure history. The earlier proposal becomes stale. Show the integration suite and the four-case first-offer comparison in [EVALUATION.md](EVALUATION.md). The complete walkthrough is in [DEMO.md](DEMO.md); model, queries and setup are in [README.md](README.md) and [CYPHER.md](CYPHER.md).

**AI assistance disclosure:** Codex assisted with architecture review, implementation, verification, documentation and UI. The local model in the product chooses bounded tools. The entrant is responsible for reviewing the technical work, submitting it and explaining it.

**Limits:** One synthetic, fixed-sequence scenario; at most 256 partner combinations and one van trip. A feasible result is a proposed schedule under declared facts, not a reservation, data-wiping certification or real-world delivery. No measured general agent-memory benefit is claimed.

## Links to fill after final review

- Public source repository: **pending**
- Playable demonstration video: **pending**
- Live deployment: **not required; complete local setup is in README**
- Final submission receipt: **pending**

## Final form check

- Name Track 01 and use only claims reproduced by the current commit and video.
- Include the public repo, playable video, README setup, Cypher/graph model, and AI assistance disclosure.
- Verify the video and repo without a signed-in session.
- Submit before 18 October 2026, 11:59 PM IST, then retain the receipt.
