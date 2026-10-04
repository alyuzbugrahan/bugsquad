import subprocess
import sys
from pathlib import Path

MAX_FILE_CHARS = 20_000
IGNORED_DIRS = {".git", ".venv", "__pycache__", ".pytest_cache", "node_modules"}
MAX_LIST_ENTRIES = 200
TEST_TIMEOUT_SECONDS = 30
MAX_TEST_OUTPUT_CHARS = 8_000
MAX_READ_LINES = 300

def _resolve_inside(workspace: Path, path: str) -> Path:
    """Turn a relative path into an absolute one and make sure it stays inside the workspace."""
    root = workspace.resolve()
    target = (root / path).resolve()
    if not target.is_relative_to(root):
        raise ValueError(f"Path is outside the workspace: {path}")
    return target


def read_file(workspace: Path, path: str, start_line: int = 1, end_line: int | None = None) -> str:
    """Return a text file inside the workspace, or the 1-based inclusive line range start_line..end_line.

    At most MAX_READ_LINES lines are returned per call."""
    try:
        target = _resolve_inside(workspace, path)
        text = target.read_text(encoding="utf-8")
    except FileNotFoundError:
        return f"ERROR: File not found: {path}"
    except (ValueError, UnicodeDecodeError, IsADirectoryError) as e:
        return f"ERROR: {e}"

    lines = text.splitlines(keepends=True)
    total = len(lines)
    if total == 0:
        return text
    if not 1 <= start_line <= total:
        return f"ERROR: start_line must be between 1 and {total} for {path}."

    last = start_line + MAX_READ_LINES - 1
    if end_line is not None:
        if end_line < start_line:
            return "ERROR: end_line must be greater than or equal to start_line."
        last = min(last, end_line)
    last = min(last, total)

    chunk = "".join(lines[start_line - 1:last])
    if start_line == 1 and last == total:
        return chunk

    note = f"[Showing lines {start_line}-{last} of {total} in {path}."
    if last < total:
        note += f" Call read_file again with start_line={last + 1} to continue, or use search_code to jump to a name."
    return note + "]\n" + chunk


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