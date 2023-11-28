def make_shirt(shirt_message, shirt_size="large"):
    print(f"The size of the shirt is {shirt_size.title()}.")
    print(f"The message on the shirt is {shirt_message.title()}")


# Using positional arguments
# make_shirt("medium", "this is a shirt!")

# Using keyword arguments
# make_shirt("small", "this shirt is probably too small for me.")

# Using default messages
make_shirt("i love python")
