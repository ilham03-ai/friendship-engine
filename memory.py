# memory.py
import json
from pathlib import Path

MEMORY_PATH = Path("memory.json")

DEFAULT_MEMORY = {
    "facts": {
        "name": None,
        "style": None,   # "hype", "calm", "coach"
    },
    "notes": [],
}

def load_memory() -> dict:
    if MEMORY_PATH.exists():
        try:
            data = json.loads(MEMORY_PATH.read_text(encoding="utf-8"))

            # ✅ Migrazione: se il vecchio file non ha la struttura attesa
            if not isinstance(data, dict):
                return DEFAULT_MEMORY.copy()

            data.setdefault("facts", {})
            data.setdefault("notes", [])

            # assicurati che facts contenga le chiavi base
            data["facts"].setdefault("name", None)
            data["facts"].setdefault("style", None)

            return data

        except Exception:
            return DEFAULT_MEMORY.copy()

    return DEFAULT_MEMORY.copy()

def save_memory(mem: dict) -> None:
    MEMORY_PATH.write_text(json.dumps(mem, indent=2, ensure_ascii=False), encoding="utf-8")

def set_fact(mem: dict, key: str, value):
    mem.setdefault("facts", {})
    mem["facts"][key] = value

def add_note(mem: dict, text: str) -> None:
    mem.setdefault("notes", [])
    mem["notes"].append(text)