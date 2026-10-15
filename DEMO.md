# PACT judge demo script (target: 2–3 minutes)

Record a real screen walkthrough of the running local app and briefly show FalkorDB Browser or the Cypher catalogue. Do not label a proposal as an approval or a real delivery.

1. **Problem, 20 seconds.** Four synthetic organizations have parts of a school laptop project. A coordinator needs 20 prepared devices by 15:00; one provider can withdraw after work has started.
2. **Original graph decision, 25 seconds.** Click **Reset scenario**. Show the `Goal → Requirement ← Offer ← Organization` path and the independently checked 14:00 schedule. Explain that the graph holds the offers, quantities and windows; OR-Tools checks a schedule from those facts.
3. **Disruption, 35 seconds.** Click **Simulate provider withdrawal**. Point to ten retained wipe records and the case revision. W2 can complete the rest; W3 also exists but its late window misses the deadline. Show both paths and the rejected alternative. Delivery shifts to 14:30.
4. **Agent decision and safe action, 35 seconds.** Click **Create checked proposal**. Show the three MCP graph reads, separate guarded action, evidence IDs, historical W2 rate of five/hour versus the current ten/hour, and the pending human-review proposal ID. State that no reservation, approval, external message or physical work occurs.
5. **Counterfactual and failure honesty, 35 seconds.** Click **W2 slows to old rate**: both backups now miss the goal, and W2's old failure applies. Click **W3 rescues slow W2**: W3 becomes feasible by 14:00 without erasing that W2 history. The earlier proposal is stale. Click **Baseline offers** to restore the 14:30 W2 plan. Point to `verify.py` for damaged-replay and stale-write checks and to `EVALUATION.md` for the first-offer comparison.
6. **Why FalkorDB, 15 seconds.** Show the Cypher graph paths and pending proposal in the browser or README. Stop the database or point to the measured error behavior: the product cannot discover partners or schedule without FalkorDB.

## Before uploading

- Rehearse the exact commands in README and use the current commit.
- Capture live behavior, legible text, sound, and the entire browser flow; inspect the exported video and its link signed out.
- Include the repo URL, video URL, primary Track 01, complete local setup, and AI assistance disclosure in the final form.
- Keep any real names, contacts, personal files, tokens, and unsupported impact claims out of the recording.
