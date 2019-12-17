#8.14 Cars

# Write a function that stores information about a car in a dictionary
# Should always recieve a manufacturer and model name.
# Then accept an arbitrary number of keyword arguments

def make_car(make, model, **options):
	"""Creates dictionary about a car and its features"""
	car_info = {}
	car_info['make'] = make
	car_info['model'] = model
	
	for key, value in options.items():
		car_info[key] = value
	
	return car_info

my_car = make_car('acura', 'tlx', color = 'white', lux_package = True)
print(my_car)
