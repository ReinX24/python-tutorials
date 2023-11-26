favorite_places = {
	'rein': ['nepo mall', 'open laboratory', 'mixue ice cream shop'],
	'rhanniel': ['miniso', 'library', 'jollibee'],
	'mon': ['puregold', 'bon chon', 'mcdonalds'],
}

for name, places in favorite_places.items():
	print(f"\n{name.title()}'s favorite places:")
	for place in places:
		print(f"\t{place.title()}")
