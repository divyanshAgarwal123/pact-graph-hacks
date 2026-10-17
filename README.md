# PACT — graph-backed collaboration planning

[![Verify PACT](https://github.com/divyanshAgarwal123/pact-graph-hacks/actions/workflows/verify.yml/badge.svg)](https://github.com/divyanshAgarwal123/pact-graph-hacks/actions/workflows/verify.yml)

Graph Hacks 2026 entry in progress. PACT explores whether a coordinator can assemble and recover a multi-organization collaboration from connected offers, constraints, evidence, and remembered outcomes. All current fixture data is synthetic. The primary track is **Agents That Act on Connected Data**. Track 02 remains conditional on a tested handoff between distinct agents; the present build does not claim shared agent coordination or a measured memory advantage.

## Status

Phases 1–3, a narrow recovery slice, and a local judge walkthrough are working. FalkorDB stores the case and discovers candidate offers by traversing `Goal → Requirement ← Offer ← Organization`. The planner keeps competing offers, reads current quantities, availability, rates, and deadline from the graph, uses OR-Tools CP-SAT to check each bounded partner combination, and independently checks schedule witnesses. A synthetic withdrawal preserves completed device records and exposes two backups. W2's 14:30 proposal fits while W3's later slot misses the deadline. Four counterfactual presets and bounded judge-chosen W2 rate/W3 start controls update live graph terms, so the selected partner can change or the plan can become blocked. The browser compares each checked result with a first-active-offer policy using the same graph facts and solver run. Revision-linked graph events show which terms changed, while earlier proposals remain visible as stale. A local model chooses bounded graph inspections that execute through an official MCP client and then explicitly requests a separate guarded action to record a revision-bound pending proposal in FalkorDB for human review. These are narrow synthetic feasibility results. They do **not** establish approvals, real-world delivery, general recovery, or a measured agent memory benefit.

## Run

Requires Docker Compose and Python 3.10+ with [`uv`](https://docs.astral.sh/uv/getting-started/installation/). The optional agent review needs [Ollama](https://ollama.com/) and `qwen3:8b`. The graph, planning and integration verification need no model.

```sh
docker compose up -d
UV_CACHE_DIR=/tmp/pact-uv-cache uv sync --locked
UV_CACHE_DIR=/tmp/pact-uv-cache uv run python pact.py seed
UV_CACHE_DIR=/tmp/pact-uv-cache uv run python pact.py candidates
UV_CACHE_DIR=/tmp/pact-uv-cache uv run python pact.py plan
UV_CACHE_DIR=/tmp/pact-uv-cache uv run python verify.py
UV_CACHE_DIR=/tmp/pact-uv-cache uv run python evaluate.py
UV_CACHE_DIR=/tmp/pact-uv-cache uv run python pact.py withdraw
UV_CACHE_DIR=/tmp/pact-uv-cache uv run python pact.py plan
```

For the interactive walkthrough, download the model once and start Ollama in one terminal, then run the service in another:

```sh
ollama pull qwen3:8b
ollama serve
UV_CACHE_DIR=/tmp/pact-uv-cache uv run uvicorn app:app --host 127.0.0.1 --port 8765
```

Open `http://127.0.0.1:8765`. The graph and schedule work without Ollama; the agent review button needs the model. `PACT_MODEL` and `OLLAMA_URL` can override the local defaults. This demonstration is bound to localhost and has no login. Do not expose it publicly as a writable service.

`mcp_server.py` exposes `inspect_connections`, `check_schedule`, and `recall_failure` as read-only [MCP](https://github.com/modelcontextprotocol/python-sdk) tools. The local agent uses the official SDK client in-process to execute each model-selected inspection. External MCP hosts can start the same server over stdio with `UV_CACHE_DIR=/tmp/pact-uv-cache uv run python mcp_server.py`; stdout is reserved for the protocol. The model's `record_pending_proposal` request is handled by a separate revision-checked application action, not advertised as an MCP write tool. This is one model agent, not a multi-agent coordination claim.

Watch the [2:47 working browser demo](https://divyanshagarwal123.github.io/pact-graph-hacks/) or [open the MP4](https://divyanshagarwal123.github.io/pact-graph-hacks/PACT-demo.mp4). Public playback and chapter seeking were verified on 17 October, along with anonymous file access. It shows the actual local browser workflow and published Cypher, with captions and disclosed computer narration. Model waiting time is shortened; all scenario data is synthetic. The [judge walkthrough](DEMO.md), [counterfactual evaluation](EVALUATION.md), and [submission packet](SUBMISSION_DRAFT.md) provide the supporting evidence and AI disclosure. The organizer's form specifically requires a public or unlisted YouTube URL; that upload is still pending. The Pages site is a video player, not a live PACT app deployment.

The demo graph is named `pact_demo`; `seed` replaces only that disposable graph. `verify.py` uses and deletes a separate `pact_verify` graph. `withdraw` simulates W's withdrawal at 10:00, keeps wipe records for L01–L10, and activates W2 and W3 for the remaining ten devices in one graph query. Repeating `withdraw` is idempotent only when all ten records, both backup activations, and a revision of at least 2 remain intact. Run `seed` to restore the original case. FalkorDB listens at `127.0.0.1:6389` to avoid a common local Redis port conflict. Its browser listens at `127.0.0.1:3009`. Docker Compose keeps a named volume for persistence. Queries fail if the database is unavailable.

After withdrawal, the browser's **Live counterfactuals** controls update only the synthetic W2 rate and W3 window. Every changed set of terms advances the case revision; repeating the same setting is a no-op. Earlier proposals remain stored but are marked stale against the new revision. The HTTP endpoints are `POST /api/contingency/baseline`, `/early_w3`, `/slow_w2`, and `/rescue_w3`. They reject changes before withdrawal.

Every reset creates a new case identity. Agent inspections and the atomic proposal write check both that identity and the numeric revision, so an in-flight proposal from an earlier case cannot be saved after a reset reuses the same revision number. If upgrading an existing demo graph created before this identity check, click **Reset scenario** once; missing identities fail visibly rather than bypassing the guard.

The **Test these terms** form lets a judge choose W2's rate from 4–12 devices/hour and W3's start from 09:30–12:00 in 15-minute steps. W3 keeps a one-hour window. `POST /api/custom-terms` accepts `{"w2_rate":7,"w3_start_minute":615}` after withdrawal; that example checks W3 for a 14:15 modeled delivery. The bounds keep this synthetic one-trip workflow inspectable; the values are still written to FalkorDB and checked by the ordinary planner, not mapped to a preset answer.

## Graph model and central query

See the [Cypher and graph-model catalogue](CYPHER.md) for the executed traversal, atomic recovery and proposal queries.

- `Goal` requires `Requirement` nodes with explicit quantities.
- An `Organization` makes an `Offer` with an explicit quantity.
- An active `Offer` may satisfy a `Requirement` when its quantity covers the remaining work.
- `Offer → Device` links the donor's declared device records to its batch.
- `Device → WipeRecord` preserves simulated completed work across a withdrawal and database restart.
- `Episode → Organization → Offer` lets the agent retrieve a prior capacity failure and compare its old rate with the current offer. A separate episode records the simulated withdrawal and its completed device records.
- `Revision → CaseEvent → Offer` records supported changes and their before-and-after terms; withdrawal events also link to the recorded episode.
- `Revision → Proposal` links a pending review item to the case. `Proposal` stores checked offer IDs, evidence IDs, delivery minute, and case revision. Proposal creation checks the current revision and writes in one query.

```cypher
MATCH (goal:Goal {id:$goal})-[:REQUIRES]->(r:Requirement)
      <-[:SATISFIES]-(offer:Offer)<-[:MAKES]-(org:Organization)
WHERE coalesce(offer.active,true) = true
RETURN r.id, r.quantity, org.id, org.name, offer.id, offer.quantity
ORDER BY r.id, org.id
```

Candidate coverage checks an offer's quantity against the required quantity after subtracting completed `Device → WipeRecord` paths. It does not trust a separate mutable completion counter. The planner evaluates each active offer combination, returns the selected graph paths, and records why other combinations failed. It caps the search at 256 combinations rather than silently dropping offers. A timeout, unproven optimum, or failed independent check for any combination makes the overall result unresolved.

FalkorDB is the only store for this state. Removing it makes discovery and scheduling fail. The checker verifies quantities, unique donor device records, each step's duration and time window, task order, room use, and delivery deadline. The current solver models a single van trip, the fixed wipe → transfer → prepare → deliver path, and a fixed Day 2 clinic/introduction. It searches bounded partner combinations but not split batches, arbitrary workflow graphs, or real approvals. A pending proposal is never a reservation or approval. Supported writes advance the revision; direct manual database edits outside the app do not. Later gates add broader recovery and measured conditional memory. Do not treat this slice as a complete submission.

## Phase gates

| Gate | Current evidence | Next test |
| --- | --- | --- |
| 1 — Graph foundation | Live query found four organizations; query survived container restart; unavailable endpoint returned an error | Preserve local reproducibility |
| 2 — Feasible schedule | 20-device witness delivered by 14:00; 18-device and 13:30-deadline variants blocked; tampered witness rejected | Expand beyond the fixed one-trip workflow |
| 3 — Recovery and graph action | Ten simulated wipe records survived withdrawal and replay; a damaged replay was rejected. W2 delivered by 14:30 while W3 missed the deadline. The old 5/hour failure was rejected as obsolete against W2's current 10/hour offer. A checked pending proposal survived a database restart; stale writes were rejected. | Broader disruption set and measured outcomes |
| 4 — Product and submission | Browser walkthrough verified reset, withdrawal, a live model proposal, blocked/rescue cases, comparison, change ledger, stale proposal and judge-chosen terms on 17 October. Reset-race regressions passed locally and on a clean GitHub runner; custom state persisted across Docker restart. Phone-width and keyboard checks passed. Public video playback and seeking work. Seven of eight required form answers are staged. | Required YouTube URL, participant review and final submission authorization |

## Interpretation

The current graph stores declared contributions, not proof of ownership or data-wiping certification. A `feasible_within_model` result is a proposed schedule under the synthetic assumptions. It does not reserve a device, collect anyone's approval, or record physical work. OR-Tools provides the constraint search; FalkorDB provides the only current collaboration state and the path from goal to offers. The local model chooses from three allowlisted read-only MCP tools and can request one guarded `record_pending_proposal` action. Deterministic checks set the final recommendation, memory applicability, and whether that action may write at the current revision. No arbitrary Cypher or unrestricted mutation tool is exposed to the model. The outcome of the controlled memory experiment is still unknown.

## Build provenance

Main code began October 16, 2026 IST, within the organizer's [October 15–18 build window](https://www.wemakedevs.org/hackathons/falkordb/schedule). Pre-event PACT notes and synthetic scenario sketches existed; implementation started during the event. **AI assistance disclosure:** Codex assisted with architecture review, implementation, tests, documentation, and UI. Divyansh must review and be able to explain the source, model, queries, evaluation, and demo before submission.
