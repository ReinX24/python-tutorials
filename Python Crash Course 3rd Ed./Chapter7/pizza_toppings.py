prompt = "\nEnter a topping to be added to your pizza:"
prompt += "\n(Enter 'quit' to exit program) "

topping_added = ""
all_toppings = []

while topping_added != "quit":
	topping_added = input(prompt)

	if topping_added != "quit":
		print(f"\n{topping_added} will be added to your pizza!")
		all_toppings.append(topping_added)
	else:
		print("\n[Summary of Toppings]")
		for topping in all_toppings:
			print(f"- {topping}")
