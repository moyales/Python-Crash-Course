#6.8: Pets
#Make several dictionaries where each is the name of a pet.

#Several dictionaries
finnegan = {'name' : 'finnegan', 'species' : 'cat', 'owner' : 'matt'}
alex = {'name' : 'alex', 'species' : 'cockatiel', 'owner' : 'aussie'}
gaucho = {'name' : 'gaucho', 'species' : 'dog', 'owner' : 'tani'}
rocky = {'name' : 'rocky', 'species' : 'lizard', 'owner' : 'teacher'}
leroy = {'name' : 'leroy' ,'species' : 'goldfish', 'owner' : 'mohammed'}

#List of pets
pets = [finnegan, alex, gaucho, rocky, leroy]

#Looping through list with info about each pet
for pet in pets:
	print("Name: " + pet["name"].title())
	print("Species: " + pet['species'].title())
	print("Owner: " + pet['owner'].title() + "\n")
