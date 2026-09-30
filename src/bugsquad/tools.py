from pathlib import Path

MAX_FILE_CHARS = 20_000
IGNORED_DIRS = {".git", ".venv", "__pycache__", ".pytest_cache", "node_modules"}
MAX_LIST_ENTRIES = 200

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