sandwich_orders = ['tuna', 'pastrami', 'peanut butter', 'pastrami',
				   'strawberry jam', 'pastrami', 'grilled cheese']
finished_sandwiches = []

# 7 - 9
print("Sorry, the deli has ran out of pastrami...")
while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')

# 7 - 8
while sandwich_orders:
	current_sandwich = sandwich_orders.pop()
	print(f"I made your {current_sandwich.title()} sandwich.")
	finished_sandwiches.append(current_sandwich)

# Print all the elements in finished_sandwiches
print("\n[Finished Sandwiches]")
for finished_sandwich in finished_sandwiches:
	print(f"- {finished_sandwich.title()} sandwich")
