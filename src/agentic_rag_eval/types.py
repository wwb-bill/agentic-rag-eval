"""Core types for agentic RAG evaluation."""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any

@dataclass
class AgenticStep:
    type: str  # retrieval, tool_call, observation, reasoning, answer
    tool: str = ""
    tool_args: dict[str, Any] = field(default_factory=dict)
    retrieved_doc_ids: list[str] = field(default_factory=list)
    content: str = ""

@dataclass
class AgenticTrajectory:
    query: str
    steps: list[AgenticStep] = field(default_factory=list)
    final_answer: str = ""
    ground_truth: dict[str, Any] = field(default_factory=dict)
    retrieved_docs: dict[str, str] = field(default_factory=dict)
    cost_tokens: dict[str, int] = field(default_factory=dict)

    def retrieval_steps(self): return [s for s in self.steps if s.type == "retrieval"]
    def tool_steps(self): return [s for s in self.steps if s.type == "tool_call"]
    def called_tools(self): return list(set(s.tool for s in self.tool_steps()))

@dataclass
class MetricResult:
    metric: str
    score: float
    details: dict[str, Any] = field(default_factory=dict)
    passed: bool = True

    def to_dict(self):
        return {"metric": self.metric, "score": round(self.score, 4), "details": self.details, "passed": self.passed}
