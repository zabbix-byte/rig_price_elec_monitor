# ⚡​ RIG DOWN, OPTIMIZE YOUR RIG!
**Works only for HiveOs** | **For Spain**
 
This app stop your miner automatically with the price of electricity ⚡​



#### 🛠️​ **INSTALL**
1. Go in the HiveOs CLI and connect to the rig terminal.
2. clone this repo in the server.
3. check if you have python3
4. execute this command.

    ```sh
    pip3 install --user -e .
     # or
    pip3 install -e .
    ```
5. Run the app
    ```sh
    rig_price_elec_monitor --zone PCB --price_limit 0.17 --disount 0
     # or in background
    rig_price_elec_monitor --zone PCB --price_limit 0.17 --disount 0 &
    ```


**Help message 🗿**

```
rig_down --zone <PCB/CYM> --price_limit <0.17..> --disount <20>

        --zone:
             PCB: Peninsula, Canarias, Baleares
             CYM: Ceuta y Melilla

        --price_limit:
            0.3, 0.12 etc This is the price of the light you want to close de rigs
        
        --disount
            10, 30, 50 is the % of disount you company is doing you (if you dont have disount put 0)
```

