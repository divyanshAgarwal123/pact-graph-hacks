"""Local synthetic PACT walkthrough; no accounts or external actions."""

from pathlib import Path
from threading import Lock

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse

from pact import candidates, graph, memories, scenario, seed, simulate_withdrawal
from planner import plan
from agent import review


app = FastAPI(title="PACT synthetic demo")
_demo_lock = Lock()
_web = Path(__file__).parent / "web"


@app.get("/")
def home():
    return FileResponse(_web / "index.html")


@app.get("/app.css")
def css():
    return FileResponse(_web / "app.css", media_type="text/css")


@app.get("/app.js")
def javascript():
    return FileResponse(_web / "app.js", media_type="text/javascript")


@app.get("/api/state")
def state():
    try:
        g = graph()
        current = scenario(g)
        episodes = [row[0] for row in g.query(
            "MATCH (e:Episode {kind:'withdrawal'}) RETURN e.id").result_set]
        return {"candidate_graph": candidates(g), "scenario": current,
                "proposal": plan(current), "episodes": episodes,
                "memories": memories(g)}
    except Exception as error:
        raise HTTPException(503, f"FalkorDB demo unavailable: {error}") from error


@app.post("/api/reset")
def reset():
    with _demo_lock:
        try:
            seed(graph())
        except Exception as error:
            raise HTTPException(503, f"Could not reset synthetic graph: {error}") from error
    return state()


@app.post("/api/withdraw")
def withdraw():
    with _demo_lock:
        try:
            simulate_withdrawal(graph())
        except Exception as error:
            raise HTTPException(503, f"Could not simulate withdrawal: {error}") from error
    return state()


@app.post("/api/agent-review")
def agent_review():
    try:
        return review(graph())
    except Exception as error:
        raise HTTPException(503, f"Local agent unavailable: {error}") from error
