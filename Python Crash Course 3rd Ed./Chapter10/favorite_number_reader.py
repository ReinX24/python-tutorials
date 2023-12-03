from pathlib import Path
import json


def read_number(path):
	"""Read the json file of favorite_number.json."""
	try:
		contents = json.loads(path.read_text())
	except FileNotFoundError:
		print(f"{path} not found!")
	else:
		print(f"Your favorite number is {contents}!")


path = Path("favorite_number.json")
read_number(path)
