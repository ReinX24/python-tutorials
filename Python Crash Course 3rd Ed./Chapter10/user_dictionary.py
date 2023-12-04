from pathlib import Path
import json


def ask_name():
	"""Ask the user for their name."""
	user_name = input('Enter your name: ')
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


path = Path('user_info.json')
contents = (f"\nName: {ask_name()}"
			f"\nAge: {ask_age()}"
			f"\nHobby: {ask_hobby()}")
contents = json.dumps(contents)
path.write_text(contents)

stored_contents = path.read_text()
stored_contents = json.loads(stored_contents)
print(stored_contents)
