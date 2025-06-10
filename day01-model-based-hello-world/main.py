import json
import os

DATA_FILE = "memory.json"

def load_memory():
	"""Load memory from a JSON file, or return an empty dictionary if the file does not exist."""
	if os.path.exists(DATA_FILE):
		with open(DATA_FILE, 'r') as file:
			return json.load(file)
	return {}

def save_memory(memory):
	"""Save memory to a JSON file."""
	with open(DATA_FILE, 'w') as file:
		json.dump(memory, file, indent=4)

def get_greeting(name):
	"""Generate a greeting for the given name, using memory to remember past greetings."""
	memory = load_memory()
	if name in memory:
		return f"Welcome back, {name}! I remember you."
	else:
		memory[name] = True  # Remember this name
		save_memory(memory)
		return f"Hello, {name}! Nice to meet you for the first time."
