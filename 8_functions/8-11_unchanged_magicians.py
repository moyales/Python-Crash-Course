# 8.11 Unchanged Magicians

#Copy work from 8.10. Call funciton make_great() with a copy
#of the list of magician names

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



