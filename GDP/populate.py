import csv
import json
import os
from django import setup
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GDP.settings')
setup()

from gdp_app.models import (Country, Region, Indicator, Gdp, )

import datetime

class Populate:
    """
    Populate the db with some indicator data
    """
    indicators = ('Population', 'GDP', 'GDP(PPP)', 'Fertility',)
    regions = ('Asia', 'Europe', 'North America', 'South America', 'Africa', 'Oceania', )
    gdp_file = 'data/gdp.json'
    population_csv = 'data/population.csv'
    population_json = 'data/population.json'
    country_file = 'data/country.json'

    def __init__(self):
        """
        read some stuff from json files and set the internal data structures
        """
        with open(self.country_file) as f:
            self.countries = json.load(f)

        with open(self.gdp_file) as f:
            self.values = json.load(f)

    def convert_population_to_json(self) -> None:
        """
        Downloaded the population file as csv, want it as json
        :return: None
        """

        data = dict()
        with open(self.population_csv) as f:
            reader = csv.DictReader(f)
            for row in reader:
                id = row['Country Code']
                data[id] = row
        with open(self.population_json, 'w') as f:
            json.dump(data, f)

    def populate(self) -> None:
        """
        Push regions, countries, indicators and values
        :return: Nothing
        """
        # populate region
        for region in self.regions:
            if not Region.objects.filter(name=region).exists():
                r = Region(name=region)
                r.save()

        # populate country
        for country in self.countries:
            code = country['cca3']
            if not Country.objects.filter(abbr=code).exists():
                c = Country(name=country['country'], abbr=code,
                            region=Region.objects.get(name=country['region']))
                c.save()

        # populate indicators
        for ind in self.indicators:
            if not Indicator.objects.filter(name=ind).exists():
                i = Indicator(name=ind)
                i.save()

        # populate gdp & population
        for val in self.values:
            if Country.objects.filter(abbr=val['Country Code']).exists():
                country = Country.objects.get(abbr=val['Country Code'])
                ind = Indicator.objects.get(name='GDP')
                pop = Indicator.objects.get(name='Population')
                # gdp
                if not Gdp.objects.filter(country=country,
                                          indicator=ind,
                                          year=val['Year']).exists():
                    gdp = Gdp(country=country, indicator=ind, year=val['Year'], value=val['Value'])
                    gdp.save()
                # population
                if not Gdp.objects.filter(country=country,
                                          indicator=pop,
                                          year=val['Year']).exists():
                    gdp = Gdp(country=country, indicator=pop, year=val['Year'], value=val['Value'])
                    gdp.save()





if __name__ == '__main__':
    p = Populate()
    p.populate()
