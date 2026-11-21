import os
from openai import OpenAI

# Standardmäßig auf lokales vLLM (Port 8000) oder Ollama (Port 11434/v1) konfigurierbar
BASE_URL = os.getenv("LLM_BASE_URL", "http://localhost:8000/v1")
API_KEY = os.getenv("LLM_API_KEY", "not-needed")
MODEL_NAME = os.getenv("LLM_MODEL", "local-llm")

client = OpenAI(base_url=BASE_URL, api_key=API_KEY)


def ask_local_llm(system_prompt: str, user_prompt: str) -> str:
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.2,
    )
    return response.choices[0].message.content or ""


if __name__ == "__main__":
    reply = ask_local_llm(
        system_prompt="Du bist ein präziser KI-Systemarchitekt.",
        user_prompt="Nenne drei Vorteile lokaler Open-Weights-Modelle im Mittelstand.",
    )
    print(reply)
