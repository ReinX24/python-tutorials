email = input('Enter your email: ')

# We will be splitting the email by username and domain
# Finding the index of the first occurrence of @
# index = email.index('@')

# Gets the username before the @ symbol
user_name = email[:email.index('@')]

# Gets the domain after the @ symbol, does not contain @ symbol
domain = email[email.index('@') + 1:]

print(f'''
    Your username is: {user_name}
    Your domain is: {domain}''')
