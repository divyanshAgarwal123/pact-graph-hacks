# PACT counterfactual evaluation

Run `UV_CACHE_DIR=/tmp/pact-uv-cache uv run python evaluate.py` with FalkorDB running. The script creates and deletes a separate `pact_evaluate` graph; it does not alter the browser demo. Observed October 16 and reproduced October 17, 2026 IST after the case-identity fix.

The comparison policy picks the first active offer for each requirement, then runs **the same CP-SAT solver and independent schedule checker** as PACT. PACT checks all bounded active-offer combinations and chooses the earliest checked delivery. Both policies read the same FalkorDB scenario in each case. The baseline is a simple first-partner policy, not a claim about other hackathon entries or an optimized alternative system.

| Synthetic case after W withdraws | First-offer policy | PACT | W2 history applies? |
| --- | --- | --- | --- |
| Baseline terms | W2, 14:30 | W2, 14:30 | No |
| W3 available earlier | W2, 14:30 | W3, 14:00 | No |
| W2 slows to past failed rate; W3 late | Blocked | Blocked | Yes |
| W2 slow; W3 available earlier | Blocked | W3, 14:00 | Yes |

The last case is the meaningful recovery distinction: checking another connected offer finds a feasible continuation without discarding an applicable warning about W2. The earlier-W3 case saves 30 modeled minutes against the first-offer policy. The blocked case stays blocked rather than inventing a partner.

These are four hand-built variants of one fixed workflow and one synthetic dataset. They support this case's decisions only. They do not measure generalized reliability, memory benefit, real-world delivery, performance against other entrants, or win probability. The model agent is outside this policy comparison; its guarded action is checked separately in `verify.py` and `VERIFICATION.md`.

The browser also accepts bounded, judge-chosen W2 rate and W3 start values after withdrawal. A separate local API check used 7 devices/hour and 10:15, yielding a checked W3 delivery at 14:15. That input is outside the four rows above; it is an additional functional check, not an independent benchmark.
