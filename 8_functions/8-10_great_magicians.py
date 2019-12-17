# 8.10 Great Magicians

# Use a copy of 8.9
# Write a function called make_great() that modifies the list of
# magicians by adding the phrase "the Great" to each magician's name

def show_magicians(magician_names):
	"""Prints the names of each magician in list."""
	for magician in magician_names:
		msg = "Another great trick by " + magician.title() + "!"
		print(msg)
	

def make_great(magician_names, greatness):
	"""Modifies list of magicians by adding 'the Great' to name"""
	while magician_names:
		great = magician_names.pop()
		greatness.append(great + " the Great")
	
	for greats in greatness:
		print(greats)
		

magician_names = ['houdini', 'copperfield', 'carbonaro']
great = []

show_magicians(magician_names)
make_great(magician_names, great)
