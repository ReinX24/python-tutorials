# user_0 = {
# 	'username': 'efermi',
# 	'first': 'enrico',
# 	'last': 'fermi',
# }

# Looping through the list and printing its keys and their associated values
# for key, value in user_0.items():
# 	print(f"\nKey: {key}")
# 	print(f"Value: {value}")

users = []

for user in range(10):
	new_user = {'name': 'user_' + str(user), 'id': user, 'access': 'basic'}
	users.append(new_user)

# Make first 3 users have admin access
for user in users[:3]:
	if user['access'] == 'basic':
		user['access'] = 'admin'

for user in users[:5]:
	print(user)