# PACT — graph-backed collaboration planning

Graph Hacks 2026 entry in progress. PACT explores whether a coordinator can assemble and recover a multi-organization collaboration from connected offers, constraints, evidence, and remembered outcomes. All current fixture data is synthetic. The working track choice is **Agent Memory and Coordination**; its memory advantage remains an untested hypothesis.

## Status

Phases 1–2, a narrow recovery slice, and a local judge walkthrough are working. FalkorDB stores a four-party case and discovers candidate offers by traversing `Goal → Requirement ← Offer ← Organization`. The planner reads current quantities, availability, rates, and deadline from the graph, uses OR-Tools CP-SAT to construct a schedule for the declared workflow, and checks its witness independently. A synthetic withdrawal preserves completed device records and switches to a backup offer. A local model can choose bounded, read-only tools to review that proposal. These are narrow synthetic feasibility results. They do **not** establish approvals, real-world delivery, general recovery, or a measured agent memory benefit.

## Run

Requires Docker Compose and Python 3.10+ with `uv`.

```sh
docker compose up -d
UV_CACHE_DIR=/tmp/pact-uv-cache uv sync --locked
UV_CACHE_DIR=/tmp/pact-uv-cache uv run python pact.py seed
UV_CACHE_DIR=/tmp/pact-uv-cache uv run python pact.py candidates
UV_CACHE_DIR=/tmp/pact-uv-cache uv run python pact.py plan
UV_CACHE_DIR=/tmp/pact-uv-cache uv run python pact.py withdraw
UV_CACHE_DIR=/tmp/pact-uv-cache uv run python pact.py plan
```

For the interactive walkthrough, start [Ollama](https://ollama.com/) with a locally available `qwen3:8b` model in one terminal, then run the service in another:

```sh
ollama serve
UV_CACHE_DIR=/tmp/pact-uv-cache uv run uvicorn app:app --host 127.0.0.1 --port 8765
```

Open `http://127.0.0.1:8765`. The graph and schedule work without Ollama; the agent review button needs the model. `PACT_MODEL` and `OLLAMA_URL` can override the local defaults. This demonstration is bound to localhost and has no login. Do not expose it publicly as a writable service.

The demo graph is named `pact_demo`; `seed` replaces only that disposable graph. `withdraw` simulates W's withdrawal at 10:00, keeps wipe records for L01–L10, and activates W2 for the remaining ten devices. Repeating `withdraw` is idempotent. Run `seed` to restore the original case. FalkorDB listens at `127.0.0.1:6389` to avoid a common local Redis port conflict. Its browser listens at `127.0.0.1:3009`. Docker Compose keeps a named volume for persistence. Queries fail if the database is unavailable.

## Graph model and central query

- `Goal` requires `Requirement` nodes with explicit quantities.
- An `Organization` makes an `Offer` with an explicit quantity.
- An active `Offer` may satisfy a `Requirement` when its quantity covers the remaining work.
- `Device → WipeRecord` preserves simulated completed work across a withdrawal and database restart.
- `Episode → Organization → Offer` lets the agent retrieve a prior capacity failure and compare its old rate with the current offer. A separate episode records the simulated withdrawal and its completed device records.

```cypher
MATCH (goal:Goal {id:$goal})-[:REQUIRES]->(r:Requirement)
      <-[:SATISFIES]-(offer:Offer)<-[:MAKES]-(org:Organization)
WHERE coalesce(offer.active,true) = true
RETURN r.id, r.quantity, org.id, org.name, offer.id, offer.quantity
ORDER BY r.id, org.id
```

Candidate coverage checks an offer's quantity against the required quantity after subtracting completed `Device → WipeRecord` paths. It does not trust a separate mutable completion counter.

FalkorDB is the only store for this state. Removing it makes discovery and scheduling fail. The checker verifies quantities, each step's duration and time window, task order, room use, and delivery deadline. The current solver models a single van trip, the fixed wipe → transfer → prepare → deliver path, and a fixed Day 2 clinic/introduction. It does not search arbitrary partner sets or split batches. Later gates add revision-bound approvals, broader recovery, and measured conditional memory. Do not treat this slice as a complete submission.

## Phase gates

| Gate | Current evidence | Next test |
| --- | --- | --- |
| 1 — Graph foundation | Live query found four organizations; query survived container restart; unavailable endpoint returned an error | Preserve local reproducibility |
| 2 — Feasible schedule | 20-device witness delivered by 14:00; 18-device and 13:30-deadline variants blocked; tampered witness rejected | Expand beyond the fixed one-trip workflow |
| 3 — Recovery and shared memory | Ten simulated wipe records survived withdrawal, replay, and restart; W2 schedule delivered by 14:30. An old W2 failure at 5/hour was rejected as obsolete when the current offer said 10/hour. | Add revision-safe approvals and compare no-history, text-memory, and conditional graph-memory on matched scenarios |
| 4 — Product and submission | Local browser flow works for reset, withdrawal, schedule, retained records, and read-only agent review | Broader browser checks, source evidence, demo video, public repo, disclosure, human explanation |

## Interpretation

The current graph stores declared contributions, not proof of ownership or data-wiping certification. A `feasible_within_model` result is a proposed schedule under the synthetic assumptions. It does not reserve a device, collect anyone's approval, or record physical work. OR-Tools provides the constraint search; FalkorDB provides the only current collaboration state and the path from goal to offers. The local model chooses from three allowlisted, read-only tools; deterministic checks set the final recommendation and whether the old memory applies. No arbitrary Cypher or mutation tool is exposed to the model. The outcome of the controlled memory experiment is still unknown.

## Build provenance

Main code began October 16, 2026 IST, within the organizer's [October 15–18 build window](https://www.wemakedevs.org/hackathons/falkordb/schedule). Pre-event PACT notes and synthetic scenario sketches existed; implementation started during the event. Codex assisted with the implementation; Divyansh must review and be able to explain the source, model, queries, evaluation, and demo before submission.
