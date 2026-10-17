# Local verification log

## Publication and demo production — 17 October 2026 IST

- Case-identity fix published at [95050e8](https://github.com/divyanshAgarwal123/pact-graph-hacks/commit/95050e89ae04ae2c7967f4a6ebd868f41de2b762). Its [clean-runner integration and comparison checks](https://github.com/divyanshAgarwal123/pact-graph-hacks/actions/runs/39029201162) passed.
- Actual browser workflow and published Cypher captured with the browser tool. Export is an edited 166.780-second H.264/AAC MP4 (672×948, 24 fps, 4,669,987 bytes), with computer narration and visible captions. Model waiting time is shortened. No application outcome is invented in the edit.
- Published video/player/captions/transcript at [528b0ba](https://github.com/divyanshAgarwal123/pact-graph-hacks/commit/528b0ba5f3af144bf38fd293301896fd80cd5444); that commit's [verification workflow](https://github.com/divyanshAgarwal123/pact-graph-hacks/actions/runs/39030084519) also passed.
- Decoded the full video, inspected a sample from each chapter, checked audio for unexpected prolonged silence, and verified browser playback. Chapter seeking worked against a range-capable local static server; browser reported the complete seekable interval, ready state 4 and no media error.
- Downloaded the public MP4 anonymously and compared all bytes with the reviewed export. SHA-256: `b6a24a021fcc237a117ef26250ff601b125b8bb130a298ef670507131db838e9`.
- GitHub's file page offers a download rather than inline playback. Public streaming-player activation is not complete: automatic approval review rejected the GitHub Pages configuration change pending explicit site-setting approval. No Pages setting was changed.
- The organizer's submission route was tried twice and displayed “Unavailable — Couldn't reach the server. Check your connection.” in this browser. No final form fields, submission action or receipt were obtained. Participant explanation/review and the form's actual video requirements remain final gates.

Review the local player at `http://127.0.0.1:8788/`; the app is separate at `http://127.0.0.1:8765/`. The prepared Pages source is branch `main`, folder `/docs`, containing only the video and static player assets.

## Recheck and reliability fix — 17 October 2026 IST

The existing implementation was preserved and tested against the pinned local Docker FalkorDB. The web and Ollama services were stopped at the start of this session and were started on localhost. These are fresh local observations; the previously published commit and CI do not include this session's changes yet.

| Check | Observed result |
| --- | --- |
| Installed environment and live graph | Existing locked environment imported FalkorDB, OR-Tools, FastAPI and MCP; pinned graph container was running |
| `verify.py` and `evaluate.py` | Integration suite and all four documented counterfactual comparisons passed |
| Reset/revision collision reproducer, before fix | An old feasible revision-3 proposal was accepted after reset into a different, blocked revision-3 case; reproduced only in a disposable graph |
| Case identity fix | Every reset now generates a fresh case ID; scenario reads, API snapshots, agent inspection checks and atomic proposal writes compare identity plus revision. Missing identities fail visibly and require one synthetic reset |
| Reset regression checks | Old-case proposal refused at a repeated revision; reset during a scenario read forced a retry; reset after model inspections and immediately before the guarded action returned unresolved and wrote no proposal. The action-race regression stubs model responses while executing real MCP tools against the disposable graph |
| Live local `qwen3:8b` browser review after fix | Three MCP inspections and a separate `record_pending_proposal` request completed; proposal `d90a5039-…` was saved at revision 2 |
| Browser counterfactuals and provenance | Original delivery 14:00; withdrawal retained ten wipe records and proposed W2 at 14:30; slowing W2 blocked the plan and marked its history applicable; W3 rescue proposed 14:00; saved revision-2 proposal became visibly stale. Comparison and revision-linked event ledger rendered |
| Browser custom form | W2 7/hour and W3 10:15 produced the checked W3 14:15 continuation at revision 5; first-offer policy blocked. Keyboard Tab reached the second select and submit button; Enter resubmitted the unchanged terms without advancing the revision |
| Phone viewport | At 390×844, document width remained 390px; schedule stacked and custom controls were operable. Temporary viewport was restored. This is a focused responsive check, not a full accessibility audit |
| Docker restart | Same case identity, revision 5, ten completed wipe records, 14:15 plan and stored proposal survived unchanged |
| Static checks | Python compilation, JavaScript syntax and `git diff --check` passed |

Screenshots are retained locally in `outputs/pact-working-demo-2026-10-17.jpg`, `outputs/pact-custom-recovery-2026-10-17.jpg`, and `outputs/pact-mobile-2026-10-17.jpg`. The running demo is left at the custom revision-5 case; **Reset scenario** restores the opening example. A playable public demo video and final submission receipt remain outstanding. No general memory-benefit, tenant-isolation, or production-concurrency result follows from these checks.

## Earlier checks — 16 October

Observed October 16, 2026 IST, after the official coding window opened. The manual walkthrough used the synthetic `pact_demo` graph; `verify.py` used and deleted a separate `pact_verify` graph. Both used the FalkorDB Docker image pinned in `compose.yaml`.

| Check | Observed result |
| --- | --- |
| Fresh source copy: `uv sync --locked` then `verify.py` | Installed 28 locked packages into a new virtual environment; disposable-graph integration suite passed against the local Docker FalkorDB |
| `pact.py seed` | Created goal, four requirements, six offers (two inactive backups), six organizations, donor-linked device records, and revision 1; traversal covered all requirements |
| `docker compose restart graph` followed by `pact.py candidates` | Four candidate offers remained available after restart |
| Unavailable port 6399 | Client raised connection refused; no fallback result |
| `pact.py plan` | Independent checker accepted a 20-device witness: wiping 09:00–11:00, transfer 11:00–11:30, preparation 11:30–13:30, delivery 13:30–14:00 |
| Donor quantity changed from 24 to 18 | Planner returned `blocked` for insufficient declared quantity |
| Goal deadline changed from 15:00 to 13:30 | Solver returned `blocked` for no schedule fitting the window |
| Delivery witness deliberately altered | Independent checker rejected it for wrong duration |
| Simulated W withdrawal and two backup activations | Ten wipe records retained; W2 chosen for ten new wipes and delivery by 14:30; W3 rejected because it misses the deadline |
| Withdrawal command repeated | Still ten wipe records, two active backups and revision 2 (no extra increment) |
| Backup rate reduced to 5/hour | Recovery schedule blocked |
| FalkorDB restarted during recovery state | Ten records and the 14:30 recovery plan remained available |
| Old W2 episode queried at current rate 10/hour | Memory marked obsolete; old failure did not blacklist W2 |
| W2 rate reduced to the historical 5/hour | Memory marked applicable; planner blocked the schedule; rate restored to 10/hour |
| Local `qwen3:8b` agent reviewed recovery | Model called `inspect_connections`, `check_schedule`, `recall_failure`, then explicitly requested `record_pending_proposal`; deterministic gates returned `present_plan` and `obsolete` and stored a pending proposal at revision 2 |
| Updated local browser walkthrough | Recovery page showed selected W2 path, rejected W3 path and reason; agent panel showed the tool trace, evidence IDs and a pending-human-review proposal ID |
| `uv run python verify.py` | Disposable-graph suite passed base and partner-switch cases, six blocked constraints, atomic withdrawal failure when a device is missing, damaged-replay rejection, simulated solver timeout and non-optimal result handling, stale/current proposal writes, new-connection persistence and concurrent snapshots |
| Current `qwen3:8b` agent after reliability fixes | Returned `present_plan`, marked old W2 rate episode `obsolete`, called all three inspection tools then `record_pending_proposal`, and saved proposal `a2c1d38a-…` at revision 2 |
| HTTP counterfactual flow after withdrawal | `early_w3` switched the winner to W3 at 14:00; `slow_w2` blocked the plan and made the old W2 episode applicable; `baseline` restored W2 at 14:30. Pre-withdrawal change returned HTTP 409. Revisions advanced 2→3→4→5. |
| Full HTTP agent and rescue flow | Local agent called its three inspection tools and `record_pending_proposal`, saving `a50926a9-…` at revision 2. `slow_w2` blocked the plan at revision 3 and marked the proposal stale. `rescue_w3` chose W3 for 14:00 at revision 4 while W2 history remained applicable; `baseline` restored W2 at revision 5. |
| Official MCP SDK tool path | An in-process client called all three read tools against the disposable graph. An external stdio MCP client discovered `check_schedule`, `inspect_connections`, and `recall_failure` and successfully called the live schedule tool. The local model completed an MCP-backed review and saved pending proposal `a7574662-…` at revision 5. The guarded write itself is not an MCP tool. |
| Current HTTP walkthrough after MCP integration | `/api/state` returned a feasible revision-5 case; `/api/agent-review` returned the three MCP read calls, a separate guarded action, and pending proposal `a47ea9a7-…` at the same revision. |
| `evaluate.py` first-offer comparison | On the same four synthetic graph cases and with the same solver/checker, PACT matched the first-offer policy in the baseline and blocked cases, delivered 30 modeled minutes earlier when W3 was early, and recovered the slow-W2 case via W3 where the first-offer policy blocked. See `EVALUATION.md`; no general memory or competition-performance claim follows. |
| Fresh current-source copy with MCP | Installed 44 locked packages into a new virtual environment; both `verify.py` and `evaluate.py` passed against the running local FalkorDB. |
| [GitHub Actions clean runner](https://github.com/divyanshAgarwal123/pact-graph-hacks/actions/runs/38826376488) | On public commit `0ff45fb`, Ubuntu installed locked dependencies, started the pinned FalkorDB container, passed `verify.py` including judge-chosen terms and `evaluate.py`, then removed the disposable graph. This does not cover the local Ollama agent, browser walkthrough, or video. |
| FalkorDB restart after counterfactuals | API still returned revision 5 baseline, ten retained wipe records, W2 selected, and saved proposal `a50926a9-…` marked stale. |
| Pending proposal + FalkorDB restart | Revision 2, ten completed records, selected W2 and pending proposal `dc7d8929-…` remained after container restart |
| `benchmark.py --runs 30` | One warm local recovery case, seven graph calls/run: graph scenario p50 3.864 ms/p95 6.297 ms; solver/checker p50 2.750 ms/p95 3.238 ms; combined p50 6.587 ms/p95 9.616 ms. This excludes the local model, network browser path, cold start and concurrent load. |
| Live first-offer comparison | The running server served the comparison HTML and JavaScript. Read-only `/api/state` at revision 5 showed a first-active-offer alternative and PACT both feasible at 14:30 under baseline terms; `evaluate.py` covers the other three graph variants. `node --check web/app.js` and `git diff --check` passed. The comparison's latest browser rendering remains unverified. |
| Revision-linked change ledger | Updated `verify.py` passed seed, withdrawal, replay, W2 rate change, W3 rescue, no-op, failed-write and proposal-link checks against a disposable graph. The local HTTP sequence returned revisions 1→2→3→4 with the expected before-and-after summaries and four graph events; `/api/reset` restored the demo to revision 1. `node --check web/app.js`, Python compilation and `git diff --check` passed. The ledger's browser rendering remains unverified. |
| Current model-agent HTTP flow after ledger change | The local `qwen3:8b` agent called `inspect_connections`, `check_schedule`, and `recall_failure` through MCP, then requested `record_pending_proposal`. The guarded action stored pending proposal `840489b5-…` at revision 2; after a rescue contingency advanced to revision 3, the API marked it stale. Reset restored the demo to revision 1. This confirms the HTTP and model path, not the browser rendering. |
| Judge-chosen backup terms | `verify.py` passed a non-preset W2 rate of 7/hour and W3 start of 10:15 on the disposable graph; W3 was selected for a checked 14:15 delivery with ten wipe records retained. The running HTTP API returned 409 before withdrawal, 422 for invalid bounds, revision 3 and matching event summaries for valid terms, and no new revision/event on replay. `/api/reset` restored revision 1. The new form's browser rendering remains unverified. |
| Earlier local API check on port 8765 | `/api/state` returned HTTP 200 with revision 2, ten retained records, two alternatives, selected W2, and current saved proposals. The original in-app-browser tab was not reverified after a transient connection error. |

The public GitHub repository was created with public visibility. Its default-branch `README.md` was independently fetched after the initial push. The demo graph currently remains at the original synthetic case, revision 1, after the model-agent HTTP check. The graph is disposable; no external organizational data or actual work is represented. The concurrent-read check covered one local writer and 20 reads, not load testing. These checks do not establish physical approvals, arbitrary recovery, deployment, final video or submission. The browser and agent checks cover the named local paths only; the counterfactual and ledger controls were verified through their HTTP endpoints, not a new browser walkthrough.
