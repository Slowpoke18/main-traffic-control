from mfrc522 import MFRC522
import utime

red_led_lane_1 = machine.Pin(15, machine.Pin.OUT)
reader = MFRC522(spi_id=0,sck=6,miso=4,mosi=7,cs=5,rst=22)
 
print("Bring TAG closer...")
print("")
card = 0 
while True:
    reader.init()
    (stat, tag_type) = reader.request(reader.REQIDL)
    if stat == reader.OK:
        (stat, uid) = reader.SelectTagSN()
        if stat == reader.OK:
            card = int.from_bytes(bytes(uid),"little",False)
            print("CARD ID: "+str(card))
    if str(card) == "1079007939":
        red_led_lane_1.value(1)
    else:
        red_led_lane_1.value(0)
utime.sleep_ms(1000)

