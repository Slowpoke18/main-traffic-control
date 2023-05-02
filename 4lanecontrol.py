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

lane = 1

def red_light_on_1():
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

def yellow_light_on_1():
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

def green_light_on_1():
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

def red_light_on_2():
    red_led_lane_1.value(1)
    yellow_led_lane_1.value(0)
    green_led_lane_1.value(0)
    red_led_lane_2.value(0)
    yellow_led_lane_2.value(0)
    green_led_lane_2.value(1)
    red_led_lane_3.value(0)
    yellow_led_lane_3.value(0)
    green_led_lane_3.value(1)
    red_led_lane_4.value(1)
    yellow_led_lane_4.value(0)
    green_led_lane_4.value(0)

def yellow_light_on_2():
    red_led_lane_1.value(1)
    yellow_led_lane_1.value(0)
    green_led_lane_1.value(0)
    red_led_lane_2.value(0)
    yellow_led_lane_2.value(1)
    green_led_lane_2.value(0)
    red_led_lane_3.value(1)
    yellow_led_lane_3.value(0)
    green_led_lane_3.value(0)
    red_led_lane_4.value(1)
    yellow_led_lane_4.value(0)
    green_led_lane_4.value(0)

def green_light_on_2():
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

def red_light_on_3():
    red_led_lane_1.value(1)
    yellow_led_lane_1.value(0)
    green_led_lane_1.value(0)
    red_led_lane_2.value(1)
    yellow_led_lane_2.value(0)
    green_led_lane_2.value(0)
    red_led_lane_3.value(1)
    yellow_led_lane_3.value(0)
    green_led_lane_3.value(0)
    red_led_lane_4.value(0)
    yellow_led_lane_4.value(0)
    green_led_lane_4.value(1)

def yellow_light_on_3():
    red_led_lane_1.value(1)
    yellow_led_lane_1.value(0)
    green_led_lane_1.value(0)
    red_led_lane_2.value(1)
    yellow_led_lane_2.value(0)
    green_led_lane_2.value(0)
    red_led_lane_3.value(0)
    yellow_led_lane_3.value(1)
    green_led_lane_3.value(0)
    red_led_lane_4.value(1)
    yellow_led_lane_4.value(0)
    green_led_lane_4.value(0)

def green_light_on_3():
    red_led_lane_1.value(1)
    yellow_led_lane_1.value(0)
    green_led_lane_1.value(0)
    red_led_lane_2.value(1)
    yellow_led_lane_2.value(0)
    green_led_lane_2.value(0)
    red_led_lane_3.value(0)
    yellow_led_lane_3.value(0)
    green_led_lane_3.value(1)
    red_led_lane_4.value(1)
    yellow_led_lane_4.value(0)
    green_led_lane_4.value(0)

def red_light_on_4():
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

def yellow_light_on_4():
    red_led_lane_1.value(1)
    yellow_led_lane_1.value(0)
    green_led_lane_1.value(0)
    red_led_lane_2.value(1)
    yellow_led_lane_2.value(0)
    green_led_lane_2.value(0)
    red_led_lane_3.value(1)
    yellow_led_lane_3.value(0)
    green_led_lane_3.value(0)
    red_led_lane_4.value(0)
    yellow_led_lane_4.value(1)
    green_led_lane_4.value(0)

def green_light_on_4():
    red_led_lane_1.value(1)
    yellow_led_lane_1.value(0)
    green_led_lane_1.value(0)
    red_led_lane_2.value(1)
    yellow_led_lane_2.value(0)
    green_led_lane_2.value(0)
    red_led_lane_3.value(1)
    yellow_led_lane_3.value(0)
    green_led_lane_3.value(0)
    red_led_lane_4.value(0)
    yellow_led_lane_4.value(0)
    green_led_lane_4.value(1)

