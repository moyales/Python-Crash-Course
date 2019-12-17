# 8.9: Magicians

# Make a list of magician's names. Pass the list to a function
# called show_magicians(), which prints the name of each magician

def show_magicians(magician_names):
	"""Prints the names of each magician in list."""
	for magician in magician_names:
		msg = "Another great trick by " + magician.title() + "!"
		print(msg)
	
magicians = ['houdini', 'copperfield', 'carbonaro']
show_magicians(magicians)
	
