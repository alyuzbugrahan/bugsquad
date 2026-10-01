from pathlib import Path

from bugsquad.llm import chat_with_tools
from bugsquad.registry import TOOL_SCHEMAS, execute_tool

MAX_STEPS = 15

SYSTEM_PROMPT = """You are a debugging agent working on a small Python project.
Your job is to fix the bug described in the issue.

Workflow:
1. List the files and read the issue.
2. Read the relevant source code.
3. Run the tests to see how they fail.
4. Make the smallest possible fix with edit_file.
5. Run the tests again to verify the fix.

Rules:
- Never edit test files.
- Stop as soon as all tests pass.
- When you are done, reply with a short summary: the root cause and what you changed."""


def run_agent(workspace: Path, task: str, max_steps: int = MAX_STEPS) -> str:
    """Let the model use tools in a loop until it gives a final answer or hits the step limit."""
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": task},
    ]

    for step in range(1, max_steps + 1):
        msg = chat_with_tools(messages, TOOL_SCHEMAS)
        messages.append(msg.model_dump(exclude_none=True))

        if msg.tool_calls:
            for tool_call in msg.tool_calls:
                name = tool_call.function.name
                result = execute_tool(workspace, name, tool_call.function.arguments)
                print(f"[step {step}] {name}({tool_call.function.arguments}) -> {result[:70]!r}")
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "name": name,
                    "content": result,
                })
            continue

        return msg.content or ""

    return f"STOPPED: reached the limit of {max_steps} steps without a final answer."