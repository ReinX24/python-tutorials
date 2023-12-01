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
