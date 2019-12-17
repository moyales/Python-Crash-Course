#8.6: City Names
#Write a function called city_country() that takes in the name
# of a city and its country.

def city_country(city, country):
	"""Takes the name of a city, and the country its in"""
	c_country = city + ", " + country
	return c_country.title()

place = city_country('new york', 'united states')
print(place)

other_place = city_country('paris', 'france')
print(other_place)

another_place = city_country('montreal', 'canada')
print(another_place)
