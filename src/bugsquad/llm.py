import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

#Degisken yoksa hemen ve net bir mesajla hata veriyor. Basindaki _ bu fonkisoyn sadece bu dosyanin icerisinde kullanilir anlamina gelen bir python gelenegi.
def _get_required_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Missing environment variable: {name}. Chech your .env file")
    return value

client = OpenAI(
    api_key=_get_required_env("LLM_API_KEY"),
    base_url=_get_required_env("LLM_BASE_URL"),
    max_retries=5,
)
MODEL = _get_required_env("LLM_MODEL")

def chat(messages: list[dict]) -> str:
    """Send message to the model and return the text reply."""
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
    )
    return response.choices[0].message.content


def chat_with_tools(messages: list[dict], tools: list[dict]):
    """Send messages plus tool schemas; return the model's message (text and/or tool calls)."""
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        tools=tools,
        tool_choice="auto",
    )
    return response.choices[0].message