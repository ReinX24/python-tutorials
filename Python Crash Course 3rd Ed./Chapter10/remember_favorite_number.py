from pathlib import Path
import json


def ask_favorite_number(path):
	"""Asking the user for their favorite number."""
	try:
		favorite_number = int(input("\nEnter your favorite number: "))
	except ValueError:
		print(f"\n{favorite_number} is not a valid input!")
	else:
		path.write_text(json.dumps(favorite_number))


def read_favorite_number(path):
	"""Reading the user's stored favorite number."""
	try:
		favorite_number = json.loads(path.read_text())
	except FileNotFoundError:
		print(f"\n{path} not found!")
	else:
		print(f"\n{favorite_number} is your favorite number!")


def user_menu():
	"""Menu that the user could use to write or read their favorite number."""
	path = Path('favorite_number.json')
	while True:
		print("\n[Favorite Number Recorder]")
		print("[1] Record Favorite Number")
		print("[2] Read Favorite Number")
		print("[q] Quit Program")
		user_choice = input("> ")

		if user_choice == '1':
			ask_favorite_number(path)
		elif user_choice == '2':
			read_favorite_number(path)
		elif user_choice == 'q':
			print("\n[Program Terminated]")
			break
		else:
			print("\nInvalid Input!")


user_menu()
