import machine
import time

# Set up the LED lanes
red_led_lane_1 = machine.Pin(0, machine.Pin.OUT)
yellow_led_lane_1 = machine.Pin(1, machine.Pin.OUT)
green_led_lane_1 = machine.Pin(2, machine.Pin.OUT)

red_led_lane_2 = machine.Pin(6, machine.Pin.OUT)
yellow_led_lane_2 = machine.Pin(7, machine.Pin.OUT)
green_led_lane_2 = machine.Pin(8, machine.Pin.OUT)

red_led_lane_3 = machine.Pin(10, machine.Pin.OUT)
yellow_led_lane_3 = machine.Pin(11, machine.Pin.OUT)
green_led_lane_3 = machine.Pin(12, machine.Pin.OUT)

red_led_lane_4 = machine.Pin(20, machine.Pin.OUT)
yellow_led_lane_4 = machine.Pin(19, machine.Pin.OUT)
green_led_lane_4 = machine.Pin(18, machine.Pin.OUT)


def red_light_on():
    red_led_lane_1.value(1)
    yellow_led_lane_1.value(0)
    green_led_lane_1.value(0)
    red_led_lane_2.value(0)
    yellow_led_lane_2.value(0)
    green_led_lane_2.value(1)
    red_led_lane_3.value(1)
    yellow_led_lane_3.value(0)
    green_led_lane_3.value(0)
    red_led_lane_4.value(1)
    yellow_led_lane_4.value(0)
    green_led_lane_4.value(0)

def yellow_light_on():
    red_led_lane_1.value(0)
    yellow_led_lane_1.value(1)
    green_led_lane_1.value(0)
    red_led_lane_2.value(1)
    yellow_led_lane_2.value(0)
    green_led_lane_2.value(0)
    red_led_lane_3.value(1)
    yellow_led_lane_3.value(0)
    green_led_lane_3.value(0)
    red_led_lane_4.value(1)
    yellow_led_lane_4.value(0)
    green_led_lane_4.value(0)

def green_light_on():
    red_led_lane_1.value(0)
    yellow_led_lane_1.value(0)
    green_led_lane_1.value(1)
    red_led_lane_2.value(1)
    yellow_led_lane_2.value(0)
    green_led_lane_2.value(0)
    red_led_lane_3.value(1)
    yellow_led_lane_3.value(0)
    green_led_lane_3.value(0)
    red_led_lane_4.value(1)
    yellow_led_lane_4.value(0)
    green_led_lane_4.value(0)

def all_light_off():
    red_led_lane_1.value(0)
    yellow_led_lane_1.value(0)
    green_led_lane_1.value(0)
    red_led_lane_2.value(0)
    yellow_led_lane_2.value(0)
    green_led_lane_2.value(0)
    red_led_lane_3.value(0)
    yellow_led_lane_3.value(0)
    green_led_lane_3.value(0)
    red_led_lane_4.value(0)
    yellow_led_lane_4.value(0)
    green_led_lane_4.value(0)
# Main loop
while True:
    # Prompt the user to enter a command
    cmd = input("Enter number of vehicles to vary the time ")
    #print(type(cmd))
    #cmd_off = str(cmd)
    cmd_new = int(cmd)
    print(cmd_new)
    #cmd_off = str(cmd)
    # Process the command
    if cmd_new == 0:
        all_light_off()
    elif cmd_new <= 5:
        time.sleep(1)
        green_light_on()
        time.sleep(5)
        yellow_light_on()
        time.sleep(2)
        red_light_on()
    elif cmd_new >= 10:
        time.sleep(1)
        green_light_on()
        time.sleep(10)
        yellow_light_on()
        time.sleep(2)
        red_light_on()
    elif (cmd_new >= 5 and cmd_new <=10):
        time.sleep(1)
        green_light_on()
        time.sleep(cmd_new)
        yellow_light_on()
        time.sleep(2)
        red_light_on()
    else:
        print("Invalid command, try again.")
