#7.8: Deli
#Make a list called sandwich orders and fill it with sandwich names
#Make an empty list called finished_sandwiches and loop through

sandwich_orders = ['pastrami', 'italian', 'cuban', 'BLT']
finished_sandwiches = []

while sandwich_orders:
	order = sandwich_orders.pop()
	
	print("I made your " + order + " sandwich.")
	finished_sandwiches.append(order)

print("\nThese are the sandwiches that were made:")
for sandwich in finished_sandwiches:
	print(sandwich)
