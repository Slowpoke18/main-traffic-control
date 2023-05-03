from machine import Pin, PWM
import network
import time
from umqtt.robust import MQTTClient
import sys
import utime
led = Pin("LED",Pin.OUT)
pwm1 = PWM(Pin(0))
pwm2 = PWM(Pin(1))
pwm3 = PWM(Pin(3))
pwm4 = PWM(Pin(4))
pwm.freq(50)

WIFI_SSID = 'Redmi Note 9 Pro'
WIFI_PASSWORD = '0987654321'

mqtt_client_id = bytes('client_'+'123', 'utf-8') # Just a random client ID

ADAFRUIT_IO_URL = 'io.adafruit.com'  	# Your Adafruit IO credentials
ADAFRUIT_USERNAME = '_slowpoke18'
ADAFRUIT_IO_KEY = 'aio_JGIf55pBMLJQRDzSogyurolAS1K4'

TOGGLE_FEED_ID = 'onboardled'
CLAW_FEED_ID = 'claw'
DIRECTION_FEED_ID = 'direction'
DISTANCE_FEED_ID = 'distance'
HEIGHT_FEED_ID = 'height'

def connect_wifi():# function for connecting your wifi
    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)
    wifi.disconnect()
    wifi.connect(WIFI_SSID,WIFI_PASSWORD)
    if not wifi.isconnected():
        print('connecting..')
        timeout = 0
        while (not wifi.isconnected() and timeout < 15):
            print(15 - timeout)
            timeout = timeout + 1
            time.sleep(1)
    if(wifi.isconnected()):
        print('connected')
    else:
        print('not connected')
        sys.exit()

connect_wifi() # Connecting to WiFi 

client = MQTTClient(client_id=mqtt_client_id,
                    server=ADAFRUIT_IO_URL,
                    user=ADAFRUIT_USERNAME,
                    password=ADAFRUIT_IO_KEY,
                    ssl=False)

try:
    client.connect()				# Connect to MQTT server
except Exception as e:
    print('could not connect to MQTT server {}{}'.format(type(e).name, e))
    sys.exit()

def cb(topic, msg):
    print('Received Data:  Topic = {}, Msg = {}'.format(topic, msg))
    # Parse the slider value from the message payload
    slider_value1 = int(msg.decode())
    pwm1.duty_ns(slider_value1)
    time.sleep(1)
    print('Received Data:  Topic = {}, Msg = {}'.format(topic, msg))
    # Parse the slider value from the message payload
    slider_value2 = int(msg.decode())
    pwm2.duty_ns(slider_value2)
    time.sleep(1)
    print('Received Data:  Topic = {}, Msg = {}'.format(topic, msg))
    # Parse the slider value from the message payload
    slider_value3 = int(msg.decode())
    pwm3.duty_ns(slider_value3)
    time.sleep(1)
    print('Received Data:  Topic = {}, Msg = {}'.format(topic, msg))
    # Parse the slider value from the message payload
    slider_value4 = int(msg.decode())
    pwm4.duty_ns(slider_value4)
    time.sleep(1)
    print('Received Data:  Topic = {}, Msg = {}'.format(topic, msg))
    recieved_data = str(msg,'utf-8')
    if recieved_data=="0":
        led.value(0)
    if recieved_data=="1":
        led.value(1)

toggle_feed = bytes('{:s}/feeds/{:s}'.format(ADAFRUIT_USERNAME, TOGGLE_FEED_ID), 'utf-8')
claw_feed = bytes('{:s}/feeds/{:s}'.format(ADAFRUIT_USERNAME, CLAW_FEED_ID), 'utf-8')
distance_feed = bytes('{:s}/feeds/{:s}'.format(ADAFRUIT_USERNAME, DISTANCE_FEED_ID), 'utf-8')
direction_feed = bytes('{:s}/feeds/{:s}'.format(ADAFRUIT_USERNAME, DIRECTION_FEED_ID), 'utf-8')
height_feed = bytes('{:s}/feeds/{:s}'.format(ADAFRUIT_USERNAME, HEIGHT_FEED_ID), 'utf-8')# format – usesrname/feeds/led  
client.set_callback(cb)# Callback function               
client.subscribe(toggle_feed)
client.subscribe(claw_feed)
client.subscribe(distance_feed)
client.subscribe(direction_feed)
client.subscribe(height_feed)# Subscribing to particular topic

while True:
    try:
        client.check_msg()# non blocking function
    except:
        client.disconnect()
        sys.exit()
