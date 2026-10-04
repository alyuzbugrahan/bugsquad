import shutil
import tempfile
from pathlib import Path

HIDDEN_DIR = "hidden"
_IGNORED = shutil.ignore_patterns("__pycache__", ".pytest_cache", HIDDEN_DIR)


def prepare_workspace(project: Path) -> Path:
    """Copy the project into a fresh temp folder, leaving out hidden tests, and return its path."""
    root = Path(tempfile.mkdtemp(prefix="bugsquad_"))
    workspace = root / project.name
    shutil.copytree(project, workspace, ignore=_IGNORED)
    if (workspace / HIDDEN_DIR).exists():
        raise RuntimeError("Hidden tests leaked into the agent workspace.")
    return workspace


def cleanup(workspace: Path) -> None:
    """Delete the temp folder that holds the workspace."""
    shutil.rmtree(workspace.parent, ignore_errors=True)