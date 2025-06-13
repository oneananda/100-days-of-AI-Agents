# Day 03 – Utility-Based Decision Agent 🎯📈

Welcome to Day 03 of my **100 Days of AI Agents** challenge!

This project explores a **Utility-Based Agent**, which selects actions not just based on goals, but also based on the **utility value** (usefulness) of possible outcomes. This represents a more advanced decision-making process compared to reflex or goal-based agents.

---

## 🧠 Agent Type

- **Type:** Utility-Based Agent  
- **Core Mechanism:** Goal recognition + action evaluation based on utility scores

---

## 💬 What It Does

- Asks the user to describe their goal.
- Looks up a list of potential actions for that goal.
- Recommends the action with the highest utility (i.e., the most helpful).

---

## 📂 Folder Structure

```

utility\_based\_decision\_agent/
├── main.py              # Core agent logic
├── utilities.json       # Goal → actions + utility scores
├── requirements.txt     # No external dependencies
└── README.md

````

---

## ▶️ How to Run

1. Navigate to the folder:
	```bash
	   cd day03/utility_based_decision_agent
	```

2. Run the agent:

   ```bash
   python main.py
   ```

---

## 💡 Example Interaction

```text
🤖 What is your goal?
> get fit

🎯 Best action to achieve 'get fit':
✅ Lift weights (utility: 9)
```

---

## 🧪 Concepts Demonstrated

* Action ranking based on utility values
* Conditional decision-making
* A step toward more intelligent, preference-aware agents

---

## 🔧 How It Works

* Goals and action sets are defined in `utilities.json`.
* Each action has a utility score between 1–10.
* The agent selects the action with the highest utility using `max()`.

---

## 🧠 Future Enhancements

* Multi-goal prioritization
* Utility calculation based on user preferences
* Integration with real data sources for dynamic scoring

---


