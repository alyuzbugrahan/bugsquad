import argparse
import json
import shutil
from datetime import datetime
from pathlib import Path

from bugsquad.agent import run_agent
from bugsquad.llm import MODEL
from bugsquad.tools import run_tests
from bugsquad.workspace import HIDDEN_DIR, cleanup, prepare_workspace

TASK = "Fix the bug described in issue.md."
DIFFICULTIES = ["easy", "medium", "hard"]


def grade(project: Path, workspace: Path) -> bool:
    """Restore the original visible tests, add the hidden tests, and return True if all of them pass."""
    for test_file in project.glob("test_*.py"):
        shutil.copy(test_file, workspace / test_file.name)
    for test_file in (project / HIDDEN_DIR).glob("test_*.py"):
        shutil.copy(test_file, workspace / test_file.name)
    return run_tests(workspace).startswith("STATUS: PASSED")


def evaluate_case(name: str, difficulty: str, project: Path, run: int) -> dict:
    """Run the agent once on one benchmark and return a record of what happened."""
    record = {
        "case": name, "difficulty": difficulty, "run": run,
        "solved": False, "finished": False, "steps": 0,
        "input_tokens": 0, "output_tokens": 0, "cost_usd": 0.0, "error": None,
    }
    workspace = prepare_workspace(project)
    if not (workspace / "issue.md").is_file():
        cleanup(workspace)
        record["error"] = "Invalid benchmark: issue.md is missing"
        return record
    try:
        result = run_agent(workspace, TASK)
        record.update(
            solved=grade(project, workspace),
            finished=result.finished,
            steps=result.steps,
            input_tokens=result.input_tokens,
            output_tokens=result.output_tokens,
            cost_usd=result.cost_usd,
        )
    except Exception as e:
        record["error"] = f"{type(e).__name__}: {e}"
    finally:
        cleanup(workspace)
    return record


def print_summary(records: list[dict]) -> None:
    print(f"\n{'Difficulty':<12}{'Solved':>10}{'Avg steps':>12}{'Avg cost':>12}")
    for group in DIFFICULTIES + ["TOTAL"]:
        rows = records if group == "TOTAL" else [r for r in records if r["difficulty"] == group]
        if not rows:
            continue
        solved = sum(r["solved"] for r in rows)
        avg_steps = sum(r["steps"] for r in rows) / len(rows)
        avg_cost = sum(r["cost_usd"] for r in rows) / len(rows)
        print(f"{group:<12}{f'{solved}/{len(rows)}':>10}{avg_steps:>12.1f}{f'${avg_cost:.4f}':>12}")

    failed = sorted({r["case"] for r in records if not r["solved"]})
    if failed:
        print("\nNot solved in every run:", ", ".join(failed))
    errors = [r for r in records if r["error"]]
    if errors:
        print(f"Runs that crashed: {len(errors)} (see the JSON file for details)")


def main() -> int:
    parser = argparse.ArgumentParser(prog="bugsquad-eval", description="Run the agent on the benchmarks and measure how many bugs it really fixes.")
    parser.add_argument("--benchmarks", type=Path, default=Path("benchmarks"), help="Folder with manifest.json and the cases.")
    parser.add_argument("--runs", type=int, default=3, help="How many times to run each case.")
    parser.add_argument("--only", nargs="*", help="Only run cases whose name starts with these prefixes, e.g. --only 002 010")
    args = parser.parse_args()

    manifest = json.loads((args.benchmarks / "manifest.json").read_text(encoding="utf-8"))
    names = [n for n in manifest if not args.only or n.startswith(tuple(args.only))]

    records = []
    for name in names:
        for run in range(1, args.runs + 1):
            print(f"\n=== {name}  (run {run}/{args.runs}) ===")
            record = evaluate_case(name, manifest[name]["difficulty"], args.benchmarks / name, run)
            status = "SOLVED" if record["solved"] else "not solved"
            print(f"--> {status}  steps={record['steps']}  cost=${record['cost_usd']:.4f}")
            records.append(record)

    print_summary(records)

    out_dir = Path("runs")
    out_dir.mkdir(exist_ok=True)
    out_file = out_dir / f"eval_{datetime.now():%Y%m%d_%H%M%S}.json"
    out_file.write_text(json.dumps({"model": MODEL, "runs_per_case": args.runs, "records": records}, indent=2), encoding="utf-8")
    print(f"\nSaved results to {out_file}")
    return 0