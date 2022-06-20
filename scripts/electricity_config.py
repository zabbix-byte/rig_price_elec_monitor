
from .get_electricity import GetPrices

import datetime

class EletricityConfig(GetPrices):
    def __init__(self, zone, limit_price, disount) -> None:
        super().__init__(zone)
        self._data = self.get_json()
        self._converted_data = {}
        self._current_hour = datetime.datetime.utcnow().hour+2
        self._current_minute = datetime.datetime.utcnow().minute
        self._limit_pice = limit_price

        for i in self._data:
             self._converted_data[self._data[i]['hour']] = (float(self._data[i]['price'])/1000) - ((float(self._data[i]['price'])/1000) * (disount/100))
        
    
    def get_current_hour_price(self):
        for i in self._converted_data:
            if int(i.split('-')[0]) == self._current_hour:
                if self._limit_pice < self._converted_data[i]:
                    return self._converted_data[i]
        return 'ok'
