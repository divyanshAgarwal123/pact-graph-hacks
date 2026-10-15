# PACT technical explanation for judge questions

Use these as prompts to explain the code in your own words, not as claims of work beyond the demo.

**What problem does PACT solve?** It proposes a schedule for a synthetic school laptop project where different organizations contribute devices, wiping, preparation and a room. When a provider withdraws, it keeps recorded completed work and checks replacement offers against the deadline.

**Why a graph?** The relevant facts are connections: a goal requires a capability, an offer satisfies it, an organization makes that offer, and devices have completion records. PACT traverses those paths to find current partners and retains the evidence path for each chosen or rejected alternative. The planner cannot construct this case if FalkorDB is unavailable. This does not prove graphs outperform every flat or relational design.

**What does FalkorDB do, and what does OR-Tools do?** FalkorDB holds the current graph, episodes, revisions and pending proposals. Fixed, parameterized Cypher queries retrieve connected facts. OR-Tools searches a bounded schedule for each partner combination. A separate checker rejects a schedule that violates durations, windows, order, room availability or deadline.

**What does the agent decide or do?** The local model chooses among three allowlisted read-only tools and then explicitly requests a bounded `record_pending_proposal` action. It cannot write Cypher. Deterministic checks decide whether the current graph supports a plan and whether an old failure is still applicable. The action records a pending proposal only when the checked case is feasible and the revision is unchanged. It does not approve, reserve, contact or deliver anything.

**What is the memory example?** A past W2 episode says capacity failed at five devices/hour. The current offer states ten/hour, so the historical failure is not treated as a permanent blacklist. Changing today's rate back to five/hour blocks the schedule. This is a bounded stale-fact check, not evidence of a general memory advantage.

**How does recovery avoid partial progress loss?** The simulated withdrawal is one Cypher write requiring all ten completed device nodes. It deactivates W, activates W2 and W3, records ten wipes, creates an episode and advances the revision. Replaying it does not repeat the change. The disposable-graph test tries a missing device and verifies that no partial mutation appears.

**How do you avoid stale proposals?** Each supported case mutation advances a revision node. Proposal creation matches the expected revision and writes in one graph query; a stale match creates no proposal. The UI can label old proposals as not current. Direct manual database edits outside these supported writes are outside this guarantee.

**What changes when a judge tries another offer?** Four counterfactual controls make bounded, revisioned graph writes after withdrawal. Earlier W3 availability switches the checked partner to W3 and delivers by 14:00. Reducing W2 to its historically failed rate with W3 still late blocks the proposal and makes the old episode applicable. Moving W3 earlier then rescues the goal while leaving W2's applicable failure history intact. Restoring the baseline picks W2 again. Completed device records stay intact, and earlier proposals remain stored but stale.

**Why Track 01 instead of Track 02 or 03?** The current differentiator is a graph-grounded action on connected offers with an explanation path. There is one model agent, no proven multi-agent handoff or per-tenant memory isolation, and no company document corpus. Those gaps make Track 02 and 03 claims premature.

**What is not proven?** All organizations and records are synthetic; no source verifies that a real provider owns devices, has a certified wipe process, accepts the plan, or can deliver it. The workflow is fixed, capped at 256 partner combinations and one van trip. A 30-run warm local timing sample excludes the model, cold start and concurrent load. No winning probability has been measured.

**What did AI assistance contribute?** Codex helped plan, implement, test, review and document the project. The entrant is responsible for understanding and verifying the code and for the final submission.
