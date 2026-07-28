"""CLI for agentic-rag-eval."""

import sys, json, argparse
from .loader import load_trajectories
from .pipeline import run_eval, default_metrics

def main(argv=None):
    if hasattr(sys.stdout, "reconfigure"): sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(prog="agentic-rag-eval", description="Agentic RAG evaluation")
    sub = parser.add_subparsers(dest="command")
    p = sub.add_parser("eval", help="Evaluate trajectories")
    p.add_argument("file", help="JSON file with trajectories"); p.add_argument("--json", action="store_true")
    p2 = sub.add_parser("metrics", help="List available metrics")
    args = parser.parse_args(argv)
    if args.command == "metrics":
        print("\n".join(m.name for m in default_metrics()))
    elif args.command == "eval":
        trajs = load_trajectories(args.file)
        report = run_eval(trajs, default_metrics())
        if args.json: print(json.dumps(report.to_dict(), ensure_ascii=False, indent=2))
        else: print(f"Evaluated {len(trajs)} trajectories\nOverall mean: {report.overall_mean:.4f}\nMetrics: {len(report.per_metric)} scores")
    else: parser.print_help()

if __name__ == "__main__": main()
