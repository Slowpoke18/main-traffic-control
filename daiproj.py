from mfrc522 import MFRC522
import utime
from machine import Pin

# Configure RFID1
reader1 = MFRC522(spi_id=0, sck=6, miso=4, mosi=7, cs=5, rst=22)

# Configure RFID2
reader2 = MFRC522(spi_id=0, sck=6, miso=4, mosi=7, cs=10, rst=21)

# LED pin configuration
led_pins = {
    'lane1': {
        'green': Pin(2, Pin.OUT),
        'yellow': Pin(3, Pin.OUT),
        'red': Pin(11, Pin.OUT)
    },
    'lane2': {
        'green': Pin(8, Pin.OUT),
        'yellow': Pin(9, Pin.OUT),
        'red': Pin(18, Pin.OUT)
    },
    'lane3': {
        'green': Pin(15, Pin.OUT),
        'yellow': Pin(16, Pin.OUT),
        'red': Pin(17, Pin.OUT)
    }
}

# Define the duration of each light (in milliseconds)
green_light_duration = 3000  # 3 seconds
yellow_light_duration = 2000  # 1 second

# Initialize LED states
led_states = {
    'lane1': {
        'green': False,
        'yellow': False,
        'red': True
    },
    'lane2': {
        'green': False,
        'yellow': False,
        'red': True
    },
    'lane3': {
        'green': False,
        'yellow': False,
        'red': True
    }
}

def update_led_states():
    for lane, colors in led_states.items():
        for color, state in colors.items():
            led_pins[lane][color].value(state)

