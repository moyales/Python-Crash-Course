#9.1 Restaurant

class Restaurant():
	"""A model for a restuarant name and cuisine type."""
	
	def __init__(self, restaurant_name, cuisine_type):
		"""Initiate name and cuisine type attributes."""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
	
	def describe_restaurant(self):
		"""Describes restaurant name and cuisine type."""
		print("The restaurant is called " + 
		     self.restaurant_name.title() + ".")
		print(self.restaurant_name.title() + " serves " + 
		     self.cuisine_type.title() + " food.")
	
	def open_restaurant(self):
		"""Tells that the restaurant is now open."""
		print(self.restaurant_name.title() + " is now open.\n")
		
	def close_restaurant(self):
		"""Tells that the restuarant is closed."""
		print(self.restaurant_name.title() + " is currently closed.\n")

new_restaurant = Restaurant('gusteaus', 'french')

new_restaurant.describe_restaurant()
new_restaurant.open_restaurant()
		
