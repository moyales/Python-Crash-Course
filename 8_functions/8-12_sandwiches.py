#8.12 Sandwiches

# Write a function that accepts a list of items a person wants
# with an arbitrary number of arguments for sandiwch order

def sandwich_order(*ingredients):
	"""Summarizes the sandwich that is being made"""
	print("This is what you ordered in your sandwich:")
	for ingredient in ingredients:
		print("- " + ingredient)
	print('\n')

sandwich_order('bacon')
sandwich_order('salami', 'provolone')
sandwich_order('lettuce', 'mayo', 'rye', 'mustard')
