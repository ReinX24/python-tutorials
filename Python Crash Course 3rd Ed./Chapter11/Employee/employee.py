class Employee:
	"""Employee class that stores first name, last name, and annual salary."""

	def __init__(self, first_name, last_name, annual_salary):
		"""
		Constructor that instantiates first_name, last_name, and
		annual_salary.
		"""
		self.first_name = first_name
		self.last_name = last_name
		self.annual_salary = annual_salary

	def give_raise(self, raise_amount=5000):
		"""Raise the salary by $5,000."""
		self.annual_salary += raise_amount
