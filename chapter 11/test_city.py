from city_functions import citi_functions

import unittest


class NameTestCase(unittest.TestCase):
    def test_city_country(self):
        city_country_name = citi_functions('china', 'nanjing')
        self.assertEqual(city_country_name, 'Nanjing, China')

    def test_city_country_population(self):
        city_country_population_name = citi_functions('china', 'nanjing', '5000000')
        self.assertEqual(city_country_population_name, 'Nanjing, China - population 5000000')

if __name__ == '__main__':
    unittest.main()

