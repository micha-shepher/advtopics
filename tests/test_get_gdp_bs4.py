from unittest import TestCase
from chapter4.get_gdp_bs4 import GDP


class TestGDP(TestCase):
    def test_get_gdp(self):
        gdp = GDP()
        d = gdp.get_gdp()
        # country, year, euro, hbar, dollar, hbar dollar, growth, hbar,
        try:
            for country in d:
                print(f"{country['country']:40}{country['year']:7}{country['gdp']:>15}{country['growth']:>10}")
        except KeyError:
            pass
        self.assertTrue(isinstance(d, list))
        self.assertTrue(isinstance(d[0], dict))
        self.assertTrue(list(d[0].keys()) == ['country', 'year', 'gdp', 'growth'])

