# Store information about a pizza being ordered
pizza = {
	'crust': 'thick',
	'toppings': ['mushrooms', 'extra cheese'],
}

# Summarize the order
print(
	f"You ordered a {pizza.get('crust')}-crust pizza "
	f"with the following toppings:")

for topping in pizza.get('toppings'):
	print(f"\t{topping}")
