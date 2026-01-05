# llm.py — Ollama backend (local, free)
import requests
from policy import choose_followup, style_instruction

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL_NAME = "llama3.1:8b"

def _build_messages(mem: dict, history: list, user_text: str):
    """
    history: list of dicts [{"role":"user"/"assistant","content":...}, ...]
    """
    style = style_instruction(mem)
    followup = choose_followup(mem, user_text)

    system = (
        f"You are {mem.get('agent_name','Mira')}, a warm, curious friend. "
        f"Style: {style}. "
        "Be specific, reflect the user's details, avoid generic coaching clichés. "
        "Ask at most ONE short question at the end, only if it helps. "
        f"Suggested follow-up question (use only if natural): {followup}"
    )

    messages = [{"role": "system", "content": system}]
    # keep last ~10 turns to stay coherent
    messages += history[-10:]
    messages.append({"role": "user", "content": user_text})
    return messages

def generate_reply(mem: dict, history: list, user_text: str):
    """
    Returns: (assistant_text, updated_history)
    """
    messages = _build_messages(mem, history, user_text)

    payload = {
        "model": MODEL_NAME,
        "messages": messages,
        "stream": False,
        "options": {
            "temperature": 0.7,
            "top_p": 0.9,
        },
    }

    r = requests.post(OLLAMA_URL, json=payload, timeout=120)
    r.raise_for_status()
    data = r.json()
    assistant_text = data["message"]["content"].strip()

    # update history
    history.append({"role": "user", "content": user_text})
    history.append({"role": "assistant", "content": assistant_text})

    return assistant_text, history