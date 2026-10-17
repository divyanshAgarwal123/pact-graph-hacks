# PACT judge demo script (target: 2–3 minutes)

The [Unlisted YouTube demo](https://www.youtube.com/shorts/gZWB60hv4WM) is published and playback is verified. The [chaptered browser player](https://divyanshagarwal123.github.io/pact-graph-hacks/) also plays the 2:47 video publicly. Source video, player, poster, captions and transcript are in `docs/`. It captures the live synthetic app and published Cypher on 17 October 2026, with disclosed computer narration; model waiting time is shortened. The YouTube link is entered in the required submission field. The earlier API-replay video remains a separate local fallback.

Record a real screen walkthrough of the running local app and briefly show FalkorDB Browser or the Cypher catalogue. Do not label a proposal as an approval or a real delivery.

1. **Problem, 20 seconds.** Four synthetic organizations have parts of a school laptop project. A coordinator needs 20 prepared devices by 15:00; one provider can withdraw after work has started.
2. **Original graph decision, 25 seconds.** Click **Reset scenario**. Show the `Goal → Requirement ← Offer ← Organization` path and the independently checked 14:00 schedule. Explain that the graph holds the offers, quantities and windows; OR-Tools checks a schedule from those facts.
3. **Disruption, 35 seconds.** Click **Simulate provider withdrawal**. Point to ten retained wipe records and the case revision. W2 can complete the rest; W3 also exists but its late window misses the deadline. Show both paths and the rejected alternative. Delivery shifts to 14:30.
4. **Agent decision and safe action, 35 seconds.** Click **Create checked proposal**. Show the three MCP graph reads, separate guarded action, evidence IDs, historical W2 rate of five/hour versus the current ten/hour, and the pending human-review proposal ID. State that no reservation, approval, external message or physical work occurs.
5. **Counterfactual and failure honesty, 50 seconds.** Click **W2 slows to old rate**: both backups now miss the goal, and W2's old failure applies. Click **W3 rescues slow W2**: W3 becomes feasible by 14:00 without erasing that W2 history. Show the live comparison: the first-active-offer policy blocks, while PACT checks W3 and proposes a feasible continuation. Then choose W2 rate **7** and W3 start **10:15** in **Test these terms**: the same graph-backed planner selects W3 for 14:15. Point to the revision-linked change ledger and the earlier proposal marked stale. Click **Baseline offers** to restore the 14:30 W2 plan. Point to `verify.py` for damaged-replay and stale-write checks and to `EVALUATION.md` for the separate four-case comparison.
6. **Why FalkorDB, 15 seconds.** Show the Cypher graph paths and pending proposal in the browser or README. Stop the database or point to the measured error behavior: the product cannot discover partners or schedule without FalkorDB.

## Before uploading

- Rehearse the exact commands in README and use the current commit.
- Capture live behavior, legible text, sound, and the entire browser flow; inspect the exported video and its link signed out.
- Include the repo URL, video URL, primary Track 01, complete local setup, and AI assistance disclosure in the final form.
- Keep any real names, contacts, personal files, tokens, and unsupported impact claims out of the recording.
