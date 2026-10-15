# Local verification log

Observed October 16, 2026 IST, after the official coding window opened. These checks used the synthetic `pact_demo` graph and the FalkorDB Docker image pinned in `compose.yaml`.

| Check | Observed result |
| --- | --- |
| `uv sync --locked` | Resolved 18 packages; checked 14 |
| `pact.py seed` | Created goal, four requirements, four offers, and four organizations; traversal covered all requirements |
| `docker compose restart graph` followed by `pact.py candidates` | Four candidate offers remained available after restart |
| Unavailable port 6399 | Client raised connection refused; no fallback result |
| `pact.py plan` | Independent checker accepted a 20-device witness: wiping 09:00–11:00, transfer 11:00–11:30, preparation 11:30–13:30, delivery 13:30–14:00 |
| Donor quantity changed from 24 to 18 | Planner returned `blocked` for insufficient declared quantity |
| Goal deadline changed from 15:00 to 13:30 | Solver returned `blocked` for no schedule fitting the window |
| Delivery witness deliberately altered | Independent checker rejected it for wrong duration |
| Simulated W withdrawal and W2 activation | Ten existing wipe records retained; ten new wipes scheduled; delivery by 14:30 |
| Withdrawal command repeated | Still ten wipe records and one active backup offer |
| Backup rate reduced to 5/hour | Recovery schedule blocked |
| Backup offer disabled | Recovery blocked for missing wiping offer |
| FalkorDB restarted during recovery state | Ten records and the 14:30 recovery plan remained available |
| Old W2 episode queried at current rate 10/hour | Memory marked obsolete; old failure did not blacklist W2 |
| W2 rate reduced to the historical 5/hour | Memory marked applicable; planner blocked the schedule; rate restored to 10/hour |
| Local `qwen3:8b` agent reviewed recovery | Model called `inspect_connections`, `check_schedule`, and `recall_failure`; deterministic gate returned `present_plan` and `obsolete` |
| Local browser walkthrough | Reset changed delivery from 14:30 to 14:00; withdrawal restored W2 and 14:30; agent panel displayed tool trace and evidence IDs |

The graph currently remains in the recovery demo state; run `pact.py seed` to restore the original case. The graph is disposable; no external organizational data or actual work is represented. These checks do not cover concurrency, approvals, arbitrary recovery, deployment, or the final submission. The browser and agent checks cover the named local paths only.
