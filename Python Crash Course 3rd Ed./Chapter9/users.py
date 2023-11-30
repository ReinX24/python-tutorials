class User:

	def __init__(self, first_name, last_name, age, course):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.course = course
		self.login_attempts = 0

	def describe_user(self):
		print(f"\nName: {self.first_name.title()} {self.last_name.title()}")
		print(f"Age: {self.age}")
		print(f"Course: {self.course.title()}")

	def greet_user(self):
		print(f"\nHello, {self.first_name.title()}")

	def increment_login_attempts(self):
		self.login_attempts += 1

	def reset_login_attempts(self):
		self.login_attempts = 0


# 9 - 7
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


# Creating an instance of the Admin class
my_admin = Admin('rein', 'solis', 20,
				 'information technology')
my_admin.describe_user()
# my_admin.show_privileges()
my_admin.privileges.show_privileges()

# 9-5 Login Attempts
# my_user = User('rein', 'solis', age=20, course='information technology')
# print(my_user.login_attempts)
# my_user.increment_login_attempts()
# my_user.increment_login_attempts()
# my_user.increment_login_attempts()
# print(my_user.login_attempts)
# my_user.reset_login_attempts()
# print(my_user.login_attempts)

# user_one = User('rein', 'solis', age=20, course='information technology')
# user_two = User('kian', 'padilla', age=20, course='language and literature')
# user_three = User('rhanniel', 'villanueva', age=20, course='nursing')

# user_one.describe_user()
# user_one.greet_user()

# user_two.describe_user()
# user_two.greet_user()

# user_three.describe_user()
# user_three.greet_user()
