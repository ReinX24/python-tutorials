favorite_numbers = {
	'rein': [5, 6, 7],
	'rhanniel': [8, 9, 10],
	'elijah': [50, 51, 52],
	'gab': [23, 24, 25],
	'kian': [34, 35, 36],
}

# Printing each person's name along with their favorite numbers
for name, numbers in favorite_numbers.items():
	print(f"\n{name.title()}'s favorite numbers are:")
	for number in numbers:
		print(f"\t{number}")

# Get all the keys of our dictionary
# names = favorite_numbers.keys()

# Printing each person's name and favorite number
# for name in names:
# 	print(f"{name.title()}'s favorite number is {favorite_numbers[name]}.")
