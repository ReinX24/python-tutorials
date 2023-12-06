from pathlib import Path
import json


def ask_name():
	"""Ask the user for their name."""
	user_name = input('\nEnter your name: ')
	return user_name


def ask_age():
	"""Ask the user for their age."""
	try:
		user_age = int(input('Enter your age: '))
	except ValueError:
		print(f"Invalid input!")
	else:
		return user_age


def ask_hobby():
	"""Ask the user for one of their hobbies."""
	user_hobby = input('Enter a hobby: ')
	return user_hobby


def ask_username(path):
	"""Ask if the stored username is the same with the current user."""
	stored_contents = path.read_text()
	stored_contents = json.loads(stored_contents)
	stored_username = stored_contents.get('name')

	is_running = True
	while is_running:
		user_choice = input(f'Is your name {stored_username}? (y/n): ')
		if user_choice == 'y':
			is_running = False
			greet_user(stored_username)
		elif user_choice == 'n':
			is_running = False
			record_new_user(path)
		else:
			print('Invalid Input!')


def record_new_user(path):
	"""Ask the user for a new username."""
	contents = {}

	contents['name'] = ask_name()
	contents['age'] = ask_age()
	contents['hobby'] = ask_hobby()

	contents = json.dumps(contents)
	path.write_text(contents)


def greet_user(username):
	"""Welcomes back the user."""
	print(f'\nWelcome back, {username}!')


path = Path('user_info.json')
if path.exists():
	ask_username(path)
else:
	record_new_user(path)
