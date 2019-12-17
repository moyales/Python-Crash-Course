#9.4 Number Served

class Restaurant():
	"""A model for a restuarant name and cuisine type."""
	
	def __init__(self, restaurant_name, cuisine_type):
		"""Initiate name and cuisine type attributes."""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.customers_served = 0
	
	def describe_restaurant(self):
		"""Describes restaurant name and cuisine type."""
		print("The restaurant is called " + 
		     self.restaurant_name.title() + ".")
		print(self.restaurant_name.title() + " serves " + 
		     self.cuisine_type.title() + " food.")
	
	def open_restaurant(self):
		"""Tells that the restaurant is now open."""
		print(self.restaurant_name.title() + " is now open.\n")
		
	def update_c_served(self, number_served):
		"""Updates the number of customers served."""
		self.customers_served = number_served
	
	def increment_c_served(self, served):
		"""Increments the number of customers served."""
		self.customers_served += served
				
	def read_customers_served(self):
		"""Prints out the number of customers served."""
		print("Restaurant served " + str(self.customers_served) + " people.")
	
	
new_restaurant = Restaurant('bennys', 'italian')	

new_restaurant.describe_restaurant()
new_restaurant.update_c_served(10)
new_restaurant.read_customers_served()

new_restaurant.increment_c_served(20)
new_restaurant.read_customers_served()

new_restaurant.increment_c_served(20)
new_restaurant.read_customers_served()


