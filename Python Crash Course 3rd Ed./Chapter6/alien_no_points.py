alien_0 = {'color': 'green', 'speed': 'slow'}

# Printing a value that does not exist, throws an exception
# print(alien_0['points'])

# Using the get() method to return a default value if the value does
# not exist. This default value is stored at the second parameter.
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

# When we do not specify a default value, the get method returns None
damage_value = alien_0.get('damage')
print(damage_value)
