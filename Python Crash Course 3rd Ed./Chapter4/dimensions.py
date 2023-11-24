# This is a tuple, it is an immutable set of values
# We use parentheses instead of brackets to store values
dimensions = (200, 50)
# print(dimensions[0])
# print(dimensions[1])

# Looping through our tuple
# for dimension in dimensions:
#     print(dimension)

# Redefining a tuple by assigning it to new tuple values
print('Original dimensions:')
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print('\nModified dimensions:')
for dimension in dimensions:
    print(dimension)

# dimensions[0] = 250  # trying to change value in our tuple, causes an exception

# A tuple with one element should end with a comma
# my_t = (3, )
# print(my_t)
