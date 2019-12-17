# 9.8 Privileges
# From the last program, create a new class called Privileges.

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
		print("Hometown: " + self.hometown.title() + "\n")
	
	def greet_user(self):
		"""Creates a personalized greeting to the user."""
		print("\nHello, " + self.first_name.title() + "!\n")

class Privileges():
	"""Defines the priviliges of an admin."""

	def __init__(self, admin_privileges=['Ban users', 'Invite members', 'Edit server']):
		self.admin_privileges = admin_privileges
	
	def show_privileges(self):
		"""Prints out the privileges an admin has."""
		for privilege in self.admin_privileges:
			print("> " + privilege)

class Admin(User):
    """Displays the privileges of an admin."""

    def __init__(self, first_name, last_name, age, hometown):
        """Parent attributes."""

        super().__init__(first_name, last_name, age, hometown)
        self.privileges = Privileges()
    
    
administrator = Admin('matt', 'oyales', 18, 'hoboken')
administrator.describe_user()
administrator.privileges.show_privileges()