# Day 01 – Model-Based Greeting Agent 🤖🧠

Welcome to Day 01 of my **100 Days of AI Agents** challenge!

This project implements a **model-based reflex agent** — an upgraded version of a simple greeting agent that remembers past interactions. It’s a personalized twist on the classic "Hello, World!" that stores user names and adapts its greeting accordingly.

---

## 🔍 What It Does

- Prompts the user for their name.
- Responds differently depending on whether the name has been seen before.
- Saves interaction history to a local `memory.json` file.

---

## 🧠 Agent Type

- **Type:** Model-Based Reflex Agent  
- **Core Mechanism:** Condition–action rules + internal state (memory)

---

## 💬 Example Interaction

```text
👋 What's your name?
Alice
Nice to meet you, Alice!

# On another run:
👋 What's your name?
Alice
Hello again, Alice! Welcome back.
````

---
