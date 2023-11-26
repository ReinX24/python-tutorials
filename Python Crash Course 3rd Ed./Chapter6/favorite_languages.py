# Dictionary that contains names and their favorite programming language
# After the last key value pair, it is good practice to add a comma so
# that adding a key value pair manually wil be easier
# favorite_languages = {
# 	'jen': 'python',
# 	'sarah': 'c',
# 	'edward': 'rust',
# 	'phil': 'python',
# }

# 6 - 6 Polling
# names = ['jen', 'rein', 'sarah', 'reinne', 'phil']

# for name in names:
# 	if name in favorite_languages:
# 		print(f"Thank you {name.title()} for taking the poll!")
# 	else:
# 		print(f"You are invited to take the poll {name.title()}.")
# End of 6 - 6 Polling

# Making sure that there are no duplicate values printed using set()
# set() makes sure that we do not print the same value twice
# print("The following languages have been mentioned:")
# for language in set(favorite_languages.values()):
# 	print(language.title())


# Printing just the values in our dictionary
# print("The following languages have been mentioned:")
# for language in favorite_languages.values():
# 	print(language.title())

# Printing the keys in our dictionary in alphabetical order
# for name in sorted(favorite_languages):
# 	print(f"{name.title()}, thank you for taking the poll.")

# friends = ['sarah', 'phil']
# Checking if one of the keys is contained in a list
# for name in favorite_languages:
# 	print(f"Hi {name.title()}.")

# Custom message to keys in our friends list
# if name in friends:
# 	language = favorite_languages.get(name).title()
# 	print(f"\t{name.title()}, I see you love {language}!")

# Checking if 'erin' took the poll
# if 'erin' not in favorite_languages:
# 	print("Erin, please take our poll!")

# print(favorite_languages)
# sarah_language = favorite_languages['sarah']
# edward_language = favorite_languages['edward']
# phil_language = favorite_languages['phil']

# print(f"Sarah's favorite language is {sarah_language.title()}.")
# print(f"Edward's favorite language is {edward_language.title()}.")
# print(f"Phil's favorite language is {phil_language.title()}.")

# Printing each key value pair in favorite_languages
# for name, language in favorite_languages.items():
# 	print(f"{name.title()}'s favorite language is {language.title()}.")

# Just printing the names of everyone who took the poll
# for name in favorite_languages.keys():
# 	print(name.title())

# This produces the same output since when we loop through a dictionary,
# the default is looping through its keys
# for name in favorite_languages:
# 	print(name.title())

# Putting lists inside dictionaries
favorite_languages = {
	'jen': ['python', 'rust'],
	'sarah': ['c'],
	'edward': ['rust', 'go'],
	'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
	if len(languages) == 1:
		print(
			f"\n{name.title()}'s favorite language is {languages[0].title()}.")
	else:
		print(f"\n{name.title()}'s favorite languages are:")
		for language in languages:
			print(f"\t{language.title()}")
