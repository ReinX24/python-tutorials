"""A set of classes that can be used to represent electric cars."""

from car import Car


class Battery:
	"""
	This is a class that will serve as a component for our ElectricCar class.
	This is not a subclass of another class, it is an independent class.
	"""

	def __init__(self, battery_size=40):
		"""Initialize the battery's attributes."""
		self.battery_size = battery_size

	def describe_battery(self):
		"""Print a statement describing the battery size."""
		print(f"This car has a {self.battery_size}-kWh battery.")

	def get_range(self):
		"""Print a statement about the range this battery provides."""
		if self.battery_size == 40:
			distance_range = 150
		elif self.battery_size == 65:
			distance_range = 255

		print(f"This car can go about {distance_range} miles on a full range.")

	def upgrade_battery(self):
		if self.battery_size == 40:
			self.battery_size = 65
		else:
			print('Battery size cannot be upgraded!')


# Creating a child class of our Car class (ElectricCar)
class ElectricCar(Car):
	"""
	Represents aspects of a car, specific to electric vehicles.
	When this class inherits from Car, it inherits all its attributes and
	functions that are in that class.
	"""

	def __init__(self, make, model, year):
		"""
		Initialize the attributes of the parent class.
		Then initialize attributes specific to an electric car.

		Creating an instance of the Battery class instead.
		This creates an instance of a Battery class which can holds certain
		values and functions.
		"""
		super().__init__(make, model, year)
		# self.batter_size = 40
		self.battery_size = Battery()

	def describe_battery(self):
		"""Print a statement describing the battery size."""
		print(f"This car has a {self.batter_size}-kWh battery.")

	def fill_gas_tank(self):
		"""
		Electric cars don't have has tanks.
		This method overrides the method in the Car class (superclass).
		"""
		print("This car doesn't have a gas tank!")
