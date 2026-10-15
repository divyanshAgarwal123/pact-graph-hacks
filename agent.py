"""A read-only, bounded local agent over PACT's fixed graph tools."""

import json
import os
from urllib.request import Request, urlopen

from pact import GOAL_ID, candidates, memories, scenario
from planner import plan


MODEL = os.getenv("PACT_MODEL", "qwen3:8b")
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://127.0.0.1:11434/api/chat")
TOOL_NAMES = ("inspect_connections", "check_schedule", "recall_failure")
TOOLS = [{"type": "function", "function": {
    "name": name, "description": description,
    "parameters": {"type": "object", "properties": {}, "required": []}}}
    for name, description in (
        ("inspect_connections", "Read the current goal, requirements, active offers, and their organizations from FalkorDB"),
        ("check_schedule", "Solve and independently check the current synthetic schedule"),
        ("recall_failure", "Read a prior provider failure from FalkorDB and check if it applies to the current offer"),
    )]


def _chat(messages, tools=None, format_schema=None):
    payload = {"model": MODEL, "messages": messages, "stream": False, "think": False,
               "options": {"temperature": 0, "num_predict": 256}}
    if tools is not None:
        payload["tools"] = tools
    if format_schema is not None:
        payload["format"] = format_schema
    request = Request(OLLAMA_URL, data=json.dumps(payload).encode(),
                      headers={"Content-Type": "application/json"})
    with urlopen(request, timeout=45) as response:
        return json.load(response)["message"]


def review(g):
    """Run at most three tool-choice rounds; validate the model's conclusion."""
    messages = [
        {"role": "system", "content": (
            "You are PACT's read-only coordinator for a synthetic scenario. "
            "Call inspect_connections, check_schedule, and recall_failure before concluding. "
            "Use only those tool results. A past failure at a different rate may be obsolete. "
            "Never claim a proposal is approved, reserved, or physically completed. "
            "You can call more than one tool in a turn.")},
        {"role": "user", "content": (
            "Can the school receive 20 prepared laptops by 15:00? "
            "Should W2's earlier capacity failure block its current offer?")},
    ]
    executed = {}
    trace = []
    for _ in range(3):
        if len(executed) == len(TOOL_NAMES):
            break
        answer = _chat(messages, tools=TOOLS)
        calls = answer.get("tool_calls", [])
        if not calls:
            break
        messages.append(answer)
        for call in calls:
            name = call.get("function", {}).get("name")
            if name not in TOOL_NAMES:
                return {"status": "unresolved", "reason": "Model requested an unsupported tool", "trace": trace}
            if name == "inspect_connections":
                result = candidates(g)
            elif name == "check_schedule":
                result = plan(scenario(g))
            else:
                result = memories(g)
            executed[name] = result
            trace.append(name)
            messages.append({"role": "tool", "tool_name": name,
                             "content": json.dumps(result)})
    if set(executed) != set(TOOL_NAMES):
        return {"status": "unresolved", "reason": "Required graph tools were not called", "trace": trace}

    schema = {"type": "object", "properties": {
        "why": {"type": "string"},
        "evidence_ids": {"type": "array", "items": {"type": "string"}},
    }, "required": ["why", "evidence_ids"]}
    messages.append({"role": "user", "content": (
        "Return one JSON note about the checked proposal and the old W2 episode. "
        "Keep why under 35 words. Cite offer IDs or episode IDs. "
        "Describe a synthetic proposal, never an approval or completed delivery.")})
    draft = json.loads(_chat(messages, format_schema=schema)["content"])
    checked = executed["check_schedule"]
    history = executed["recall_failure"]
    expected_recommendation = ("present_plan" if checked["status"] == "feasible_within_model"
                               else "unresolved" if checked["status"] == "unresolved"
                               else "seek_new_offer")
    expected_memory = ("applicable" if history and history[0]["applicable_now"] else
                       "obsolete" if history else "none")
    valid_ids = {GOAL_ID}
    valid_ids.update(row["offer_id"] for row in executed["inspect_connections"]["candidate_offers"])
    valid_ids.update(row["episode_id"] for row in history)
    if (not draft["evidence_ids"] or not set(draft["evidence_ids"]).issubset(valid_ids)
            or len(draft["why"]) > 240):
        return {"status": "unresolved", "reason": "Model cited unknown evidence or exceeded the review limit",
                "trace": trace, "checked_plan": checked["status"]}
    if checked["status"] == "feasible_within_model" and expected_memory == "obsolete":
        explanation = "The current W2 rate supersedes its old 5/hour failure; the checked proposal meets the deadline."
    elif checked["status"] == "blocked" and expected_memory == "applicable":
        explanation = "W2's current rate matches its earlier failed rate, and the schedule checker found no feasible continuation."
    else:
        explanation = "Recommendation follows the current graph facts and the independent schedule check."
    return {"status": "reviewed", "recommendation": expected_recommendation,
            "memory_assessment": expected_memory, "explanation": explanation,
            "evidence_ids": draft["evidence_ids"], "trace": trace,
            "checked_plan": checked["status"], "model": MODEL,
            "disclaimer": "Read-only model review of a synthetic proposal; no approval or external action"}
