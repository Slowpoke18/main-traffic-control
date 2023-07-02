from machine import Pin, PWM
import network
import time
from umqtt.robust import MQTTClient
from mfrc522 import MFRC522
import sys
import utime
# Configure RFID1
reader1 = MFRC522(spi_id=0, sck=6, miso=4, mosi=7, cs=5, rst=22)

# Configure RFID2
reader2 = MFRC522(spi_id=0, sck=6, miso=4, mosi=7, cs=10, rst=21)


green1 = Pin(2,Pin.OUT)
yellow1 = Pin(3,Pin.OUT)
red1 = Pin(11,Pin.OUT)
green2 = Pin(8,Pin.OUT)
yellow2 = Pin(9,Pin.OUT)
red2 = Pin(18,Pin.OUT)
green3 = Pin(15,Pin.OUT)
yellow3 = Pin(16,Pin.OUT)
red3 = Pin(17,Pin.OUT)


WIFI_SSID = 'Redmi Note 9 Pro'
WIFI_PASSWORD = '0987654321'

mqtt_client_id = bytes('client_'+'123', 'utf-8') # Just a random client ID

ADAFRUIT_IO_URL = 'io.adafruit.com'  	# Your Adafruit IO credentials
ADAFRUIT_USERNAME = '_slowpoke18'
ADAFRUIT_IO_KEY = 'API_KEY'


LANE_1_ID = 'lane1vehiclecount'
LANE_2_ID = 'lane2vehiclecount'
LANE_3_ID = 'lane3vehiclecount'

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
    client.connect()
except Exception as e:
    print('could not connect to MQTT server {}{}'.format(type(e)._name_, e))
    sys.exit()

