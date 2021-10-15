# This file is executed on every boot (including wake-boot from deepsleep)
import esp
import os
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

# Senko OTA setup, see https://github.com/RangerDigital/senko
import senko
github_url = 'https://github.com/Blacknight318/terrarium_sense'
ota = senko.Senko(user='Blacknight318', repo='terrarium_sense',  working_dir='app', files=['boot.py', 'main.py'])