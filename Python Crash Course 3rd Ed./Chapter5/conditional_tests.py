# 5 - 1 Conditional Tests
# car = 'subaru'
# print('Is car == \'subaru\'? I predict True.')
# print(car == 'subaru')

# print('\nIs car == \'audi\'? I predict False.')
# print(car == 'audi')

# Test 1 & 2
# my_name = 'rein'
# print(my_name == 'rein')
# print(my_name == 'rain')

# Test 3 & 4
# my_phone = 'android'
# print(my_phone == 'ios')
# print(my_phone == 'android')

# Test 5 & 6
# main_champion = 'zed'
# print(main_champion == 'zed')
# print(main_champion == 'yasuo')

# Test 7 & 8
# processor = '5600G'
# print(processor == '5700G')
# print(processor == '5600G')

# Test 9 & 10
# my_hobby = 'programming'
# print('Does my_hobby == \'programming\'? I predict True.')
# print(my_hobby == 'programming')
#
# print('\nDoes my_hobby == \'smoking\'? I predict False.')
# print(my_hobby == 'smoking')

# 5 - 2 More Conditional Tests
# Equality and inequality with strings
# Tests using the lower() method
# my_name = 'Rein'

# if my_name.lower() == 'rein':
# 	print(f'Welcome back {my_name}!')
# else:
# 	print('Who are you?')

# Numerical tests involving equality and inequality, greater than
# and less than, greater than or equal to, and less than or equal to
# user_age = int(input('Enter your age: '))

# if user_age > 18:
# 	print('You are above 18!')
# if user_age < 18:
# 	print('You are below 18!')
# if user_age >= 18:
# 	print('You are 18 or above!')
# if user_age <= 18:
# 	print('You are 18 or below!')

# Using the 'and' keyword
# is_busy = True
# is_adult = True
# if is_busy and is_adult:
# 	print('Do not disturb!')
# else:
# 	print('Yes what is it?')

# Using the 'or' keyword
# my_age = 20
# friend_age = 18
# if my_age > 18 or friend_age > 18:
# 	print('Either me or my friend is over 18.')
# else:
# 	print('Neither me or my friend is over 18.')

# Testing whether an item is in a list or not
# my_hobbies = ['programming', 'gaming', 'reading', 'sleeping', 'eating']
# if 'programming' in my_hobbies:
# 	print('One of my hobbies is programming!')
# else:
# 	print('Programming is not one of my hobbies...')

# Testing whether an item is NOT in a list
my_hobbies = ['programming', 'gaming', 'reading', 'sleeping', 'eating']
if 'smoking' not in my_hobbies:
	print('Smoking is not one of my hobbies.')
