#Exercise 4.13: Buffet
#Make a tuple containing items in a buffet that cannot change.
buffet = ("chicken", "steak", "salad", "beans", "pork")
for foods in buffet:
	print(foods)
	
buffet = ("chicken", "prime rib", "salad", "beans", "bacon")
print("\nNew items in the buffet:")
for foods in buffet:
	print(foods)
