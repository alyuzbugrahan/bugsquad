import subprocess
import sys
from pathlib import Path

MAX_FILE_CHARS = 20_000
IGNORED_DIRS = {".git", ".venv", "__pycache__", ".pytest_cache", "node_modules"}
MAX_LIST_ENTRIES = 200
TEST_TIMEOUT_SECONDS = 30
MAX_TEST_OUTPUT_CHARS = 8_000

def _resolve_inside(workspace: Path, path: str) -> Path:
    """Turn a relative path into an absolute one and make sure it stays inside the workspace."""
    root = workspace.resolve()
    target = (root / path).resolve()
    if not target.is_relative_to(root):
        raise ValueError(f"Path is outside the workspace: {path}")
    return target


def read_file(workspace: Path, path: str) -> str:
    """Return the contents of a text file inside the workspace."""
    try:
        target = _resolve_inside(workspace, path)
        text = target.read_text(encoding="utf-8")
    except FileNotFoundError:
        return f"ERROR: File not found: {path}"
    except (ValueError, UnicodeDecodeError, IsADirectoryError) as e:
        return f"ERROR: {e}"

    if len(text) > MAX_FILE_CHARS:
        return text[:MAX_FILE_CHARS] + f"\n... [truncated, {len(text)} chars total]"
    return text


def list_files(workspace: Path) -> str:
    """Return every file in the workspace as relative paths, one per line."""
    root = workspace.resolve()
    files = []

    for path in sorted(root.rglob("*")):
        relative  = path.relative_to(root)
        if any(part in IGNORED_DIRS for part in relative.parts):
            continue
        if path.is_file():
            files.append(relative.as_posix())



    if not files:
        return "(workspace is empty)"
    if len(files) > MAX_LIST_ENTRIES:
        shown = "\n".join(files[:MAX_LIST_ENTRIES])
        return shown + f"\n... [{len(files) - MAX_LIST_ENTRIES} more files not shown]"
    return "\n".join(files)


def run_tests(workspace: Path) -> str:
    """Run pytest inside the workspace and return the status plus the test output."""
    root = workspace.resolve()
    try:
        completed = subprocess.run(
            [sys.executable, "-m", "pytest", ".", "-q", "-p", "no:cacheprovider"],
            cwd=root,
            capture_output=True,
            text=True,
            timeout=TEST_TIMEOUT_SECONDS,
        )
    except subprocess.TimeoutExpired:
        return f"ERROR: Tests did not finish within {TEST_TIMEOUT_SECONDS} seconds (possible infinite loop)."

    output = completed.stdout + completed.stderr
    if len(output) > MAX_TEST_OUTPUT_CHARS:
        output = "...[earlier output truncated]\n" + output[-MAX_TEST_OUTPUT_CHARS:]
        
    status = "PASSED" if completed.returncode ==0 else "FAILED"
    return f"STATUS: {status} (exit code {completed.returncode})\n\n{output}"


def edit_file(workspace: Path, path: str, old_text: str, new_text: str) -> str:
    """Replace one exact occurrence of old_text with new_text in a file inside the workspace."""
    try:
        target = _resolve_inside(workspace, path)
        content = target.read_text(encoding="utf-8")
    except FileNotFoundError:
        return f"ERROR: File not found: {path}"
    except (ValueError, UnicodeDecodeError, IsADirectoryError) as e:
        return f"ERROR: {e}"

    if target.name.startswith("test_"):
        return "ERROR: Test files are read-only. Fix the source code instead."
    if not old_text:
        return "ERROR: old_text must not be empty."

    count = content.count(old_text)
    if count == 0:
        return "ERROR: old_text was not found. Read the file again and copy the exact text, including spaces."
    if count > 1:
        return f"ERROR: old_text appears {count} times. Include more surrounding lines so it matches exactly once."

    target.write_text(content.replace(old_text, new_text, 1), encoding="utf-8")
    return f"OK: Edited {path}."