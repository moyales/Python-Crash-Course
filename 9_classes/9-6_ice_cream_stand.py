# 9.6 Ice Cream Stand

# Write a class called IceCreamStand that inherits from Restaurant.

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

class IceCreamStand(Restaurant):
    """Models information about an ice cream stand."""
    
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes for parent class, followed by attributes for child."""

        super().__init__(restaurant_name, cuisine_type)			# Don't forget the () in the super method!
        self.show_flavors = ['vanilla', 'chocolate', 'strawberry']

    def read_flavors(self):         # Remember to undent after super!
        """Read the list of ice cream flavors."""
        print(self.restaurant_name.title() + " serves:")
        for flavor in self.show_flavors:
            print(flavor.title())

ice_cream = IceCreamStand('ben n jerrys', 'ice_cream')
ice_cream.read_flavors()
