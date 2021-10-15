import secrets

def read_ds_sensor():
    roms = ds_sensor.scan()
    ds_sensor.convert_temp()
    for rom in roms:
        temp = ds_sensor.read_temp(rom)
        if isinstance(temp, float):
            msg = round(temp, 2)
            return msg
        return b'0.0'
    

def wifi_connect():
    wifi = network.WLAN(network.STA_IF)
    if not wifi.isconnected():
        print('connecting to wireless ', secrets.ssid)
        wifi.active(True)
        wifi.connect(secrets.ssid, secrets.wifi_pass)
        while not wifi.isconnected():
            pass
    print('Network ip info: ', wifi.ifconfig())

wifi_connect()
while True:
    try:
        if gc.mem_free() < 102000:
            gc.collect()
        temp = read_ds_sensor()
        print(round(temp*(9/5)+32, 2))
    except OSError as e:
        print(e)
    sleep(60)
