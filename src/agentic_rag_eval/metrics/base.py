"""Base metric protocol."""

from typing import Protocol
from ..types import AgenticTrajectory, MetricResult

class Metric(Protocol):
    name: str
    def evaluate(self, traj: AgenticTrajectory) -> MetricResult: ...
    def __call__(self, traj: AgenticTrajectory) -> MetricResult: ...

def eval_trajectory(traj: AgenticTrajectory, metrics: list[Metric]) -> list[MetricResult]:
    return [m(traj) for m in metrics]

def eval_set(trajectories: list[AgenticTrajectory], metrics: list[Metric]) -> list[list[MetricResult]]:
    return [eval_trajectory(t, metrics) for t in trajectories]

def mean_score(results: list[list[MetricResult]], metric_name: str) -> float:
    scores = [r.score for batch in results for r in batch if r.metric == metric_name]
    return sum(scores) / len(scores) if scores else 0.0
