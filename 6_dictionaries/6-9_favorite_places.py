#6.9: Favorite Places
#Make a dictionary called favorite_places
#Store names of people as keys and list their favorite places
#Putting a list inside of a dictionary

favorite_places = {
	'matt' : ['montreal', 'new york', 'san francisco'],
	'bob' : ['berlin', 'sydney'],
	'ellen' : ['rotterdam', 'stockholm', 'paris'],
	'mary' : ['atlanta'],
	'john' : ['los angeles', 'tacoma']
	}

for name,places in favorite_places.items():
	print("\n")
	if len(places) > 1:
		print(name.title() + "'s favorite places are:")
		for place in places:
			print("\t" + place.title())	
	else:
		print(name.title() + "'s favorite place is:")
		for place in places:
			print("\t" + place.title())

	
