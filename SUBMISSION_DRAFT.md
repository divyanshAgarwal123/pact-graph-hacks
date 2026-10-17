# PACT — submission packet

Checked against the live organizer form on 17 October 2026 IST. Seven of eight required answers are staged in the browser. The remaining required answer is a **public or unlisted YouTube video URL**. Pages playback is verified, but it does not replace this form requirement. No final submission has occurred.

## Verified project links

- Source and complete local setup: https://github.com/divyanshAgarwal123/pact-graph-hacks
- Public working-video player: https://divyanshagarwal123.github.io/pact-graph-hacks/
- Direct MP4: https://divyanshagarwal123.github.io/pact-graph-hacks/PACT-demo.mp4
- Graph model and queries: https://github.com/divyanshAgarwal123/pact-graph-hacks/blob/main/CYPHER.md
- Verification: https://github.com/divyanshAgarwal123/pact-graph-hacks/blob/main/VERIFICATION.md
- Passing fix checks: https://github.com/divyanshAgarwal123/pact-graph-hacks/actions/runs/39029201162

## Project title

PACT — graph-grounded coalition recovery

40 characters; the form permits 120.

## Description

PACT helps campus and nonprofit coordinators recover projects that depend on contributions from several organizations. In our synthetic school-laptop example, a wiping provider withdraws after ten devices are finished. PACT preserves those records, compares connected backup offers, explains why an alternative misses the deadline, and finds a checked continuation when one exists.

Changing a backup's capacity or availability changes the graph-grounded decision. A local model selects three read-only MCP inspections and may request a revision-bound pending proposal for human review. Current facts and an independent schedule checker guard that action.

This is one bounded synthetic workflow; a proposal is not an approval, reservation or real delivery. Codex assisted with implementation, verification, documentation and demo production. The edited browser demo uses computer narration and shortens model waiting time.

## Track

Agents That Act on Connected Data (Track 01). Other tracks are unselected.

## Repository

https://github.com/divyanshAgarwal123/pact-graph-hacks

## Demo video

**Pending:** upload the reviewed `docs/PACT-demo.mp4` to the existing YouTube channel as **Unlisted**, then verify playback and insert its actual watch URL. The file is 2:47 with visible captions and disclosed computer narration. Title, description, chapters and supporting links are prepared locally in `outputs/youtube-upload-metadata.json`.

The YouTube upload screen explicitly requires acknowledgment of its [Terms of Service](https://www.youtube.com/t/terms) and [Community Guidelines](https://www.youtube.com/yt/about/policies/). No file has been selected or uploaded; obtain the required agreement confirmation before that step.

## Live demo or deployment — optional

Leave blank. The Pages site hosts the video; it is not a live deployment of the writable PACT app. Complete local Docker/Python setup is in README, as permitted by the rules.

## How did you use FalkorDB in your project?

FalkorDB is the only store for PACT's current collaboration state. The goal-to-requirement-to-offer-to-organization traversal discovers active partners. Offer terms supply quantities, processing rates and availability to a bounded CP-SAT planner and independent schedule checker; there is no storage fallback when the graph is unavailable.

Device-to-wipe-record paths preserve ten simulated completed wipes after withdrawal, so recovery schedules only unfinished work. An episode-to-organization-to-offer traversal checks whether a historical capacity failure still applies. Revision-linked change events retain before-and-after terms and explain a partner switch.

The local model chooses read-only graph tools through MCP. A separate guarded Cypher write records only a checked pending proposal, atomically matching both the case identity and revision. A fresh identity on reset prevents an old proposal from being accepted when numeric revisions repeat. The integration suite checks stale writes, reset races, replay integrity, blocked constraints and concurrent snapshots. Restart persistence was also verified locally.

## Blog link — optional

Leave blank. No blog submission is claimed.

## What did you like about FalkorDB? — draft for participant review

The connected model lets us follow a goal to requirements, active offers and their organizations, while keeping completed work, historical episodes, change events and pending proposals in the same graph. Parameterized Cypher makes those evidence paths inspectable. The Python client and Docker setup also let us exercise the same graph operations in the local app and a clean CI environment.

## What improvements would you like to see in FalkorDB? — draft for participant review

An end-to-end example combining revision-checked writes, idempotent recovery, MCP read tools, and concurrency/restart tests would be valuable for agent builders. A companion walkthrough showing how to visualize before-and-after evidence paths would help explain why an agent changed its decision. These are suggested learning resources, not claims of a defect in FalkorDB.

## Final gates

1. Confirm the YouTube upload acknowledgment, upload as Unlisted, and verify accessible playback. Insert the resulting YouTube URL; do not invent one or substitute the Pages URL.
2. Divyansh reviews the video and staged answers, including the two feedback drafts, and can explain the graph, solver/checker, MCP tools and case/revision guard. Use `JUDGE_QA.md`.
3. Inspect all eight required fields and the track selection, then obtain final submission authorization. The current request prepares the entry; it does not submit it.
4. Submit before 18 October 2026, 11:59 PM IST and inspect the organizer's success page or confirmation as the receipt.
