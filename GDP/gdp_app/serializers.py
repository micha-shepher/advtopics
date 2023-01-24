from rest_framework import serializers

from gdp_app.models import (Country, Region, Indicator, Gdp, )


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'

class IndicatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indicator
        fields = '__all__'

class ValueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = '__all__'
        model = Gdp

class PopulationSerializer(serializers.Serializer):
    country = serializers.CharField()
    region = serializers.CharField()
    population = serializers.DecimalField(decimal_places=0, max_digits=12)
