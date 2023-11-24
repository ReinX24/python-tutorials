# Copying a list
# my_foods = ['pizza', 'falafel', 'carrot cake']
# friend_foods = my_foods[:]  # copies all the elements in the lists
# this indexes the start of the list until the end of the list,
# thus copying all the elements of the list

# Incorrect way of copying a list, it makes the elements of each list
# the same regardless if we add them to our list or our friend's list
# friend_foods = my_foods

# my_foods.append('cannoli')  # adding an element to our list
# friend_foods.append('ice cream')  # adding an element to our friend's list

# print('My favorite foods are:')
# print(my_foods)

# print('\nMy friend\'s favorite foods are:')
# print(friend_foods)

# 4 - 10 Slices
# Print the first three items of a list
# print('\nThe first three items in the list are:')
# print(my_foods[:3])

# Print the 3 items from the middle of our list
# Adding another element to our list to make it 5 elements
# my_foods.append('french fries')
# print(my_foods)
# middle_index = int(len(my_foods) / 2)
# print(my_foods[middle_index - 1: middle_index + 2])

# Print the last 3 items in our list
# print(my_foods)
# print(my_foods[-3:])

# 4 - 11 My Pizzas, Your Pizzas
# my_pizzas = ['pepporoni', 'hawaiian', 'cheese', 'bacon', 'veggie']

# Copy of our pizzas list
# friend_pizzas = my_pizzas[:]

# Add a new pizza to the list friend_pizzas
# friend_pizzas.append('sausage')

# print('My favorite pizzas are:')
# for pizza in my_pizzas:
#     print(f'| {pizza:10} |')

# print('\nMy friend\'s favorite pizzas are:')
# for pizza in friend_pizzas:
#     print(f'| {pizza:10} |')

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]  # copies all the elements in the lists

# Adding a unique element for each of our list
my_foods.append('burger')
friend_foods.append('ice cream')

print('My food list:')
for food in my_foods:
    print(f'# {food:10}')

print('\nFriend\'s food list:')
for food in friend_foods:
    print(f'# {food:10}')