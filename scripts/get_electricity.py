import requests
import json

class GetPrices:
    zones = ['PCB', 'CYM']

    def __init__(self, zone) -> None:
        if zone not in self.zones: print('Only PCB or CYM are accepted'); exit()
        self._zone = zone
    
    def get_json(self):
        data = requests.get(f'https://api.preciodelaluz.org/v1/prices/all?zone={self._zone}')
        if data.status_code == 200: data = json.loads(data.content); return data;
        else: print('Some error in get the price of light'); exit()


