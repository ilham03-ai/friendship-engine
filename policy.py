# policy.py
import random

STYLE_PROMPTS = {
    "hype": [
        "Keep it upbeat, energetic, and supportive. Use short punchy sentences.",
        "Be friendly and curious. Celebrate small wins. Avoid being cheesy.",
    ],
    "calm": [
        "Be calm, warm, and grounding. Ask gentle questions. Keep it simple.",
        "Use a reassuring tone. Reflect feelings briefly, then ask one small question.",
    ],
    "coach": [
        "Be structured and practical. Ask clarifying questions. Give next steps.",
        "Use an engineering coach vibe: concise, actionable, and specific.",
    ],
}

def choose_followup(mem: dict, user_text: str) -> str:
    """Choose one good follow-up question to keep conversation moving."""
    name = (mem.get("facts", {}) or {}).get("name")
    style = (mem.get("facts", {}) or {}).get("style") or "hype"

    # Basic intent heuristics (super simple but effective)
    t = user_text.lower().strip()

    if any(w in t for w in ["sad", "down", "anx", "stress", "tired", "cry"]):
        return random.choice([
            f"{name or 'Hey'}, what’s weighing on you the most right now?",
            "Want to tell me what triggered that feeling?",
            "If we could fix just one small piece tonight, what would it be?",
        ])

    if any(w in t for w in ["happy", "good", "great", "excited", "proud"]):
        return random.choice([
            "Nice. What made it good—what’s the key thing?",
            "What part of that do you want more of?",
            "What’s the next tiny step to keep the momentum?",
        ])

    if len(t) <= 3:
        return random.choice([
            "Hit me with one detail—what’s happening?",
            "Give me one sentence: what’s on your mind?",
            "Okay. What do you want out of this chat right now?",
        ])

    # Default: curious, not robotic
    if style == "coach":
        return random.choice([
            "What’s the goal here, and what’s the constraint?",
            "What have you tried so far, and what happened?",
            "What would a ‘good result’ look like for you?",
        ])

    if style == "calm":
        return random.choice([
            "Do you want to be heard, or do you want ideas?",
            "What’s the one thing you wish someone understood about this?",
            "What would feel like relief right now?",
        ])

    # hype
    return random.choice([
        "Okay—what matters most to you in this situation?",
        "What’s the part you care about most right now?",
        "What would make today a win, even a small one?",
    ])

def style_instruction(mem: dict) -> str:
    style = (mem.get("facts", {}) or {}).get("style") or "hype"
    return " ".join(STYLE_PROMPTS.get(style, STYLE_PROMPTS["hype"]))