from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=50)
    abbr = models.CharField(max_length=10)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Indicator(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Gdp(models.Model):
    indicator = models.ForeignKey(Indicator, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    year = models.DecimalField(max_digits=4, decimal_places=0, choices=zip(range(1950, 2025), range(1950, 2025)))
    value = models.DecimalField(max_digits=18, decimal_places=2)

    def __str__(self):
        return f'{self.country}-{self.year}-{self.indicator}: {self.value}'
