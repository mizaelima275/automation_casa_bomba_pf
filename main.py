import time
from machine import Pin, Timer # type: ignore
from onewire import OneWire # type: ignore
from ds18x20 import DS18X20 # type: ignore
from umqtt.robust import MQTTClient # type: ignore
import network # type: ignore
import json
import config

# Conecta ao Wi-Fi
def connect_wifi():
    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect(config.ssid, config.password)
    while not station.isconnected():
        pass
    print('Conexão Wi-Fi estabelecida')

# Função para ler a temperatura dos sensores DS18B20
def read_temperature(pin):
    ow = OneWire(Pin(pin))
    ds = DS18X20(ow)
    roms = ds.scan()
    ds.convert_temp()
    time.sleep_ms(750)
    for rom in roms:
        temp = ds.read_temp(rom)
        if isinstance(temp, float):
            return round(temp, 1)  # Arredonda para uma casa decimal

# Função para ler o estado do fluxostato
def read_flow_state(pin):
    flow_pin = Pin(pin, Pin.IN)
    return flow_pin.value()

# Função para publicar os dados via MQTT
def publish_data(client):
    temperature_1 = read_temperature(config.ds18b20_pin_1)
    temperature_2 = read_temperature(config.ds18b20_pin_2)
    flow_state = read_flow_state(config.flow_pin)

    data = {
        'Sensores': {
            'Sensor1': {
                'temperatura': temperature_1
            },
            'Sensor2': {
                'temperatura': temperature_2
            }
        },
        'fluxostato': flow_state
    }
    client.publish(config.topic, json.dumps(data))
    print(data)

# Função principal
def main():
    connect_wifi()
    client = MQTTClient(config.client_id, config.mqtt_server, config.mqtt_port, config.mqtt_user, config.mqtt_password)
    client.connect()
    print('Conectado ao broker MQTT')

    timer = Timer(-1)
    timer.init(period=10000, mode=Timer.PERIODIC, callback=lambda t: publish_data(client))

try:
    main()
except KeyboardInterrupt:
    print('Desconectado...')