# 9.7 Admin
# Create a class called 'admin' that inherits from User class.

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

class Admin(User):
    """Displays the privileges of an admin."""

    def __init__(self, first_name, last_name, age, hometown):
        """Parent attributes."""

        super().__init__(first_name, last_name, age, hometown)
        self.privileges = ["Can delete posts", "Can ban users", "Can promote users", "Edit/Manage Servers"]
    
    def show_privileges(self):
        """Lists out the privileges an admin has."""
        print("Admins have the following privileges:")
        for privilege in self.privileges:
            print("> " + privilege)

administrator = Admin('matt', 'oyales', 18, 'hoboken')
administrator.describe_user()
administrator.show_privileges()

    