def normal_traffic_light():
    # Lane 1: Green, Lane 2 and Lane 3: Red
    led_states['lane1'] = {'green': True, 'yellow': False, 'red': False}
    led_states['lane2'] = {'green': False, 'yellow': False, 'red': True}
    led_states['lane3'] = {'green': False, 'yellow': False, 'red': True}
    update_led_states()
    utime.sleep_ms(green_light_duration)

    # Check for RFID1 detection at the end of Lane 1's green light
    reader1.init()
    (stat1, tag_type1) = reader1.request(reader1.REQIDL)

    if stat1 == reader1.OK:
        (stat1, uid1) = reader1.SelectTagSN()
        if stat1 == reader1.OK:
            card1 = int.from_bytes(bytes(uid1), "little", False)
            print("RFID1 - CARD ID: " + str(card1))
            if card1 == 2890929491:
                led_states['lane1'] = {'green': True, 'yellow': False, 'red': False}
                led_states['lane2'] = {'green': False, 'yellow': False, 'red': True}
                led_states['lane3'] = {'green': False, 'yellow': False, 'red': True}
                update_led_states()
                while True:
                    # Stay in the same state until RFID2 detects a tag
                    reader2.init()
                    (stat2, tag_type2) = reader2.request(reader2.REQIDL)

                    if stat2 == reader2.OK:
                        (stat2, uid2) = reader2.SelectTagSN()
                        if stat2 == reader2.OK:
                            card2 = int.from_bytes(bytes(uid2), "little", False)
                            print("RFID2 - CARD ID: " + str(card2))
                            if card2 == 2890929491:
                                break  # Restart normal traffic light behavior

    # Lane 1: Yellow, Lane 2 and Lane 3: Red
    led_states['lane1'] = {'green': False, 'yellow': True, 'red': False}
    update_led_states()
    utime.sleep_ms(yellow_light_duration)
    
    # Check for RFID1 detection at the end of Lane 1's yellow light
    reader1.init()
    (stat1, tag_type1) = reader1.request(reader1.REQIDL)

    if stat1 == reader1.OK:
        (stat1, uid1) = reader1.SelectTagSN()
        if stat1 == reader1.OK:
            card1 = int.from_bytes(bytes(uid1), "little", False)
            print("RFID1 - CARD ID: " + str(card1))
            if card1 == 2890929491:
                led_states['lane1'] = {'green': True, 'yellow': False, 'red': False}
                led_states['lane2'] = {'green': False, 'yellow': False, 'red': True}
                led_states['lane3'] = {'green': False, 'yellow': False, 'red': True}
                update_led_states()
                while True:
                    # Stay in the same state until RFID2 detects a tag
                    reader2.init()
                    (stat2, tag_type2) = reader2.request(reader2.REQIDL)

                    if stat2 == reader2.OK:
                        (stat2, uid2) = reader2.SelectTagSN()
                        if stat2 == reader2.OK:
                            card2 = int.from_bytes(bytes(uid2), "little", False)
                            print("RFID2 - CARD ID: " + str(card2))
                            if card2 == 2890929491:
                                break  # Restart normal traffic light behavior

    # Lane 1: Red, Lane 2: Green, Lane 3: Red
    led_states['lane1'] = {'green': False, 'yellow': False, 'red': True}
    led_states['lane2'] = {'green': True, 'yellow': False, 'red': False}
    update_led_states()
    utime.sleep_ms(green_light_duration)

    # Check for RFID1 detection at the end of Lane 2's green light
    reader1.init()
    (stat1, tag_type1) = reader1.request(reader1.REQIDL)

    if stat1 == reader1.OK:
        (stat1, uid1) = reader1.SelectTagSN()
        if stat1 == reader1.OK:
            card1 = int.from_bytes(bytes(uid1), "little", False)
            print("RFID1 - CARD ID: " + str(card1))
            if card1 == 2890929491:
                led_states['lane1'] = {'green': True, 'yellow': False, 'red': False}
                led_states['lane2'] = {'green': False, 'yellow': False, 'red': True}
                led_states['lane3'] = {'green': False, 'yellow': False, 'red': True}
                update_led_states()
                while True:
                    # Stay in the same state until RFID2 detects a tag
                    reader2.init()
                    (stat2, tag_type2) = reader2.request(reader2.REQIDL)

                    if stat2 == reader2.OK:
                        (stat2, uid2) = reader2.SelectTagSN()
                        if stat2 == reader2.OK:
                            card2 = int.from_bytes(bytes(uid2), "little", False)
                            print("RFID2 - CARD ID: " + str(card2))
                            if card2 == 2890929491:
                                break  # Restart normal traffic light behavior

    # Lane 1: Red, Lane 2: Yellow, Lane 3: Red
    led_states['lane1'] = {'green': False, 'yellow': False, 'red': True}
    led_states['lane2'] = {'green': False, 'yellow': True, 'red': False}
    update_led_states()
    utime.sleep_ms(yellow_light_duration)
    
    # Check for RFID1 detection at the end of Lane 2's yellow light
    reader1.init()
    (stat1, tag_type1) = reader1.request(reader1.REQIDL)

    if stat1 == reader1.OK:
        (stat1, uid1) = reader1.SelectTagSN()
        if stat1 == reader1.OK:
            card1 = int.from_bytes(bytes(uid1), "little", False)
            print("RFID1 - CARD ID: " + str(card1))
            if card1 == 2890929491:
                led_states['lane1'] = {'green': True, 'yellow': False, 'red': False}
                led_states['lane2'] = {'green': False, 'yellow': False, 'red': True}
                led_states['lane3'] = {'green': False, 'yellow': False, 'red': True}
                update_led_states()
                while True:
                    # Stay in the same state until RFID2 detects a tag
                    reader2.init()
                    (stat2, tag_type2) = reader2.request(reader2.REQIDL)

                    if stat2 == reader2.OK:
                        (stat2, uid2) = reader2.SelectTagSN()
                        if stat2 == reader2.OK:
                            card2 = int.from_bytes(bytes(uid2), "little", False)
                            print("RFID2 - CARD ID: " + str(card2))
                            if card2 == 2890929491:
                                break  # Restart normal traffic light behavior

    # Lane 1: Red, Lane 2 and Lane 3: Green
    led_states['lane1'] = {'green': False, 'yellow': False, 'red': True}
    led_states['lane2'] = {'green': False, 'yellow': False, 'red': True}
    led_states['lane3'] = {'green': True, 'yellow': False, 'red': False}
    update_led_states()
    utime.sleep_ms(green_light_duration)

    # Check for RFID1 detection at the end of Lane 3's green light
    reader1.init()
    (stat1, tag_type1) = reader1.request(reader1.REQIDL)

    if stat1 == reader1.OK:
        (stat1, uid1) = reader1.SelectTagSN()
        if stat1 == reader1.OK:
            card1 = int.from_bytes(bytes(uid1), "little", False)
            print("RFID1 - CARD ID: " + str(card1))
            if card1 == 2890929491:
                led_states['lane1'] = {'green': True, 'yellow': False, 'red': False}
                led_states['lane2'] = {'green': False, 'yellow': False, 'red': True}
                led_states['lane3'] = {'green': False, 'yellow': False, 'red': True}
                update_led_states()
                while True:
                    # Stay in the same state until RFID2 detects a tag
                    reader2.init()
                    (stat2, tag_type2) = reader2.request(reader2.REQIDL)

                    if stat2 == reader2.OK:
                        (stat2, uid2) = reader2.SelectTagSN()
                        if stat2 == reader2.OK:
                            card2 = int.from_bytes(bytes(uid2), "little", False)
                            print("RFID2 - CARD ID: " + str(card2))
                            if card2 == 2890929491:
                                break  # Restart normal traffic light behavior

    # Lane 1: Red, Lane 2: Yellow, Lane 3: Red
    led_states['lane1'] = {'green': False, 'yellow': False, 'red': True}
    led_states['lane3'] = {'green': False, 'yellow': True, 'red': False}
    update_led_states()
    utime.sleep_ms(yellow_light_duration)
    
    # Check for RFID1 detection at the end of Lane 3's yellow light
    reader1.init()
    (stat1, tag_type1) = reader1.request(reader1.REQIDL)

    if stat1 == reader1.OK:
        (stat1, uid1) = reader1.SelectTagSN()
        if stat1 == reader1.OK:
            card1 = int.from_bytes(bytes(uid1), "little", False)
            print("RFID1 - CARD ID: " + str(card1))
            if card1 == 2890929491:
                led_states['lane1'] = {'green': True, 'yellow': False, 'red': False}
                led_states['lane2'] = {'green': False, 'yellow': False, 'red': True}
                led_states['lane3'] = {'green': False, 'yellow': False, 'red': True}
                update_led_states()
                while True:
                    # Stay in the same state until RFID2 detects a tag
                    reader2.init()
                    (stat2, tag_type2) = reader2.request(reader2.REQIDL)

                    if stat2 == reader2.OK:
                        (stat2, uid2) = reader2.SelectTagSN()
                        if stat2 == reader2.OK:
                            card2 = int.from_bytes(bytes(uid2), "little", False)
                            print("RFID2 - CARD ID: " + str(card2))
                            if card2 == 2890929491:
                                break  # Restart normal traffic light behavior

while True:
    normal_traffic_light()

