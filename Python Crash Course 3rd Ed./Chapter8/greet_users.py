# A function that uses a list as its parameter
def greet_users(names):
    """Print a simple greeting to each user in the list"""
    for name in names:
        message = f"Hello, {name.title()}!"
        print(message)


usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
