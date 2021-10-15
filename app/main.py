import secrets
from umqtt.robust import MQTTClient


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
    

def send_to_mqtt_server(mqtt_client, mqtt_feed, temperature):
    client = MQTTClient(client_id=mqtt_client, server=secrets.mqtt_server, user=secrets.mqtt_username, password=secrets.mqtt_key, ssl=False)
    try:
        client.connect()
        client.publish(mqtt_feed, bytes(str(temperature), 'utf-8'), qos=0)
        client.disconnect()
    except Exception as e:
        print('Failed to connected to MQTT Server with error: {}'.format(e))
        pass


wifi_connect()
mqtt_client_id = bytes('client_'+str(int.from_bytes(os.urandom(3), 'little')), 'utf-8')
mqtt_feedname = bytes('{:s}/feeds/{:s}'.format(secrets.mqtt_username, secrets.mqtt_temperature_topic), 'utf-8')

while True:
    if not wifi.isconnected() == True:
        wifi_connect()
    try:
        if gc.mem_free() < 102000:
            gc.collect()
        temp = read_ds_sensor()
        print(round(temp*(9/5)+32, 2))
        send_to_mqtt_server(mqtt_client_id, mqtt_feedname, temp)
    except OSError as e:
        print(e)
    if not ota.fetch() == True:
        ota.update()
        machine.reset()
    sleep(60)
