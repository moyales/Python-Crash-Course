#8.5: Cities
#Write a function that accepts the name and country of a city.

def describe_city(name, country = 'the united states'):
	"""Describes the city name and country its in"""
	print(name.title() + " is in " + country.title() + ".")

describe_city('los angeles')
describe_city('new york')
describe_city('tokyo', country = 'japan')


