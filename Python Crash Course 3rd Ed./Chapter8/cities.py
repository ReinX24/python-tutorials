def describe_city(city_name, city_country="philippines"):
    print(f"{city_name.title()} is in {city_country.title()}")


describe_city("iceland", "reykjavik")

# Using default argument/s
describe_city("manila")
describe_city("dagupan")

# Not using default argument/s
describe_city("tokyo", "japan")
