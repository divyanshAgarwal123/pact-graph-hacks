# PACT — Graph Hacks submission draft

**Track:** Agents That Act on Connected Data (Track 01)

**Project:** PACT — graph-grounded coalition recovery

**One-line pitch:** When a partner withdraws from a shared project, PACT finds a feasible replacement across connected offers while preserving work already completed.

**Description:** Four initial synthetic organizations contribute retired laptops, data wiping, preparation and a school room; two more provide backup wiping offers. Their capacities, windows and requirements live in FalkorDB. PACT traverses goal-to-requirement-to-offer-to-organization paths, compares available partner combinations, and uses a bounded schedule solver with an independent checker to explain which plan meets a 15:00 deadline. A simulated wiping-provider withdrawal keeps ten completed device records, activates two alternative offers, selects the one that fits and explains why the later offer misses the deadline. Preset and bounded judge-chosen counterfactuals can change the winning partner or block the plan by changing only graph-stored offer terms. A local model selects three allowlisted graph tools executed through MCP and may request a separate guarded action: saving a revision-bound proposal for human review. No provider is contacted or approved.

**Why FalkorDB is central:** FalkorDB is the only current state store. It connects goals, requirements, offers, organizations, device work records, a historical failure episode, revision-linked change events and pending proposals. The decision changes when an offer, window or completed-work path changes; the graph also records which supported change caused a revision. Without the database, partner discovery and scheduling fail.

**Technical proof to demonstrate:** Reset to the 14:00 original witness; simulate withdrawal; show ten retained wipe records, W2 chosen for a 14:30 delivery, W3 rejected, old W2 failure judged obsolete against its current rate, and a pending proposal saved only at the current revision. Slow W2 to its historical failed rate to block the plan, then move W3 earlier to rescue the goal by 14:00 without discarding W2's applicable failure history. Enter 7/hour and 10:15 as judge-chosen terms to show an uncanned 14:15 W3 result. The earlier proposal becomes stale; the revision-linked ledger shows which offer terms changed. Show the live first-offer comparison and the [clean GitHub Actions run](https://github.com/divyanshAgarwal123/pact-graph-hacks/actions/runs/38826376488); the four-case comparison is in [EVALUATION.md](EVALUATION.md). The complete walkthrough is in [DEMO.md](DEMO.md); model, queries and setup are in [README.md](README.md) and [CYPHER.md](CYPHER.md).

**AI assistance disclosure:** Codex assisted with architecture review, implementation, verification, documentation, UI and demo production. The local model in the product chooses bounded tools. The edited working-browser demo uses the installed macOS computer voice for narration and shortens model waiting time. The entrant is responsible for reviewing the technical work, submitting it and explaining it.

**Limits:** One synthetic, fixed-sequence scenario; at most 256 partner combinations and one van trip. A feasible result is a proposed schedule under declared facts, not a reservation, data-wiping certification or real-world delivery. No measured general agent-memory benefit is claimed.

## Submission links and remaining assets

- Public source repository: [divyanshAgarwal123/pact-graph-hacks](https://github.com/divyanshAgarwal123/pact-graph-hacks) (public; source verified on the default branch)
- Playable demonstration video: [PACT working browser demo](https://divyanshagarwal123.github.io/pact-graph-hacks/) — 2:47, captions and computer narration
- Direct video: [MP4](https://divyanshagarwal123.github.io/pact-graph-hacks/PACT-demo.mp4)
- Verified implementation fix: [95050e8](https://github.com/divyanshAgarwal123/pact-graph-hacks/commit/95050e89ae04ae2c7967f4a6ebd868f41de2b762); [passing clean-runner checks](https://github.com/divyanshAgarwal123/pact-graph-hacks/actions/runs/39029201162)
- Live deployment: **not required; complete local setup is in README**
- Final submission receipt: **pending**

## Final form check

- Name Track 01 and use only claims reproduced by the current commit and video.
- Include the public repo, playable video, README setup, Cypher/graph model, and AI assistance disclosure.
- Verify the video and repo without a signed-in session.
- Submit before 18 October 2026, 11:59 PM IST, then retain the receipt.
