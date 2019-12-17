def city_country(city, country, population=''):
    '''Take a city name and country name and return formatted version'''
    if population:
        place = city + ', ' + country + " - Population: " + str(population)
    else:
        place = city + ', ' + country
    return place.title()