def cb(topic, msg):
    received_data = str(msg,'utf-8')
    mes = int(msg.decode())
    if topic == b'_slowpoke18/feeds/lane1vehiclecount':
       print('Received Data for lane 1 vehicle count:  Topic = {}, Msg = {}'.format(topic, msg))
       green1.value(1)
       yellow1.value(0)
       red1.value(0)
       green2.value(0)
       yellow2.value(0)
       red2.value(1)
       green3.value(0)
       yellow3.value(0)
       red3.value(1)
       utime.sleep_ms(mes*1000)
       reader1.init()
       (stat1, tag_type1) = reader1.request(reader1.REQIDL)
       if stat1 == reader1.OK:
           (stat1, uid1) = reader1.SelectTagSN()
           if stat1 == reader1.OK:
               card1 = int.from_bytes(bytes(uid1), "little", False)
               print("RFID1 - CARD ID: " + str(card1))
               if card1 == 2890929491:
                   green1.value(1)
                   yellow1.value(0)
                   red1.value(0)
                   green2.value(0)
                   yellow2.value(0)
                   red2.value(1)
                   green3.value(0)
                   yellow3.value(0)
                   red3.value(1)
                   print("Emergency vehicle has entered the road!!!!!")
                   print("Halting normal operation!!!")
                   while True:
                       reader2.init()
                       (stat2, tag_type2) = reader2.request(reader2.REQIDL)
                       if stat2 == reader2.OK:
                           (stat2, uid2) = reader2.SelectTagSN()
                           if stat2 == reader2.OK:
                               card2 = int.from_bytes(bytes(uid2), "little", False)
                               print("RFID2 - CARD ID: " + str(card2))
                               if card2 == 2890929491:
                                   print("Emergency vehicle has left the road!!!!!")
                                   print("Resuming normal operation!!!")
                                   green1.value(0)
                                   break  
       green1.value(0)
       yellow1.value(1)
       utime.sleep_ms(2000)
       reader1.init()
       (stat1, tag_type1) = reader1.request(reader1.REQIDL)
       if stat1 == reader1.OK:
           (stat1, uid1) = reader1.SelectTagSN()
           if stat1 == reader1.OK:
               card1 = int.from_bytes(bytes(uid1), "little", False)
               print("RFID1 - CARD ID: " + str(card1))
               if card1 == 2890929491:
                   green1.value(1)
                   yellow1.value(0)
                   red1.value(0)
                   green2.value(0)
                   yellow2.value(0)
                   red2.value(1)
                   green3.value(0)
                   yellow3.value(0)
                   red3.value(1)
                   print("Emergency vehicle has entered the road!!!!!")
                   print("Halting normal operation!!!")
                   while True:
                       reader2.init()
                       (stat2, tag_type2) = reader2.request(reader2.REQIDL)
                       if stat2 == reader2.OK:
                           (stat2, uid2) = reader2.SelectTagSN()
                           if stat2 == reader2.OK:
                               card2 = int.from_bytes(bytes(uid2), "little", False)
                               print("RFID2 - CARD ID: " + str(card2))
                               if card2 == 2890929491:
                                   print("Emergency vehicle has left the road!!!!!")
                                   print("Resuming normal operation!!!")
                                   green1.value(0)
                                   break  
    elif topic == b'_slowpoke18/feeds/lane2vehiclecount':
       print('Received Data for lane 2 vehicle count:  Topic = {}, Msg = {}'.format(topic, msg))
       green1.value(0)
       yellow1.value(0)
       red1.value(1)
       green2.value(1)
       yellow2.value(0)
       red2.value(0)
       green3.value(0)
       yellow3.value(0)
       red3.value(1)
       utime.sleep_ms(mes*1000)
       reader1.init()
       (stat1, tag_type1) = reader1.request(reader1.REQIDL)
       if stat1 == reader1.OK:
           (stat1, uid1) = reader1.SelectTagSN()
           if stat1 == reader1.OK:
               card1 = int.from_bytes(bytes(uid1), "little", False)
               print("RFID1 - CARD ID: " + str(card1))
               if card1 == 2890929491:
                   green1.value(1)
                   yellow1.value(0)
                   red1.value(0)
                   green2.value(0)
                   yellow2.value(0)
                   red2.value(1)
                   green3.value(0)
                   yellow3.value(0)
                   red3.value(1)
                   print("Emergency vehicle has entered the road!!!!!")
                   print("Halting normal operation!!!")
                   while True:
                       reader2.init()
                       (stat2, tag_type2) = reader2.request(reader2.REQIDL)
                       if stat2 == reader2.OK:
                           (stat2, uid2) = reader2.SelectTagSN()
                           if stat2 == reader2.OK:
                               card2 = int.from_bytes(bytes(uid2), "little", False)
                               print("RFID2 - CARD ID: " + str(card2))
                               if card2 == 2890929491:
                                   print("Emergency vehicle has left the road!!!!!")
                                   print("Resuming normal operation!!!")
                                   green1.value(0)
                                   red1.value(1)
                                   red2.value(0)
                                   break  
       green2.value(0)
       yellow2.value(1)
       utime.sleep_ms(2000)
       reader1.init()
       (stat1, tag_type1) = reader1.request(reader1.REQIDL)
       if stat1 == reader1.OK:
           (stat1, uid1) = reader1.SelectTagSN()
           if stat1 == reader1.OK:
               card1 = int.from_bytes(bytes(uid1), "little", False)
               print("RFID1 - CARD ID: " + str(card1))
               if card1 == 2890929491:
                   green1.value(1)
                   yellow1.value(0)
                   red1.value(0)
                   green2.value(0)
                   yellow2.value(0)
                   red2.value(1)
                   green3.value(0)
                   yellow3.value(0)
                   red3.value(1)
                   print("Emergency vehicle has entered the road!!!!!")
                   print("Halting normal operation!!!")
                   while True:
                       reader2.init()
                       (stat2, tag_type2) = reader2.request(reader2.REQIDL)
                       if stat2 == reader2.OK:
                           (stat2, uid2) = reader2.SelectTagSN()
                           if stat2 == reader2.OK:
                               card2 = int.from_bytes(bytes(uid2), "little", False)
                               print("RFID2 - CARD ID: " + str(card2))
                               if card2 == 2890929491:
                                   print("Emergency vehicle has left the road!!!!!")
                                   print("Resuming normal operation!!!")
                                   green1.value(0)
                                   red1.value(1)
                                   break  
       
    
    elif topic == b'_slowpoke18/feeds/lane3vehiclecount':
       print('Received Data for lane 3 vehicle count:  Topic = {}, Msg = {}'.format(topic, msg))
       green1.value(0)
       yellow1.value(0)
       red1.value(1)
       green2.value(0)
       yellow2.value(0)
       red2.value(1)
       green3.value(1)
       yellow3.value(0)
       red3.value(0)
       utime.sleep_ms(mes*1000)
       reader1.init()
       (stat1, tag_type1) = reader1.request(reader1.REQIDL)
       if stat1 == reader1.OK:
           (stat1, uid1) = reader1.SelectTagSN()
           if stat1 == reader1.OK:
               card1 = int.from_bytes(bytes(uid1), "little", False)
               print("RFID1 - CARD ID: " + str(card1))
               if card1 == 2890929491:
                   green1.value(1)
                   yellow1.value(0)
                   red1.value(0)
                   green2.value(0)
                   yellow2.value(0)
                   red2.value(1)
                   green3.value(0)
                   yellow3.value(0)
                   red3.value(1)
                   print("Emergency vehicle has entered the road!!!!!")
                   print("Halting normal operation!!!")
                   while True:
                       reader2.init()
                       (stat2, tag_type2) = reader2.request(reader2.REQIDL)
                       if stat2 == reader2.OK:
                           (stat2, uid2) = reader2.SelectTagSN()
                           if stat2 == reader2.OK:
                               card2 = int.from_bytes(bytes(uid2), "little", False)
                               print("RFID2 - CARD ID: " + str(card2))
                               if card2 == 2890929491:
                                   print("Emergency vehicle has left the road!!!!!")
                                   print("Resuming normal operation!!!")
                                   green1.value(0)
                                   red1.value(0)
                                   break  
       green3.value(0)
       yellow3.value(1)
       utime.sleep_ms(2000)
       reader1.init()
       (stat1, tag_type1) = reader1.request(reader1.REQIDL)
       if stat1 == reader1.OK:
           (stat1, uid1) = reader1.SelectTagSN()
           if stat1 == reader1.OK:
               card1 = int.from_bytes(bytes(uid1), "little", False)
               print("RFID1 - CARD ID: " + str(card1))
               if card1 == 2890929491:
                   green1.value(1)
                   yellow1.value(0)
                   red1.value(0)
                   green2.value(0)
                   yellow2.value(0)
                   red2.value(1)
                   green3.value(0)
                   yellow3.value(0)
                   red3.value(1)
                   print("Emergency vehicle has entered the road!!!!!")
                   print("Halting normal operation!!!")
                   while True:
                       reader2.init()
                       (stat2, tag_type2) = reader2.request(reader2.REQIDL)
                       if stat2 == reader2.OK:
                           (stat2, uid2) = reader2.SelectTagSN()
                           if stat2 == reader2.OK:
                               card2 = int.from_bytes(bytes(uid2), "little", False)
                               print("RFID2 - CARD ID: " + str(card2))
                               if card2 == 2890929491:
                                   print("Emergency vehicle has left the road!!!!!")
                                   print("Resuming normal operation!!!")
                                   break  


lane1_feed = bytes('{:s}/feeds/{:s}'.format(ADAFRUIT_USERNAME, LANE_1_ID), 'utf-8')
lane2_feed = bytes('{:s}/feeds/{:s}'.format(ADAFRUIT_USERNAME, LANE_2_ID), 'utf-8')
lane3_feed = bytes('{:s}/feeds/{:s}'.format(ADAFRUIT_USERNAME, LANE_3_ID), 'utf-8')
client.set_callback(cb)# Callback function               
client.subscribe(lane1_feed)
client.subscribe(lane2_feed)
client.subscribe(lane3_feed)

while True:
    try:
        client.check_msg()# non blocking function
    except:
        client.disconnect()
        sys.exit()



