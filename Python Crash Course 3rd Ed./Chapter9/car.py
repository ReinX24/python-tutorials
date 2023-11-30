"""A class that can be used to represent a car."""


class Car:
	"""Simple attempt to represent a car"""

	def __init__(self, make, model, year):
		"""Initialize attributes to describe a car."""
		self.make = make
		self.model = model
		self.year = year
		# Default attributes and values for car instances of the car class
		self.odometer_reading = 0

	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive name."""
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title()

	def read_odometer(self):
		"""Print a statement showing the car's mileage"""
		print(f"This car has {self.odometer_reading:,} miles on it.")

	def update_odometer(self, mileage):
		"""
		Set the odometer reading to the given value.
		Reject the change if it attempts to roll the odometer back.
		"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")

	def increment_odometer(self, mileage):
		"""Add the given amount to the odometer reading"""
		self.odometer_reading += mileage

	def fill_gas_tank(self):
		"""Filling up the gas tank of the car."""
		print("Filling up gas tank of the car!")


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


# 9 - 9
# my_car = ElectricCar('subaru', 'outback', 2019)
# my_car.battery_size.get_range()
# my_car.battery_size.upgrade_battery()
# my_car.battery_size.get_range()

# Creating an instance of our ElectricCar class
# my_leaf = ElectricCar('nissan', 'leaf', '2024')
# print(my_leaf.get_descriptive_name())
# my_leaf.battery_size.describe_battery()
# my_leaf.battery_size.get_range()
# my_leaf.describe_battery()
# my_leaf.fill_gas_tank()

# my_used_car = Car('subaru', 'outback', 2019)
# print(my_used_car.get_descriptive_name())

# my_used_car.update_odometer(23_500)
# my_used_car.read_odometer()

# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()

# my_new_car = Car('audi', 'a4', 2024)
# print(my_new_car.get_descriptive_name())

# my_new_car.odometer_reading = 23

# my_new_car.update_odometer(25)
# my_new_car.update_odometer(23)  # will not work since we can't roll back the
# miles in an odometer
# my_new_car.read_odometer()
