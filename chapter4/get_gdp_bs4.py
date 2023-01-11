import requests
from bs4 import BeautifulSoup


class GDP:
    """mine the https://countryeconomy.com/gdp site for 2022 GDP figures"""

    url = 'https://countryeconomy.com/gdp'

    def __init__(self):
        """

        """
        pass

    def get_gdp(self) -> list:
        """
        Get the gdp values from the page and print them
        :return: None
        """

        r = requests.get(self.url)
        if not r.status_code == 200:
            print(f'could not mine {self.url}')
            return []
        soup = BeautifulSoup(r.content, 'html5lib')
        table = soup.find(attrs={'id': 'tbA'})
        reply = list()
        for row in table.find_all('tr'):
            result = {}
            for i, col in enumerate(row.find_all('td')):
                if i == 0:
                    result['country'] = col.text[:-4]
                elif i == 1:
                    result['year'] = col.text
                elif i == 2:
                    result['gdp'] = col.text
                elif i == 6:
                    result['growth'] = col.text
            if len(result) == 4:
                reply.append(result)
        return reply

