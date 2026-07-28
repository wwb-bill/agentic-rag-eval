"""Load trajectories from JSON files."""

import json
from .types import AgenticTrajectory, AgenticStep

def load_trajectories(path: str) -> list[AgenticTrajectory]:
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    items = data if isinstance(data, list) else [data]
    return [trajectory_from_dict(d) for d in items]

def trajectory_from_dict(d: dict) -> AgenticTrajectory:
    steps = [AgenticStep(**s) for s in d.get("steps", [])]
    return AgenticTrajectory(
        query=d["query"], steps=steps, final_answer=d.get("final_answer", ""),
        ground_truth=d.get("ground_truth", {}), retrieved_docs=d.get("retrieved_docs", {}),
        cost_tokens=d.get("cost_tokens", {}),
    )
