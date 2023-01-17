from rest_framework import viewsets
from rest_framework import permissions

from .models import Country, Region, Gdp, Indicator
from .serializers import (CountrySerializer,
                          ValueSerializer, RegionSerializer, IndicatorSerializer)


class CountryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [permissions.IsAuthenticated]


class RegionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    permission_classes = [permissions.IsAuthenticated]



class IndicatorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Indicator.objects.all()
    serializer_class = IndicatorSerializer
    permission_classes = [permissions.IsAuthenticated]



class ValueViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Gdp.objects.all().order_by('country', 'indicator')
    serializer_class = ValueSerializer
    permission_classes = [permissions.IsAuthenticated]

