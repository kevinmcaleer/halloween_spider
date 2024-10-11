# Spider Animatronic
from time import sleep
from rangefinder import ping
import Servo # Need to use the Pimoroni MicroPython firmware to get this library

# Set the pins used
ECHO_PIN = 0
TRIGGER_PIN = 1
SERVO_PIN = 2

# set Default positions
DEFAULT_POSITON = 90 # test different values to find the correct resting position for your robot
MAX_POSITION = 120   # test different values to find the correct Maximum position for your robot
MIN_DISTANCE = 0     # minimum distance to react from
MAX_DISTANCE = 30    # maximum distance to react from

servo = Servo()

def map_value(value, from_min, from_max, to_min, to_max):
    """ Map values from one range to another """
    
    # Calculate the ratio of the input value within its current range
    ratio = (value - from_min) / (from_max - from_min)
    
    # Map that ratio to the new range
    mapped_value = to_min + (ratio * (to_max - to_min))
    return mapped_value

def get_distance():
    distance = ping()
    return distance

def move_to_default_position():
    servo.angle = DEFAULT_POSITON

def move_to_distance(distance:int):
    servo.angle = map(distance, MIN_DISTANCE, MAX_DISTANCE, DEFAULT_POSITON, MAX_POSITION) 

def main():
    distance = get_distance()
    if distance > 30:
        move_to_default_position()
    else:
        move_to_distance(distance=distance)

    sleep(0.25)

main()