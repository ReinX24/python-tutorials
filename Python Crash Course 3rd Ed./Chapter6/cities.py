cities = {
	'dagupan': {
		'country': 'philippines',
		'population': '174,302',
		'fact': 'it is known to be the World\'s Bangus Capital.',
	},
	'kyoto': {
		'country': 'japan',
		'population': '1,459,640',
		'fact': 'was the capital city of Japan for more than a thousand years.',
	},
	'new york': {
		'country': 'united states',
		'population': '18,937,000',
		'fact': 'the city\'s original name was New Amsterdam.',
	},
	'shanghai': {
		'country': 'china',
		'population': '29,211,000',
		'fact': 'it is the 3rd biggest city in the world.',
	},
	'busan': {
		'country': 'south korea',
		'population': '3,357,737',
		'fact': '\'busan\' means \'Cauldron Mountain\' in Korean.',
	},
}

for city, city_info in cities.items():
	print(f"\n{city.title():10}:")
	for category, info in city_info.items():
		print(f"\t{category.title():10}: {info.title()}")
