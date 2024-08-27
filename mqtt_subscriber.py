import paho.mqtt.client as mqtt

# Supress warnings
import warnings
warnings.filterwarnings("ignore")

# IP-Address of broker (Raspberry Pi)
MQTT_SERVER = "clt-lab-w-1979"

# Topic names
MQTT_TEMP = "sensor/temp"
MQTT_HUMI = "sensor/humi"
MQTT_PRES = "sensor/pres"

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    # Subscribing in on_connect() means that if we lose the connection
    # and reconnect then subscriptions will be renewed.
    client.subscribe(MQTT_TEMP)
    client.subscribe(MQTT_HUMI)
    client.subscribe(MQTT_PRES)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    msg = str(msg.topic) + " " + str(msg.payload)[2:-1]
    print(msg)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_SERVER, 1883, 60)

# Loop
client.loop_forever()
