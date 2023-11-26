favorite_numbers = {
	'rein': 5,
	'rhanni': 7,
	'elijah': 50,
	'gab': 23,
	'kian': 34,
}

# Get all the keys of our dictionary
names = favorite_numbers.keys()

# Printing each person's name and favorite number
for name in names:
	print(f"{name.title()}'s favorite number is {favorite_numbers[name]}.")
