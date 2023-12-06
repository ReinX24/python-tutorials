def city_country(city, country, population=None):
	"""Format city and country to a more readable format"""
	if population:
		formatted_result = f"{city.title()}, {country.title()} - population {population:,}"
	else:
		formatted_result = f"{city.title()}, {country.title()}"
	return formatted_result
