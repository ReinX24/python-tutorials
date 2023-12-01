from user import User


class Admin(User):
	"""The admin class has certain privileges."""

	def __init__(self, first_name, last_name, age, course):
		super().__init__(first_name, last_name, age, course)
		self.privileges = Privileges()


# 9 - 8
class Privileges:
	"""Privileges class that stores a list of privileges."""

	def __init__(self):
		self.privileges = ['can add post', 'can delete post', 'can ban user']

	def show_privileges(self):
		print("\nPrivileges: ")
		for privilege in self.privileges:
			print(f"- {privilege.title()}")
