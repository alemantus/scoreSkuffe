import RPi.GPIO as GPIO
import sys
from endStop import endStop
# import the library
from RpiMotorLib import RpiMotorLib


#GPIO.setup(22, GPIO.OUT, pull_up_down=GPIO.PUD_DOWN)    
#define GPIO pins
GPIO_pins = (-1, -1, -1) # Microstep Resolution MS1-MS3 -> GPIO Pin
direction= 27       # Direction -> GPIO Pin
step = 22       # Step -> GPIO Pin

# Declare an named instance of class pass GPIO pins numbers
mymotortest = RpiMotorLib.A4988Nema(direction, step, GPIO_pins, "A4988")

inStop = endStop(19)
outStop = endStop(16)

# call the function, pass the arguments
while(outStop.readEndstop() == 1):
    mymotortest.motor_go(True, "Full" , 20, .002, True, 0)

while(inStop.readEndstop() == 1):
    mymotortest.motor_go(False, "Full" , 20, .004, True, 0)


mymotortest.motor_stop()

# good practise to cleanup GPIO at some point before exit
#GPIO.cleanup()
