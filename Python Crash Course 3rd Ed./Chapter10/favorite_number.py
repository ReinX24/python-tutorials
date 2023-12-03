from pathlib import Path
import json


def ask_number(path):
	"""Ask the user for their favorite number."""
	while True:
		try:
			number = input("Enter your favorite number: ")
		except ValueError:
			print(f"{number} is not a number!")
		else:
			contents = json.dumps(int(number))
			path.write_text(contents)
			print(f"Your favorite number {number} has been recorded!")
			break


path = Path('favorite_number.json')
ask_number(path)
