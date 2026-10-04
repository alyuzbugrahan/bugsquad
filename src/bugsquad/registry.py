import inspect
import json
from pathlib import Path

from bugsquad import tools
from bugsquad.tools import MAX_READ_LINES

TOOL_FUNCTIONS = {
    "list_files": tools.list_files,
    "read_file": tools.read_file,
    "edit_file": tools.edit_file,
    "run_tests": tools.run_tests,
}

TOOL_SCHEMAS = [
    {
        "type": "function",
        "function": {
            "name": "list_files",
            "description": "List every file in the project. Call this first to see what exists.",
            "parameters": {"type": "object", "properties": {}},
        },
    },
    {
        "type": "function",
        "function": {
            "name": "read_file",
            "description": (
                "Read a text file. Small files are returned in full. Long files are returned "
                f"{MAX_READ_LINES} lines at a time; use start_line and end_line to read a specific part."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {"type": "string", "description": "File path relative to the project root."},
                    "start_line": {"type": "integer", "description": "First line to read (1-based). Default 1."},
                    "end_line": {"type": "integer", "description": "Last line to read (inclusive). Optional."},
                },
                "required": ["path"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "edit_file",
            "description": (
                "Replace an exact snippet in a source file. Read the file first and copy old_text "
                "exactly, including indentation. old_text must appear exactly once. "
                "Test files (test_*.py) are read-only."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {"type": "string", "description": "File path relative to the project root."},
                    "old_text": {"type": "string", "description": "Exact text to replace."},
                    "new_text": {"type": "string", "description": "Replacement text."},
                },
                "required": ["path", "old_text", "new_text"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "run_tests",
            "description": "Run the project's test suite and return the result. Use it to verify a fix.",
            "parameters": {"type": "object", "properties": {}},
        },
    },
]


def execute_tool(workspace: Path, name: str, arguments: str) -> str:
    """Run the tool the model asked for and always return a string for the model to read."""
    func = TOOL_FUNCTIONS.get(name)
    if func is None:
        return f"ERROR: Unknown tool '{name}'. Available tools: {', '.join(TOOL_FUNCTIONS)}."

    try:
        args = json.loads(arguments or "{}")
    except json.JSONDecodeError:
        return f"ERROR: Arguments for '{name}' are not valid JSON."
    if not isinstance(args, dict):
        return f"ERROR: Arguments for '{name}' must be a JSON object."

    try:
        inspect.signature(func).bind(workspace, **args)
    except TypeError as e:
        return f"ERROR: Wrong arguments for '{name}': {e}"

    return func(workspace, **args)