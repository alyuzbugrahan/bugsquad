from pathlib import Path

MAX_FILE_CHARS = 20_000


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