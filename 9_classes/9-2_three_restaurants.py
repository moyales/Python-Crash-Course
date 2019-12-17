#9.2 Three Restaurants

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
		     self.cuisine_type.title() + ".\n")
	
	def open_restaurant(self):
		"""Tells that the restaurant is now open."""
		print(self.restaurant_name.title() + " is now open.\n")
		
cracker_barrel = Restaurant('cracker barrel', 'southern')
mamas = Restaurant('mamas', 'italian')
peter_luger = Restaurant('peter luger', 'steaks')

cracker_barrel.describe_restaurant()
mamas.describe_restaurant()
peter_luger.describe_restaurant()
