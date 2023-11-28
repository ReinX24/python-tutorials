# *toppings means that this function can accept multiple parameters
# This is an example of an arbitrary argument
def make_pizza(size, *toppings):
    """Print the list of toppings that have been requested."""
    # *toppings stores data using a tuple
    print(f"\nMaking {size}-inch pizza with the following toppings: ")
    for topping in toppings:
        print(f"- {topping}")


# make_pizza(16, 'pepperoni')
# make_pizza(12, 'muhsrooms', 'green peppers', 'extra cheese')
