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

class ValueSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Gdp
