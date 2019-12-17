#passing a list to a function

#This function will expect a list of names
def greet_users(names):
	"""Print a simple greeting to each user in the list."""
	for name in names:
		msg = "Hello, " + name.title() + "!"
		print(msg)
	
usernames = ['brian', 'matt', 'david']
greet_users(usernames)
