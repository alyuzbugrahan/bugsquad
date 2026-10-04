import argparse
import difflib
import shutil
import sys
import tempfile
from pathlib import Path

from bugsquad.agent import run_agent
from bugsquad.tools import run_tests
from bugsquad.workspace import cleanup, prepare_workspace

TASK = "Fix the bug described in issue.md."


def _diff(original: Path, workspace: Path) -> str:
    """Return a unified diff of every .py file the agent changed."""
    chunks = []
    for changed in sorted(workspace.rglob("*.py")):
        relative = changed.relative_to(workspace)
        before = (original / relative).read_text(encoding="utf-8").splitlines(keepends=True)
        after = changed.read_text(encoding="utf-8").splitlines(keepends=True)
        chunks.extend(difflib.unified_diff(before, after, f"a/{relative}", f"b/{relative}"))
    return "".join(chunks)


def main() -> int:
    parser = argparse.ArgumentParser(prog="bugsquad", description="Let an AI agent fix the bug in a project.")
    parser.add_argument("project", type=Path, help="Folder containing issue.md, the code and its tests.")
    parser.add_argument("--keep", action="store_true", help="Keep the working copy and print its location.")
    args = parser.parse_args()

    if not (args.project / "issue.md").is_file():
        print(f"error: {args.project} has no issue.md", file=sys.stderr)
        return 2

    workspace = prepare_workspace(args.project)
    try:
        result = run_agent(workspace, TASK)
        verdict = run_tests(workspace).splitlines()[0]

        print("\n=== Changes ===")
        print(_diff(args.project, workspace) or "(no changes)")
        print("=== Agent summary ===")
        print(result.answer)
        print(f"\nIndependent check: {verdict}")
        print(f"finished={result.finished}  steps={result.steps}  "
              f"tokens={result.input_tokens}+{result.output_tokens}  cost=${result.cost_usd:.4f}")
    finally:
        if args.keep:
            print(f"\nWorking copy kept at: {workspace}")
        else:
            cleanup(workspace)

    return 0 if verdict.startswith("STATUS: PASSED") else 1