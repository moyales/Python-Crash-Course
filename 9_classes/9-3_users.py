#9.3 Users

class User():
	"""Utilises info about a user."""
	
	def __init__(self, first_name, last_name, age, hometown):
		"""Initiate user info attributes."""
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.hometown = hometown
	
	def describe_user(self):
		"""Prints a summary of the user's info."""
		print("--- User Info ---")
		print("Full Name: " + self.first_name.title() + " " + self.last_name.title())
		print("Age: " + str(self.age))
		print("Hometown: " + self.hometown.title())
	
	def greet_user(self):
		"""Creates a personalized greeting to the user."""
		print("\nHello, " + self.first_name.title() + "!\n")

matthew = User('matthew', 'oyales', 18, 'hackettstown')
matthew.describe_user()
matthew.greet_user()

justin = User('justin', 'young', 18, 'east brunswick')
justin.describe_user()
justin.greet_user()
