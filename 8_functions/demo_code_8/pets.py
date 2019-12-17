def describe_pet(species, name):
	"""Display info about a pet"""
	print("I have a " + species + ".")
	print("My " + species + "'s name is " + name.title() + ".\n")

describe_pet('parrot', 'alex')

#With keyword arguments
describe_pet(name = 'brian', species = 'dog')
