# Codex Council result: PACT at Graph Hacks

## Recommendation

Enter Track 01 as the primary track. Complete a graph-grounded contingency decision with competing offers, revision-safe recovery, visible evidence paths and a pending human-review proposal. Treat Track 02 as conditional on a demonstrated two-agent handoff, isolated memory and measured benefit.

## Council Result

Six independent first opinions agreed on Track 01 fit; none endorsed Track 02 for the current one-agent implementation. Two anonymous reviewers ranked Candidate E and F highest in different orders: the coverage reviewer favored the judge-visible recovery outcome and fair baseline; the performance reviewer favored explicit latency and query measurements. Deterministic score aggregation ranked E first but marked the original recommendations **blocked** because each omitted at least one material defect. A revised bounded local build plan received **GO** from both reviewers. Confidence is **medium** for that plan and **blocked** for submission readiness. Codex role diversity is not independent model-provider diversity.

## Blocking Issues

- Current submission lacks a verified public repository, demo video and final submission receipt.
- Track 02 lacks distinct agent handoff, per-user isolation, high-concurrency write evidence and a controlled memory comparison.
- A claimed broad real-world collaboration system would overstate one synthetic case. Keep scope and demo claims bounded.

## Refinements

- Preserve every active offer; compare feasible and rejected partner combinations.
- Show graph paths and the reason each alternative fails.
- Measure correctness before latency and keep model, graph and solver timing separate.

## Implementation Shape

`pact.py` owns graph facts, one-query withdrawal and case revisions. `planner.py` evaluates bounded offer combinations and checks witnesses. `agent.py` uses allowlisted inspection tools and can explicitly request one guarded action that writes only pending revision-bound proposals after deterministic checks. `app.py` and `web/` show selected and rejected graph paths. `verify.py` exercises a disposable graph. No physical action or approval is automated.

## Verification

Run `UV_CACHE_DIR=/tmp/pact-uv-cache uv run python verify.py` with the Docker graph. Check a competing-offer choice and switch, unchanged replay, incomplete-device mutation rejection, stale proposal rejection, concurrent snapshots, unavailable database, restart persistence, and a real browser review action. Inspect final README, graph queries, video and public repository before submission.

## Performance Impact

The agent has up to five 45-second model calls; the solver has a three-second per-combination cap and evaluates at most 256 combinations. These are upper bounds, not measured latency or scalability evidence. Report p50/p95 only over documented repeated workloads. Indexes and extra batching should follow a measured bottleneck.

## Audit Notes

Official sources: [event](https://www.wemakedevs.org/hackathons/falkordb), [rules](https://www.wemakedevs.org/hackathons/falkordb/rules), [organizer guide](https://www.wemakedevs.org/blogs/how-to-build-an-agent-that-reasons-over-a-graph). Member opinions, anonymous candidates, reviewer scores, revision and preflight estimate are saved in this session. The official event pages do not publish exact weights or a judge list. Winning probability is unknown.
