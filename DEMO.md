# PACT judge demo script (target: 2–3 minutes)

Record a real screen walkthrough of the running local app and briefly show FalkorDB Browser or the Cypher catalogue. Do not label a proposal as an approval or a real delivery.

1. **Problem, 20 seconds.** Four synthetic organizations have parts of a school laptop project. A coordinator needs 20 prepared devices by 15:00; one provider can withdraw after work has started.
2. **Original graph decision, 25 seconds.** Click **Reset scenario**. Show the `Goal → Requirement ← Offer ← Organization` path and the independently checked 14:00 schedule. Explain that the graph holds the offers, quantities and windows; OR-Tools checks a schedule from those facts.
3. **Disruption, 35 seconds.** Click **Simulate provider withdrawal**. Point to ten retained wipe records and the case revision. W2 can complete the rest; W3 also exists but its late window misses the deadline. Show both paths and the rejected alternative. Delivery shifts to 14:30.
4. **Agent decision and safe action, 35 seconds.** Click **Create checked proposal**. Show the three tool calls, graph evidence IDs, historical W2 rate of five/hour versus the current ten/hour, and the pending human-review proposal ID. State that no reservation, approval, external message or physical work occurs.
5. **Failure honesty, 25 seconds.** In a separate synthetic verification run, show one changed rate or deadline returning blocked, and `verify.py` passing stale-write and partial-withdrawal checks. Explain that missing or stale facts do not become confident plans.
6. **Why FalkorDB, 15 seconds.** Show the Cypher graph paths and pending proposal in the browser or README. Stop the database or point to the measured error behavior: the product cannot discover partners or schedule without FalkorDB.

## Before uploading

- Rehearse the exact commands in README and use the current commit.
- Capture live behavior, legible text, sound, and the entire browser flow; inspect the exported video and its link signed out.
- Include the repo URL, video URL, primary Track 01, complete local setup, and AI assistance disclosure in the final form.
- Keep any real names, contacts, personal files, tokens, and unsupported impact claims out of the recording.
