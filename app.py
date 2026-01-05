# app.py
from configs import AGENT_NAME
from memory import load_memory, save_memory
from llm import generate_reply

def main():
    mem = load_memory()
    mem.setdefault("agent_name", AGENT_NAME)
    mem.setdefault("facts", {})
    mem.setdefault("prefs", {})
    mem.setdefault("state", {})

    history = []

    print(f"{AGENT_NAME} (prototype). Type 'exit' to stop.\n")

    # onboarding light
    if not mem["facts"].get("name"):
        print(f"{AGENT_NAME}: Hey :) What should I call you?")
        name = input("You: ").strip()
        mem["facts"]["name"] = name
        save_memory(mem)
        print(f"{AGENT_NAME}: Nice to meet you, {name}. What should I be for you: a calm listener, a hype buddy, or a structured coach?")
        mode = input("You: ").strip().lower()
        mem["prefs"]["mode"] = mode
        save_memory(mem)

    while True:
        user_text = input("\nYou: ").strip()
        if user_text.lower() in {"exit", "quit"}:
            print(f"{AGENT_NAME}: Okay. I’m here whenever you want to talk.")
            break

        assistant, history = generate_reply(mem, history, user_text)
        print(f"{AGENT_NAME}: {assistant}")

        # persist lightweight state if you want
        save_memory(mem)

if __name__ == "__main__":
    main()