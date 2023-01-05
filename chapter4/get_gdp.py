import requests
import json


class GetGdp:
    url = "https://pkgstore.datahub.io/core/gdp/gdp_json/data/1a2503aa36368933be8f9a96e1dc16de/gdp_json.json"

    def __init__(self):
        pass

    def get_gdp_json(self):
        """
        get the json file from the databank server
        :return: json file containing the global gdp table
        """

        headers = {'Accept': 'application/json'}

        response = requests.get(self.url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"could not get json file from url")
            return response.status_code


if __name__ == '__main__':
    gdp_processor = GetGdp()
    print(gdp_processor.get_gdp_json())