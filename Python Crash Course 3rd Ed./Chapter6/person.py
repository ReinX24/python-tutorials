person_one = {
	'first_name': 'john',
	'last_name': 'carmack',
	'city': 'kansas'
}

person_two = {
	'first_name': 'james',
	'last_name': 'gosling',
	'city': 'alberta'
}

person_three = {
	'first_name': 'bjarne',
	'last_name': 'stroustrup',
	'city': 'denmark'
}

# Putting all dictionaries inside a list
people = [person_one, person_two, person_three]

for person in people:
	full_name = f"{person.get('first_name')} {person.get('last_name')}"
	city_location = f"{person.get('city')}"
	print(f"\n\tName: {full_name.title()}")
	print(f"\tCity: {city_location.title()}")

# print(f"First Name: {person_one.get('first_name').title()}")
# print(f"Last Name: {person_one.get('last_name').title()}")
# print(f"City: {person_one.get('city').title()}")
