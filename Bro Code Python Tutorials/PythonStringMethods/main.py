# name = input('Enter your full name: ')
# length of the string
# result = len(name)

# .find() find the first occurrence of a character (index)
# result = name.find('e')

# .rfind() find the last occurrence of a character
# result = name.rfind('i')

# .capitalize() capitalized the first
# name = name.capitalize()

# .upper() makes the entire string uppercase
# name = name.upper()

# .lower() makes the entire string lowercase
# name = name.lower()

# Checks if the input is a number
# result = name.isdigit()
# Checks if the string only contains alphabetical letters
# result = name.isalpha()

# print(result)

# phone_number = input('Enter your phone #: ')
# result = phone_number.count('-') # counts the amount of dashes
# phone_number = phone_number.replace('-', ' ') # replaces all dashes with spaces
# print(phone_number)

# print(help(str)) # prints all the available string methods

# validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

user_name = input('Enter your user name: ')

if len(user_name) > 12:
    print('User name must not be more than 12 characters!')
elif user_name.find(' ') >= 0:
    print('User name must not contain spaces!')
elif not user_name.isalpha():
    print('User name must not contain digits!')
else:
    print(f'Hello {user_name}')
