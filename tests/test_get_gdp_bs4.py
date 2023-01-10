from unittest import TestCase
from chapter4.get_gdp_bs4 import GDP


class TestGDP(TestCase):
    def test_get_gdp(self):
        gdp = GDP()
        d = gdp.get_gdp()
        # country, year, euro, hbar, dollar, hbar dollar, growth, hbar,
        self.assertTrue(isinstance(d, list))
        self.assertTrue(isinstance(d[0], dict))
        self.assertTrue(list(d[0].keys()) == ['country', 'year', 'gdp', 'growth'])

