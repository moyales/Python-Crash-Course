def make_pizza(size, *toppings):
	"""Summarise the pizza about to be made."""
	if len(toppings) == 1:
		print("\nMaking a " + str(size) +
		      "-inch pizza with the following topping:")
		for topping in toppings:
			print("- " + topping)
	else:
		print("\nMaking a " + str(size) +
		      "-inch pizza with the following toppings:")
		for topping in toppings:
			print("- " + topping)
