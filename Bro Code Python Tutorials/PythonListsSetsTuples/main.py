# collection = single 'variable' used to store multiple values
# List = [] ordered and changeable. Duplicated OK
# Set = {} unordered and immutable, but Add/Remove OK. No duplicates
# Tuple = () ordered and unchangeable. Duplicates OK. FASTER

# Lists
# fruits = ['apple', 'apple', 'orange', 'banana', 'coconut']
# print(fruits[::-1])
# for fruit in fruits:
#     print(fruit)

# List all functions we can use on a list
# print(dir(fruits))

# List all the functions and attributes on a list
# print(help(fruits))

# print(len(fruits))
# print('pineapple' in fruits)  # prints True or False

# fruits[2] = 'pineapple'
# fruits.append('pineapple')
# fruits.remove('apple')
# fruits.insert(0, 'pineapple')
# fruits.sort()
# fruits.sort(reverse=True)
# fruits.reverse()  # reverses order in list
# fruits.clear()
# print(fruits.index('coconut'))  # finds the index of an element in a list
# print(fruits.count('apple'))  # counts the amount of similar elements in a list
# print(fruits)

# Sets
# We cannot alter the values within sets but we can add / remove elements
# Duplicates are not allowed on the list
# fruits = {'apple', 'orange', 'banana', 'coconut', 'coconut'}
# ^ only contains 1 contain coconut element

# Displaying all the methods and attributes of a set
# print(dir(fruits))

# Displaying descriptions of different methods and attributes of a set
# print(help(fruits))

# print(len(fruits))
# print('apple' in fruits)
# print(fruits[0])  # causes an exception
# fruits.add('pineapple')
# fruits.remove('apple')

# print(fruits)
# print(fruits.pop()) # returns and removes the first element of a list
# fruits.clear()
# print(fruits)  # changes order whenever we print our set

# Tuples
# Ordered and unchangeable. Can contain duplicates. Is faster
fruits = ('apple', 'orange', 'banana', 'coconut', 'apple')
# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print('pineapple' in fruits)
# print(fruits.index('coconut'))
# print(fruits.count('apple'))

for fruit in fruits:
    print(fruit)