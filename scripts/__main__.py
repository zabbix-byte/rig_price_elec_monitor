from datetime import date
from time import time
from .electricity_config import EletricityConfig

import sys
import time
import os

def args():
    t = """
        Made by zabbix

        RIG DOWN, OPTIMIZE YOUR RIG!

        rig_down --zone <PCB/CYM> --price_limit <0.17..> --disount <20>

        --zone:
             PCB: Peninsula, Canarias, Baleares
             CYM: Ceuta y Melilla

        --price_limit:
            0.3, 0.12 etc This is the price of the light you want to close de rigs
        
        --disount
            10, 30, 50 is the % of disount you company is doing you (if you dont have disount put 0)

        """
    if len(sys.argv) < 6:
        print(t)
        exit()

    args_list = ['--zone', '--price_limit', '--disount']
    args_dicts = {}

    for i in range(1, len(sys.argv)):
        if (i % 2) == 0: 
            if detected not in args_list:
                print(t)
                exit()
            args_dicts[detected] = sys.argv[i]
        else: 
            detected = sys.argv[i]
    return args_dicts
    

def main():
    args_dicts = args()
    app_open = True
    
    while app_open:
        check = EletricityConfig(args_dicts['--zone'], float(args_dicts['--price_limit']), int(args_dicts['--disount'])).get_current_hour_price()
        if check != 'ok':
            data = os.popen('miner.py status').read() 
            if 'No' not in data and 'miners' not in data:
                if '[' in data and ']' in data:
                    print('stoping')
                    os.system('miner stop')
        else:
            data = os.popen('miner.py status').read() 
            if 'No' in data and 'miners' in data:
                if '[' not in data and ']' not in data:
                    print('starting')
                    os.system('miner start')

        time.sleep(600)

if __name__ == '__main__':
    main()