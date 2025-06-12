# Day 02 – Goal-Based Task Selector Agent 🎯🧠

Welcome to Day 02 of my **100 Days of AI Agents** challenge!

This project implements a **Goal-Based Agent** that detects a user's goal and recommends an appropriate action to help achieve it. Unlike reflex agents, this agent uses internal state and evaluates multiple outcomes to guide behavior.

---

## 🧠 Agent Type

- **Type:** Goal-Based Agent  
- **Core Mechanism:** Goal recognition + action suggestion

---

## 💬 What It Does

- Asks the user what they want to accomplish.
- Parses the input to infer a goal.
- Suggests an appropriate next action based on the goal.

---

## 📂 Folder Structure

```

day02/
└── goal\_based\_task\_selector/
├── main.py
├── goals.json           # Stores goal → action mappings
├── requirements.txt
└── README.md

````

---

## ▶️ How to Run

1. Navigate to the project:
   ```bash
   cd day02/goal_based_task_selector
````

2. Run the agent:

   ```bash
   python main.py
   ```

---

## 💡 Example Interaction

```text
What would you like to do?
> I want to learn Python

Goal detected: Learn Python
Recommended action: Start with an online tutorial or interactive coding platform like Replit or Codecademy.
```

---

## 🧪 Concepts Demonstrated

* Goal detection
* State evaluation
* Simple rule-based decision engine
* Progression from reflex to goal-based behavior

---


