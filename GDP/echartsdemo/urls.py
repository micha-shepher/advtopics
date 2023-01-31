from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('populationtable', views.populationtable, name='populationtable'),
    path('popgdp', views.pop_gdp, name='popgdp'),
    path('popgdp/<int:year>', views.pop_gdp, name='popgdpyear'),
    path('popgdpscatter/<int:year>', views.pop_gdp_scatter, name='popgdpscatter'),
    path('popgdpparallel/<str:country_code>/<int:fromyear>/<int:toyear>',
         views.pop_gdp_parallel, name='popgdpparallel'),
]
