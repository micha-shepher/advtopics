from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('populationtable', views.populationtable, name='populationtable'),
    path('popgdp', views.pop_gdp, name='popgdp'),
]
