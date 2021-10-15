# This file is executed on every boot (including wake-boot from deepsleep)
import esp
esp.osdebug(None)
import uos, machine
#uos.dupterm(None, 1) # disable REPL on UART(0)

import webrepl
webrepl.start()

from time import sleep
import onewire, ds18x20

import network
import gc
gc.collect()

ds_pin = machine.Pin(4)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))

# Senko OTA setup
import senko
github_url = 'https://github.com/Blacknight318/terrarium_sense'
ota = senko.Senko(url=github_url, files=['boot.py', 'main.py'])