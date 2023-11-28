# def greet_user(username):
# The text wrapped in triple quotes is a docstring, it is used for documentation in python
"""Display a simple greeting."""


# print(f"Hello, {username.title()}!")

# greet_user('jesse')
# greet_user('sarah')

# Using a while loop alongside our function
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


while True:
    print("\nPlease tell me your name")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
