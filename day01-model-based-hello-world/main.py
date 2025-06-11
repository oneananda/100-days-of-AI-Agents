import json
import os

DATA_FILE = "memory.json"

def load_memory():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_memory(memory):
    with open(DATA_FILE, "w") as f:
        json.dump(memory, f)

def reflex_greeting():
    memory = load_memory()
    name = input("👋 What's your name? ").strip()

    if name in memory:
        print(f"Hello again, {name}! Welcome back.")
    else:
        print(f"Nice to meet you, {name}!")
        memory[name] = {"visits": 1}
        save_memory(memory)

if __name__ == "__main__":
    reflex_greeting()
