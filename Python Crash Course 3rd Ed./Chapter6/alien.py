# alien_0 = {
# 	'color': 'green',
# 	'points': 5
# }

# Printing dictionary values
# print(alien_0['color'])
# print(alien_0['points'])

# Using dictionary values
# new_points = alien_0['points']
# print(f'You just earned {new_points} points!')

# Adding new key value pairs to our dictionary
# print(alien_0)
# alien_0['x-position'] = 0
# alien_0['y-position'] = 25
# print(alien_0) # attributes are ordered in the way they were added

# Adding values to an empty dictionary
# alien_0 = {}
# alien_0['color'] = 'green'
# alien_0['points'] = 5
# print(alien_0)

# Modifying values in a dictionary
# alien_0 = {'color': 'green'}
# print(f"The alien is {alien_0['color']}.")
# alien_0['color'] = 'yellow'
# print(f"The alien is now {alien_0['color']}.")

# alien_0 = {'x-position': 0, 'y-position': 25, 'speed': 'medium'}
# print(f"Original position: {alien_0['x-position']}")

# Changing the speed of the alien
# alien_0['speed'] = 'fast'

# Move the alien to the right
# Determine how far to move the alien based on its current speed
# if alien_0['speed'] == 'slow':
# 	x_increment = 1
# elif alien_0['speed'] == 'medium':
# 	x_increment = 2
# else:
# This must be a fast alien
# x_increment = 3

# The new position of the alien is the old position plus the increment
# alien_0['x-position'] = alien_0['x-position'] + x_increment
# alien_0['x-position'] += x_increment
# print(f"New position: {alien_0['x-position']}")

# Removing key value pairs
# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)

# del alien_0['points']  # deletes the points key value pair
# print(alien_0) # note: this deletes the key value pair permanently

# Nesting
# A List of Dictionaries
# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}

# Placing all these dictionaries in a list
# aliens = [alien_0, alien_1, alien_2]

# for alien in aliens:
# 	print(alien)

# Make an empty list for storing aliens
aliens = []

# Make 30 green aliens
for alien_number in range(30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)

# Changing the first three aliens to yellow, medium speed, and worth 10
# points each
for alien in aliens[:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['points'] = 10
		alien['speed'] = 'medium'
	elif alien['color'] == 'yellow':
		alien['color'] = 'red'
		alien['points'] = 15
		alien['speed'] = 'fast'

# Show the first 5 aliens
for alien in aliens[:5]:
	print(alien)
print('...')

# Show how many aliens have been created
print(f"Total number of aliens: {len(aliens)}")
