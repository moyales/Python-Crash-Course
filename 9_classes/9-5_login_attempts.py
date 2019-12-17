#9.5 Login Attempts

class User():
	"""Utilises info about a user."""
	
	def __init__(self, first_name, last_name, age, hometown):
		"""Initiate user info attributes."""
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.hometown = hometown
		self.login_attempts = 0			# New attribute called 'login_attempts'
	
	def describe_user(self):
		"""Prints a summary of the user's info."""
		print("--- User Info ---")
		print("Full Name: " + self.first_name.title() + " " + self.last_name.title())
		print("Age: " + str(self.age))
		print("Hometown: " + self.hometown.title() + "\n")
	
	def greet_user(self):
		"""Creates a personalized greeting to the user."""
		print("\nHello, " + self.first_name.title() + "!\n")

	def increment_login_attempts(self):
		"""Increments the value of login attempts by 1."""
		self.login_attempts += 1

	def reset_login_attempts(self):
		"""Resets the value of login attempts to 0."""
		self.login_attempts = 0
		print("Login attempts reset.")
	
	def read_login_attempts(self):
		"""Reads the number of login attempts."""
		print("Login attempts: " + str(self.login_attempts))

matt = User('matthew', 'oyales', 18, 'hackettstown')

matt.describe_user()
matt.increment_login_attempts()
matt.read_login_attempts()

matt.increment_login_attempts()
matt.read_login_attempts()

matt.increment_login_attempts()
matt.read_login_attempts()

matt.reset_login_attempts()
matt.read_login_attempts()