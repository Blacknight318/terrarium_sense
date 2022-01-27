import onewire, ds18x20


class DS18B20():
    def __init__(self, onewire_pin=4):
        self.ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))
    
    def read_ds_sensor():
        roms = ds_sensor.scan()
        ds_sensor.convert_temp()
        for rom in roms:
            temp = ds_sensor.read_temp(rom)
            if isinstance(temp, float):
                msg = round(temp, 2)
                return msg
            return b'0.0'