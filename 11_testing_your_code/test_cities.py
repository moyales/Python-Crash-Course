import unittest
from city_functions import city_country

class TestCityCountry(unittest.TestCase):
    def test_city_country(self):
        place = city_country('montreal', 'quebec')
        self.assertEqual(place, "Montreal, Quebec")

    def test_city_country_pop(self):
        place = city_country('chicago', 'illinois', 4000000)
        self.assertEqual(place, "Chicago, Illinois - Population: 4000000")

unittest.main()