# A demonstration of inheritance

# If a class is a specialized version of another class, you can use an 'inheritance'
# When one class inherits from another, it takes the attributes of the first class.
# Original class is 'parent' class. The new one is the 'child' class.

# This is the parent class.
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

# __init__() for a child class:
# Assign values to all attributes in the parent class.

# This is the child class.
class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles."""

	def __init__(self, make, model, year):
		"""Initialise attributes of the parent class."""
		super().__init__(make, model, year)

my_tesla = ElectricCar('tesla', 'model 3', 2019)
print(my_tesla.get_descriptive_name())
