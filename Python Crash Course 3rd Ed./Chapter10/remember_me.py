from pathlib import Path
import json

path = Path('username.json')

if path.exists():
    contents = path.read_text()
    username = json.loads(contents)
    print(f"Welcome back, {username}!")
else:
    username = input("What is your name? ")
    contents = json.dumps(username)  # converting python object to json
    path.write_text(contents)  # this creates the file if it does not exist
    print(f"We'll remember you when you come back, {username}!")

# username = input("What is your name? ")

# path = Path('username.json')
# contents = json.dumps(username)  # converting python object to json
# path.write_text(contents)

# print(f"We'll remember you when you come back {username}!")
