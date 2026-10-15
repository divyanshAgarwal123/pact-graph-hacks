# Local verification log

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
| `uv run python verify.py` | Disposable-graph suite passed base and partner-switch cases, six blocked constraints, atomic withdrawal failure when a device is missing, damaged-replay rejection, solver-uncertainty handling, stale/current proposal writes, new-connection persistence and concurrent snapshots |
| Current `qwen3:8b` agent after reliability fixes | Returned `present_plan`, marked old W2 rate episode `obsolete`, called all three inspection tools then `record_pending_proposal`, and saved proposal `a2c1d38a-…` at revision 2 |
| Pending proposal + FalkorDB restart | Revision 2, ten completed records, selected W2 and pending proposal `dc7d8929-…` remained after container restart |
| `benchmark.py --runs 30` | One warm local recovery case, seven graph calls/run: graph scenario p50 3.864 ms/p95 6.297 ms; solver/checker p50 2.750 ms/p95 3.238 ms; combined p50 6.587 ms/p95 9.616 ms. This excludes the local model, network browser path, cold start and concurrent load. |
| Current local API on port 8765 | `/api/state` returned HTTP 200 with revision 2, ten retained records, two alternatives, selected W2, and current saved proposals. The original in-app-browser tab was not reverified after a transient connection error. |

The graph currently remains in the recovery demo state; run `pact.py seed` to restore the original case. The graph is disposable; no external organizational data or actual work is represented. The concurrent-read check covered one local writer and 20 reads, not load testing. These checks do not establish physical approvals, arbitrary recovery, deployment, public repo, final video or submission. The browser and agent checks cover the named local paths only.
