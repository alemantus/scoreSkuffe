#!/usr/bin/python3

import time
import RPi.GPIO as GPIO


class endStop:
    def __init__(self, pinNumber):
        self.pinNumber = pinNumber

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pinNumber, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def readEndstop(self):
        return GPIO.input(self.pinNumber)



if __name__ == "__main__":
    inStop = endStop(19)
    outStop = endStop(16)
    
    while(1):
        print(f"outStop: {outStop.readEndstop()} - inStop: {inStop.readEndstop()}")
        time.sleep(0.1)