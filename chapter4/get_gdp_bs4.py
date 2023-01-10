import requests
from bs4 import BeautifulSoup


class GDP:
    """mine the https://countryeconomy.com/gdp site for 2022 GDP figures"""

    url = 'https://countryeconomy.com/gdp'

    def __init__(self):
        """

        """
        pass

    def get_gdp(self) -> None:
        """
        Get the gdp values from the page and print them
        :return: None
        """

        r = requests.get(self.url)
        if not r.status_code == 200:
            print(f'could not mine {self.url}')
            return
        soup = BeautifulSoup(r.content, 'html5lib')
        table = soup.find(attrs={'id': 't'})