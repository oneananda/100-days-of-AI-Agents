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

## 🗂 Project Structure

```
model_based_greeting_agent/
├── main.py              # Core script
├── memory.json          # Automatically created to store user data
├── requirements.txt     # No external dependencies
└── README.md
```

---

## ▶️ How to Run

1. Clone or navigate to the repo:

   ```bash
   cd model_based_greeting_agent
   ```

2. (Optional) Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. Run the agent:

   ```bash
   python main.py
   ```

---

## 🔁 Resetting Memory

To clear saved user data, simply delete the `memory.json` file:

```bash
rm memory.json  # On Windows: del memory.json
```

---

## 🧪 Concepts Demonstrated

* Reflex vs. model-based agents
* Internal state and persistence
* Basic file I/O using JSON in Python

---

Stay tuned for **Day 02**, where we’ll explore agents with goals or utility-based behavior!

```

---

