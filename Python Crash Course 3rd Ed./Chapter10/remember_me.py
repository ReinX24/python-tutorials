from pathlib import Path
import json

def get_stored_username(path):
	"""Get stored username if available."""
	if path.exists():
		contents = path.read_text()
		username = json.loads(contents)
		return username
	else:
		return None

def get_new_username(path):
	"""Prompt for a new username."""
	username = input("What is your name? ")
	contents = json.dumps(username)  # converting python object to json
	path.write_text(contents)  # this creates the file if it does not exist
	return username

def greet_user():
	"""Greet the user by name."""
	path = Path('username.json')
	username = get_stored_username(path)
	if username:
		print(f"Welcome back, {username}!")
	else:
		username = get_new_username(path)
		print(f"We'll remember you when you come back, {username}!")


greet_user()

# username = input("What is your name? ")

# path = Path('username.json')
# contents = json.dumps(username)  # converting python object to json
# path.write_text(contents)

# print(f"We'll remember you when you come back {username}!")
