# Terrarium Sensor Project

## Introduction
This project  is intended to be used to monitor terrariums for temperature and humidity and then send those values to an MQTT broker or server(like AdafruitIO). I'm starting up with a DS18B20 and will be adding the DHT22 as well as the SHT30. This code is being tested on a ESP8266 board but should also work on an ESP32.

## The Parts List
1. [ESP8266/NodeMCU ESP8266 board](https://www.amazon.com/HiLetgo-Internet-Development-Wireless-Micropython/dp/B081CSJV2V/ref=sr_1_3?crid=3SKV9DCZXU4TP&dchild=1&keywords=hiletgo%2Besp8266&qid=1634325032&sprefix=hiletgo%2B%2Caps%2C618&sr=8-3&th=1)
2. [DS18B20 Temperature Sensor](https://www.amazon.com/HiLetgo-DS18B20-Temperature-Stainless-Waterproof/dp/B00M1PM55K/ref=sr_1_3?dchild=1&keywords=ds18b20&qid=1634325126&sr=8-3)
3. [Optional: .1" pitch Screw Terminal](https://www.amazon.com/KeeYees-60pcs-Terminal-Connector-Arduino/dp/B07H5G7GC6/ref=sr_1_24?dchild=1&keywords=.1+pitch+screw+terminal&qid=1634325225&sr=8-24)
4. [Jumper wires](https://www.amazon.com/Solderless-Flexible-Breadboard-Jumper-100pcs/dp/B005TZJ0AM/ref=sr_1_15?dchild=1&keywords=jumper%2Bwires&qid=1634325264&sr=8-15&th=1)
   * [Or these](https://www.amazon.com/IZOKEE-Solderless-Breadboard-Arduino-Project/dp/B08151TQHG/ref=sr_1_6?dchild=1&keywords=jumper+wires&qid=1634325335&sr=8-6)
5. [Optional: Breadboard](https://www.amazon.com/Pcs-MCIGICM-Points-Solderless-Breadboard/dp/B07PCJP9DY/ref=sr_1_5?dchild=1&keywords=breadboard&qid=1634325446&sr=8-5)

## Required Micropython Libraries
1. [Senko](https://github.com/RangerDigital/senko)
   * You will need to copy the contents of senko.py to a senko.py file on your ESP micro
2. [micropython-umqtt.simple](https://github.com/micropython/micropython-lib/tree/master/micropython/umqtt.simple)
   * You can install with the REPL with the following commands:
     ```
     import upip
     upip.install('micropython-umqtt.simple')
        ```
3. [micropython-umqtt.robust](https://github.com/micropython/micropython-lib/tree/master/micropython/umqtt.robust)
   * You can install this from the REPL as well wihth the following commands:
     ```
     import upip
     upip.install('micropython-umqtt.robust')
     ```
4. You will also want [Thonmny](https://thonny.org/) to flash the initial [Micrpython Image](https://micropython.org/download/esp8266/) and load up the filles from the app folder.