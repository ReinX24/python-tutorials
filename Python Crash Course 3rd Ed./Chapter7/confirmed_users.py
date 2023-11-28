unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# This iterates through the unconfirmed_users list as long as that list has elements within the list
while unconfirmed_users:
	current_user = unconfirmed_users.pop()  # takes the last element in the list

	print(f"Verifying user: {current_user.title()}")
	confirmed_users.append(current_user)

# Displaying all the confirmed_users elements
print(f"\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
	print(confirmed_user.title())