def input_lane_1():
    # Prompt the user to enter a command
    cmd = input("Enter number of vehicles in lane 1: ")
    #print(type(cmd))
    #cmd_off = str(cmd)
    cmd_new = int(cmd)
    #print(cmd_new)
    # Process the command
    if cmd_new == 0:
        all_light_off()
    elif cmd_new <= 5:
        time.sleep(1)
        green_light_on_1()
        time.sleep(5)
        yellow_light_on_1()
        time.sleep(2)
        red_light_on_1()
    elif cmd_new >= 10:
        time.sleep(1)
        green_light_on_1()
        time.sleep(10)
        yellow_light_on_1()
        time.sleep(2)
        red_light_on_1()
    elif (cmd_new >= 5 and cmd_new <=10):
        time.sleep(1)
        green_light_on_1()
        time.sleep(cmd_new)
        yellow_light_on_1()
        time.sleep(2)
        red_light_on_1()
    else:
        print("Invalid command, try again.")

def input_lane_2():
    # Prompt the user to enter a command
    cmd = input("Enter number of vehicles in lane 2: ")
    #print(type(cmd))
    #cmd_off = str(cmd)
    cmd_new = int(cmd)
    #print(cmd_new)
    # Process the command
    if cmd_new == 0:
        all_light_off()
    elif cmd_new <= 5:
        time.sleep(1)
        green_light_on_2()
        time.sleep(5)
        yellow_light_on_2()
        time.sleep(2)
        red_light_on_2()
    elif cmd_new >= 10:
        time.sleep(1)
        green_light_on_2()
        time.sleep(10)
        yellow_light_on_2()
        time.sleep(2)
        red_light_on_2()
    elif (cmd_new >= 5 and cmd_new <=10):
        time.sleep(1)
        green_light_on_2()
        time.sleep(cmd_new)
        yellow_light_on_2()
        time.sleep(2)
        red_light_on_2()
    else:
        print("Invalid command, try again.")


def input_lane_3():
    # Prompt the user to enter a command
    cmd = input("Enter number of vehicles in lane 3: ")
    #print(type(cmd))
    #cmd_off = str(cmd)
    cmd_new = int(cmd)
    #print(cmd_new)
    # Process the command
    if cmd_new == 0:
        all_light_off()
    elif cmd_new <= 5:
        time.sleep(1)
        green_light_on_3()
        time.sleep(5)
        yellow_light_on_3()
        time.sleep(2)
        red_light_on_3()
    elif cmd_new >= 10:
        time.sleep(1)
        green_light_on_3()
        time.sleep(10)
        yellow_light_on_3()
        time.sleep(2)
        red_light_on_3()
    elif (cmd_new >= 5 and cmd_new <=10):
        time.sleep(1)
        green_light_on_3()
        time.sleep(cmd_new)
        yellow_light_on_3()
        time.sleep(2)
        red_light_on_3()
    else:
        print("Invalid command, try again.")
        
def input_lane_4():
    # Prompt the user to enter a command
    cmd = input("Enter number of vehicles in lane 4: ")
    #print(type(cmd))
    #cmd_off = str(cmd)
    cmd_new = int(cmd)
    #print(cmd_new)
    # Process the command
    if cmd_new == 0:
        all_light_off()
    elif cmd_new <= 5:
        time.sleep(1)
        green_light_on_4()
        time.sleep(5)
        yellow_light_on_4()
        time.sleep(2)
        red_light_on_4()
    elif cmd_new >= 10:
        time.sleep(1)
        green_light_on_4()
        time.sleep(10)
        yellow_light_on_4()
        time.sleep(2)
        red_light_on_4()
    elif (cmd_new >= 5 and cmd_new <=10):
        time.sleep(1)
        green_light_on_4()
        time.sleep(cmd_new)
        yellow_light_on_4()
        time.sleep(2)
        red_light_on_4()
    else:
        print("Invalid command, try again.")


while True:
    # Prompt the user to enter a command
    #cmd = input("Enter number of vehicles to vary the time ")
    #print(type(cmd))
    #cmd_off = str(cmd)
    #cmd_new = int(cmd)
    #print(cmd_new)
    #cmd_off = str(cmd)
    # Process the command
    if lane == 1:
        input_lane_1()
        lane = lane + 1
    elif lane == 2:
        input_lane_2()
        lane = lane + 1
    elif lane == 3:
        input_lane_3()
        lane = lane + 1
    else:
        input_lane_4()
        lane = 1
        
        
