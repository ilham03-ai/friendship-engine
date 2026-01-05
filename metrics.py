# metrics.py
import json
import time
import os
from configs import LOG_FILE, SURVEY_FILE

def log_event(role: str, text: str, meta: dict | None = None):
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    event = {"ts": time.time(), "role": role, "text": text, "meta": meta or {}}
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(event, ensure_ascii=False) + "\n")

def maybe_survey(turn_count: int) -> bool:
    from configs import SURVEY_EVERY_TURNS
    return turn_count > 0 and turn_count % SURVEY_EVERY_TURNS == 0

def save_survey(scores: dict):
    header = "ts,listen,interest,return\n"
    line = f"{time.time()},{scores['listen']},{scores['interest']},{scores['return']}\n"
    file_exists = os.path.exists(SURVEY_FILE)
    os.makedirs(os.path.dirname(SURVEY_FILE), exist_ok=True)
    with open(SURVEY_FILE, "a", encoding="utf-8") as f:
        if not file_exists:
            f.write(header)
        f.write(line)