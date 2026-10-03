import os
from dataclasses import dataclass
from pathlib import Path

from bugsquad.llm import chat_with_tools
from bugsquad.registry import TOOL_SCHEMAS, execute_tool

MAX_STEPS = 15
INPUT_PRICE_PER_M = float(os.getenv("LLM_INPUT_PRICE_PER_M", "0"))
OUTPUT_PRICE_PER_M = float(os.getenv("LLM_OUTPUT_PRICE_PER_M", "0"))


@dataclass
class AgentResult:
    answer: str
    finished: bool
    steps: int = 0
    input_tokens: int = 0
    output_tokens: int = 0

    @property
    def cost_usd(self) -> float:
        return (self.input_tokens * INPUT_PRICE_PER_M + self.output_tokens * OUTPUT_PRICE_PER_M) / 1_000_000

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


def run_agent(workspace: Path, task: str, max_steps: int = MAX_STEPS) -> AgentResult:
    """Let the model use tools in a loop until it gives a final answer or hits the step limit."""
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": task},
    ]
    result = AgentResult(answer="", finished=False)

    for step in range(1, max_steps + 1):
        response = chat_with_tools(messages, TOOL_SCHEMAS)
        msg = response.choices[0].message
        result.steps = step
        if response.usage:
            result.input_tokens += response.usage.prompt_tokens
            result.output_tokens += response.usage.total_tokens - response.usage.prompt_tokens

        messages.append(msg.model_dump(exclude_none=True))

        if msg.tool_calls:
            for tool_call in msg.tool_calls:
                name = tool_call.function.name
                output = execute_tool(workspace, name, tool_call.function.arguments)
                print(f"[step {step}] {name}({tool_call.function.arguments}) -> {output[:70]!r}")
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "name": name,
                    "content": output,
                })
            continue

        result.answer = msg.content or ""
        result.finished = True
        return result

    result.answer = f"Reached the limit of {max_steps} steps without a final answer."
    return result