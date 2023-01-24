from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'countries', views.CountryViewSet)
router.register(r'regions', views.RegionViewSet)
router.register(r'values', views.ValueViewSet)
router.register(r'indicators', views.IndicatorViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('countrylist/', views.CountryViewSet.as_view({'get': 'list'}), name='country-list'),
]