import paho.mqtt.publish as publish
from sense_hat import SenseHat
import time

sense = SenseHat()

# IP-Address of broker (Raspberry Pi)
MQTT_SERVER = "clt-lab-w-1979"

# Topic names
MQTT_TEMP   = "sensor/temp"
MQTT_HUMI   = "sensor/humi"
MQTT_PRES   = "sensor/pres"

def read_temp():
    t = sense.get_temperature()
    t = round(t,2)
    return t

def read_humidity():
    h = sense.get_humidity()
    h = round(h,2)
    return h

def read_pressure():
    p = sense.get_pressure()
    p = round(p,2)
    return p

temp = float(read_temp())
humi = float(read_humidity())
pres = float(read_pressure())

while True:
    publish.single(MQTT_TEMP, temp, hostname=MQTT_SERVER)
    time.sleep(0.5)
    publish.single(MQTT_HUMI, humi, hostname=MQTT_SERVER)
    time.sleep(0.5)
    publish.single(MQTT_PRES, pres, hostname=MQTT_SERVER)
    time.sleep(0.5)
