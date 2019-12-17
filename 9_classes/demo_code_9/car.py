"""A class that can be used to represent a car"""	
# Module-level docstring. Should be made for every module you make.

class Car():
	"""Simple attempt to represent a car."""
	
	def __init__(self, make, model, year):
		"""Initiate attributes to describe a car."""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
		
	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive name."""
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()
		
	def read_odometer(self):
		"""Print a statement showing the car's mileage."""
		print("This car has " + str(self.odometer_reading) + " miles on it.")
	
	def update_odometer(self, mileage):
		"""
		Set the odometer reading to the given value.
		Reject the change if attempted to roll odometer back.
		"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")
	
	def increment_odometer(self, miles):
		"""Add the given amount to an odometer reading."""
		if miles > 0:
			self.odometer_reading += miles
		else:
			print("You can't roll back an odometer!")

class Battery():
	"""A simple attempts to model a battery for electric cars."""

	def __init__(self, battery_size=70):
		"""Initialise the battery's attributes."""
		self.battery_size = battery_size
	
	def describe_battery(self):
		"""Print a statement about the battery size."""
		print("This car has a " + str(self.battery_size) + "-kWh battery.")
	
	def get_range(self):
		"""Print a statement about the range this battery provides."""
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270
		
		message = "This car can go approximately " + str(range)
		message += " miles on a full charge."
		print(message)

# __init__() for a child class:
# Assign values to all attributes in the parent class.

# This is the child class:
class ElectricCar(Car):
	"""Represents aspects of a car, specific to electric vehicles"""

	def __init__(self, make, model, year):
		"""
		Initialise attributes of the parent Class
		Then initialize attributes specific to an electric car.
		"""

		super().__init__(make, model, year)
		self.battery = Battery()