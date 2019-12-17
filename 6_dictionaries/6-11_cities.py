#6.11: Cities
#Make a dictionary called "cities".
#Create a dictionary about each city - country, population, fact

cities = {
	'new york' : {
		'country' : 'united states',
		'population' : 8623000,
		'fact' : 'The first pizzeria in the US opened here in 1895.'
		},
	'montreal' : {
		'country' : 'canada',
		'population' : 1780000,
		'fact' : 'The second largest French-speaking city in the world.'
		},
	'london' : {
		'country' : 'united kingdom',
		'population' : 8787892,
		'fact' : "Has the world's oldest/first underground metro."
		}
	}

for city, info in cities.items():
	print("City: " + city.title())
	country = info['country']
	population = info['population']
	fact = info['fact']
	
	print("\tCountry: " + country.title())
	print("\tPopulation: " + str(population))
	print("\tFact: " + fact + "\n")
