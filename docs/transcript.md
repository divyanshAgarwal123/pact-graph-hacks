# PACT browser demo transcript

Edited live browser capture of the synthetic PACT app, recorded 17 October 2026. Model waiting time is shortened. Computer narration uses the installed macOS Samantha voice. No app result is simulated in the edit. Source implementation: 95050e89ae04ae2c7967f4a6ebd868f41de2b762.

## 00:00:00.000 — The deadline

PACT helps a coordinator recover a shared project when one partner withdraws. In this synthetic example, a school needs twenty prepared laptops by three P M. No organization can finish the project alone. We start with the original checked plan, which delivers at two P M.

## 00:00:17.230 — Connected offers

FalkorDB connects the school goal to requirements, offers, and the organizations behind them. These are live graph facts: quantities, availability, processing rates, and completed work. The planner checks connected partner combinations with a constraint solver, then independently checks the resulting schedule. The graph is the only source of current collaboration state.

## 00:00:40.560 — Recover unfinished work

Now the original wiping provider withdraws after ten devices are finished. PACT preserves those ten records and considers two backup offers for the rest. W two can finish in time, with delivery at two thirty. W three is also connected, but its later availability misses the deadline. The rejected alternative stays visible.

## 00:01:01.220 — A guarded agent action

The local coordinator agent calls three read-only tools through MCP: inspect connections, check schedule, and recall failure. An old W two failure at five devices an hour does not match its current rate of ten. After checking the evidence, the agent requests a pending proposal. This is human review, never an approval or reservation.

## 00:01:22.800 — Block an unsafe plan

Change W two back to its old rate. Both backup schedules now fail, and PACT blocks the proposal. The historical warning becomes applicable. The earlier saved proposal is marked stale because the graph revision changed. PACT keeps the ten completed records instead of pretending the project starts over.

## 00:01:41.830 — A different partner changes the answer

Move W three earlier while W two remains slow. PACT now finds a checked two P M continuation. The first-active-offer baseline still blocks. Both policies use the same current facts and schedule checker. This is a bounded synthetic comparison, not a general performance claim.

## 00:01:59.950 — Change the terms yourself

The custom form accepts actual offer terms, not just named presets. Set W two to seven devices per hour and W three to ten fifteen. These values are written to FalkorDB. The same planner selects W three for two fifteen. The change ledger records which offer terms changed and the previous proposal remains stale.

## 00:02:20.650 — Evidence and limits

The public source includes the graph model, executed Cypher, setup instructions, and verification suite. The reset fix checks a unique case identity as well as its revision, rejecting old proposals even when revision numbers repeat. PACT is one synthetic workflow with checked pending proposals. Codex coding assistance and this computer narration are disclosed. The entry targets Agents That Act on Connected Data.
