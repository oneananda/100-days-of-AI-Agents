import json
import os

GOAL_MAP_FILE = "goals.json"

def load_goals():
    if os.path.exists(GOAL_MAP_FILE):
        with open(GOAL_MAP_FILE, "r") as f:
            return json.load(f)
    else:
        return {}

def detect_goal(user_input, goal_map):
    user_input = user_input.lower()
    for keyword, goal_data in goal_map.items():
        if keyword in user_input:
            return goal_data
    return None

def goal_based_agent():
    print("🤖 What would you like to do?")
    user_input = input("> ")

    goal_map = load_goals()
    goal_data = detect_goal(user_input, goal_map)

    if goal_data:
        print(f"\n🎯 Goal detected: {goal_data['goal']}")
        print(f"💡 Recommended action: {goal_data['action']}")
    else:
        print("\n❓ Sorry, I couldn't identify a goal from that input.")

if __name__ == "__main__":
    goal_based_agent()
