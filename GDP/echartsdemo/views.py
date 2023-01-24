from operator import itemgetter

from jinja2 import Environment, FileSystemLoader
from pyecharts.globals import CurrentConfig
from django.http import HttpResponse

from gdp_app.models import Gdp, Indicator, Country

CurrentConfig.GLOBAL_ENV = Environment(loader=FileSystemLoader("./echartsdemo/templates"))

from pyecharts import options as opts
from pyecharts.charts import Bar, Scatter

from pyecharts.components import Table
from pyecharts.options import ComponentTitleOpts

def index(request):
    c = (
        Bar()
        .add_xaxis(["ondergoed", "fleece", "cotton", "short pants", "bikini"])
        .add_yaxis("Mega store", [5, 20, 36, 10, 75, 90])
        .add_yaxis("Mini store", [15, 25, 16, 55, 48, 8])
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-title", subtitle="I like icecream"))
    )
    return HttpResponse(c.render_embed())



def populationtable(request):
    table = Table()

    headers = ["City name", "Area", "Population", "Annual Rainfall"]
    rows = [
        ["Brisbane", 5905, 1857594, 1146.4],
        ["Adelaide", 1295, 1158259, 600.5],
        ["Darwin", 112, 120900, 1714.7],
        ["Hobart", 1357, 205556, 619.5],
        ["Sydney", 2058, 4336374, 1214.8],
        ["Melbourne", 1566, 3806092, 646.9],
        ["Perth", 5386, 1554769, 869.4],
    ]
    table.add(headers, rows)
    table.set_global_opts(
        title_opts=ComponentTitleOpts(title="Population GDP table", subtitle="country population and GDP")
    )
    return HttpResponse(table.render_embed())

def pop_gdp(request, year=2010):
    """
    Tabulate the richest countries for population, GDP and GDP per capita. Then sort
    table according to GDP per capita.

    Countries that do not have both GDP and population in the database for a specific year
    are not included.
    :param request:
    :param year:
    :return:
    """
    table = Table()

    headers = ["Country", "Population(millions)", "GDP (millions)", "GDP per capita"]
    rows = []
    pop_ind = Indicator.objects.get(desc='Population')
    gdp_ind = Indicator.objects.get(desc='GDP')
    population = Gdp.objects.filter(indicator=pop_ind, year=year)
    gdp = Gdp.objects.filter(indicator=gdp_ind, year=year, value__gte=300000000000).order_by('-value')

    for g in gdp:
        try:
            pop = population.filter(country=g.country).first().value
            row = [g.country.name, f'{pop / 1000000:.2f}',
                   f'$ {round(g.value / 1000000, 2):,}', round(g.value / pop, 2)]
            rows.append(row)
        except AttributeError:
            print(f'{g.country} does not have a population for year {g.year}')

    table.add(headers=headers, rows=sorted(rows, key=itemgetter(3), reverse=True))
    table.set_global_opts(
        title_opts=ComponentTitleOpts(title=f"Population GDP table {year}",
                                      subtitle=f"country population and GDP ({year})")
    )
    return HttpResponse(table.render_embed())


def pop_gdp_scatter(request, year=2010):
    """
    scatter the richest countries for population, GDP and GDP per capita.

    Countries that do not have both GDP and population in the database for a specific year
    are not included.
    :param request:
    :param year:
    :return:
    """

    rows = []
    pop_ind = Indicator.objects.get(desc='Population')
    gdp_ind = Indicator.objects.get(desc='GDP')
    population = Gdp.objects.filter(indicator=pop_ind, year=year)
    gdp = Gdp.objects.filter(indicator=gdp_ind, year=year, value__gte=200000000000).order_by('-value')

    for g in gdp:
        try:
            pop = population.filter(country=g.country).first().value
            row = [g.country.name, pop / 1000000,
                   round(g.value / 1000000), round(g.value / pop, 2)]
            rows.append(row)
        except AttributeError:
            print(f'{g.country} does not have a population for year {g.year}')
    c = (
        Scatter()
            .add_xaxis([x[0] for x in rows])
            # .add_yaxis("GDP", [x[2] for x in rows])
            .add_yaxis("GDP per capita", [x[3] for x in rows])
            .set_global_opts(
            title_opts=opts.TitleOpts(title="Scatter-VisualMap(Size)"),
        )
    )

    return HttpResponse(c.render_embed())

