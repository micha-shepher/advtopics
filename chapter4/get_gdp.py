import json
import locale
import webbrowser
from typing import List, Dict

import requests


class GetGdp:
    url = "https://pkgstore.datahub.io/core/gdp/gdp_json/data/1a2503aa36368933be8f9a96e1dc16de/gdp_json.json"

    def __init__(self):
        """
        Bookkeeping stuff,
        1. determine where chrome resides
        2. set the locale to sane
        """
        self.chrome_path_windows = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        self.chrome_path_linux = '/usr/bin/google-chrome %s'
        self.chrome_path_mac = 'open -a /Applications/Google\ Chrome.app %s'
        import platform
        sss = platform.system()
        if sss == 'Darwin':
            self.chrome_path = self.chrome_path_mac
        elif sss == 'Windows':
            self.chrome_path = self.chrome_path_windows
        else:
            self.chrome_path = self.chrome_path_linux
        self.browser = webbrowser.get(self.chrome_path)

        locale.setlocale(locale.LC_ALL, 'en_CA.UTF-8')

    def get_gdp_json(self):
        """
        get the json file from the databank server
        :return: json file containing the global gdp table
        """

        headers = {'Accept': 'application/json'}

        response = requests.get(self.url, headers=headers)
        if response.status_code == 200:
            js = response.json()
            return js
        else:
            print(f"could not get json file from url")
            return response.status_code

    def save_gdp_json(self, table: List[Dict]):
        """
        save table as json file
        :param table:
        :return: None
        """
        with open('/tmp/gdp.json', 'w') as f:
            json.dump(table, f)

    def render_gdp_table(self, table: List[Dict]) -> str:
        """
        render the json table as an HTML table
        :param table: json list of dicts with keys 'Country Code', 'Country Name', 'Value', 'Year'
        :return: html table containing the gdp data
        """
        result = '<HTML><BODY><TABLE>{header}{content}</TABLE></BODY></HTML>'
        header = '<tr><th>Country Name</th><th>Country Code</th>' \
                 '<th>Value(million$)</th><th>Year</th></tr>'
        content = ''
        for country in table:
            money = locale.currency(country["Value"]/10e6, grouping=True)
            row = f'<tr><td>{country["Country Name"]}</td>' \
                  f'<td>{country["Country Code"]}</td>'\
                  f'<td>{money}</td>'\
                  f'<td>{country["Year"]}'
            content += row
        return result.format(content=content, header=header)

    def save_gdp_html(self, html: str):
        """save the html file in the tmp directory and pop a chrome tab
        """
        thehtml = '/tmp/gdp.html'
        with open(thehtml, 'w') as f:
            f.write(html)
        self.browser.open_new_tab(thehtml)



if __name__ == '__main__':
    gdp_processor = GetGdp()
    js = gdp_processor.get_gdp_json()
    gdp_processor.save_gdp_json(js)


    # gdp_processor.save_gdp_html(gdp_processor.render_gdp_table(js))