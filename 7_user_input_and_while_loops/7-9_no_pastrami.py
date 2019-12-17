#7.9: No Pastrami

sandwich_orders = ['pastrami', 'italian', 'pastrami', 'cuban', 'BLT', 'pastrami', 'egg']

print("-- Current Deli Orders --")
for orders in sandwich_orders:
	print(orders)

print("\nSorry, the deli has ran out of pastrami.")

while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')

print("\n-- Finished Sandwiches --")
for orders in sandwich_orders:
	print(orders)
