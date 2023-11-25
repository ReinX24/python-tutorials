# 5 - 8 and 5 - 9
# usernames = ['reinx24', 'ryunisen', 'solarine', 'kit', 'nitrotoxic', 'admin']
# usernames = []

# if usernames:
# 	for name in usernames:
# 		if name == 'admin':
# 			print(f'Hello {name}, would you like to see a status report?')
# 		else:
# 			print(f'Hello {name}, thank you for logging in again.')
# else:
# 	print('We need to find some users!')

# 5 - 10
current_users = ['reinx24', 'RYUNISEN', 'CASABLANCA', 'nitrotoxic', 'reinne']

# Making all the names in current_users lower case
current_users = [user.lower() for user in current_users]
new_users = ['kit', 'solarine', 'RYUnisen']

for user in new_users:
	if user.lower() in current_users:
		print(f'{user} is being used, enter a new username.')
	else:
		print(f'{user} is available.')
