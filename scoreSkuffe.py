import RPi.GPIO as GPIO

# import the library
from RpiMotorLib import RpiMotorLib


#GPIO.setup(22, GPIO.OUT, pull_up_down=GPIO.PUD_DOWN)    
#define GPIO pins
GPIO_pins = (-1, -1, -1) # Microstep Resolution MS1-MS3 -> GPIO Pin
direction= 27       # Direction -> GPIO Pin
step = 22       # Step -> GPIO Pin

# Declare an named instance of class pass GPIO pins numbers
mymotortest = RpiMotorLib.A4988Nema(direction, step, GPIO_pins, "A4988")


# call the function, pass the arguments
mymotortest.motor_go(False, "Full" , 1000, .002, False, .05)

mymotortest.motor_stop()

# good practise to cleanup GPIO at some point before exit
#GPIO.cleanup()
