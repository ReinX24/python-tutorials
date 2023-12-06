from cities import city_country


def test_city_country():
	"""Test if it properly formats 'santiago, chile' to 'Santiago, Chile'"""
	format_result = city_country('santiago', 'chile')
	assert format_result == 'Santiago, Chile'


def test_city_country_population():
	"""Test if 'santiago', 'chile', 'population=5000000' results to
	'Santiago, Chile - population - 5,000,000'"""
	format_result = city_country('santiago', 'chile',
								 population=5000000)
	assert format_result == 'Santiago, Chile - population 5,000,000'
