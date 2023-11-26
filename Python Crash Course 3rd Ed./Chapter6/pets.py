pets = [
	{
		'animal': 'dog',
		'owner': 'rhanniel'
	},
	{
		'animal': 'cat',
		'owner': 'rein'
	},
	{
		'animal': 'bird',
		'owner': 'reinne'
	},
	{
		'animal': 'frog',
		'owner': 'kian'
	},
]

for pet in pets:
	print(f"\n\tAnimal: {pet.get('animal').title()}")
	print(f"\tOwner: {pet.get('owner').title()}")
