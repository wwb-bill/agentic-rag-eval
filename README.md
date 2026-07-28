# agentic-rag-eval

Evaluation framework for agentic RAG — 12 metrics covering retrieval decisions, tool use, iteration quality, answer faithfulness, and cost. **5th M project, v1.0.0, 74 tests.**

Migrated from alvabillwu (account suspended). Zero dependencies, pure Python. Deterministic, no LLM judge required.

## Modules

- `metrics/retrieval.py` — RetrievalDecisionMetric, Precision, Recall, Count
- `metrics/tool_use.py` — ToolSelectionMetric, ToolArgValidity, ToolArgCorrectness
- `metrics/iteration.py` — LoopCountMetric, ConvergenceMetric
- `metrics/answer.py` — AnswerFaithfulnessMetric, AnswerRelevanceMetric
- `metrics/cost.py` — CostMetric (token budget adherence)
- `pipeline.py` — run_eval() pipeline with 12-metric default suite
- `loader.py` — Load trajectories from JSON
- `cli.py` — CLI with eval, metrics, --json

## License

MIT — migrated from https://github.com/alvabillwu/agentic-rag-eval
