# Spider Animatronic
from time import sleep
from rangefinder import Range_Finder
from servo import Servo # Need to use the Pimoroni MicroPython firmware to get this library
from math import ceil

# Set the pins used
ECHO_PIN = 0
TRIGGER_PIN = 1
SERVO_PIN = 2

# set Default positions
DEFAULT_POSITON = 0 # test different values to find the correct resting position for your robot
MAX_POSITION = 90   # test different values to find the correct Maximum position for your robot
MIN_DISTANCE = 6     # minimum distance to react from
MAX_DISTANCE = 30    # maximum distance to react from

servo = Servo(SERVO_PIN)
range_finder = Range_Finder(echo_pin = ECHO_PIN, trigger_pin = TRIGGER_PIN)

def map_value(value, from_min, from_max, to_min, to_max):
    """ Map values from one range to another """
    
    # Calculate the ratio of the input value within its current range
    ratio = (value - from_min) / (from_max - from_min)
    
    # Map that ratio to the new range
    mapped_value = to_min + (ratio * (to_max - to_min))
    return mapped_value

def get_distance():
    distance = round(range_finder.ping() / 10,2)
    return distance

def move_to_default_position():
    servo.value(DEFAULT_POSITON)

def move_to_distance(distance:int):
    angle = int(map_value(distance, MIN_DISTANCE, MAX_DISTANCE, DEFAULT_POSITON, MAX_POSITION))
    print(f'Distance: {distance}, moving to {angle}')
    servo.value(angle) 

def main():
    while True:
        distance = get_distance()
        print(f'Distance: {distance}')
        if distance > 30:
            move_to_default_position()
        else:
            move_to_distance(distance=distance)

        sleep(0.25)

main()