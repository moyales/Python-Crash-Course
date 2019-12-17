#8.4: Large Shirts
#Modify program from 8.3 with default values

def make_shirt(size = 'large', message = 'I love Python'):
	"""Creates a shirt with info about customisation"""
	print("You ordered a " + size + " shirt.")
	print("The message on your shirt is: '" + message + "'\n")

#Only default values
make_shirt()

#One value change
make_shirt(size = 'medium')

#Both values change
make_shirt(message = 'A different message', size = 'medium')
