"""Class member on vacuum control module."""
import RPi.GPIO as GPIO
import json
from time import time, sleep

class IRControl:
    """ """

    def __init__(self):
        """ """
        self.modes = {
            "base": [1000,-1000],
            "mode1": [50000,-50000],
            "mode2": [100000,-100000],
            "mode3": [10000,-10000],
            "mode4": [5000,-5000]
        }
        self.action_pin = {
            "PIN_11": 11,#In physical Pin 11
            "PIN_13": 13,#In physical Pin 13
            "PIN_15": 15,#In physical Pin 15
            "PIN_16": 16,#In physical Pin 16
            "PIN_18": 18 #In physical Pin 18
        }
        self.action_dict = {
            "up": {"pin": "PIN_16", "mode":"base"},
            "left": {"pin": "PIN_15", "mode":"base"},
            "right": {"pin": "PIN_13", "mode":"base"},
            "play-stop": {"pin": "PIN_11", "mode":"base"},
            "down": {"pin": "PIN_18", "mode":"base"}
        }
        GPIO.setmode(GPIO.BOARD)
        for pin in self.action_pin.keys():
            GPIO.setup(self.action_pin[pin], GPIO.OUT)
            GPIO.output(self.action_pin[pin], False)

    def send(self, action):
        """ """
        #send action
        action_object = self.action_dict[action]
        pin = self.action_pin[action_object["pin"]]
        for interval in self.modes[action_object["mode"]]:
            state = True if interval>0 else False
            duration = interval if interval>=0 else -interval
            GPIO.output(pin, state)
            print("SLEEP",str(float(duration)/1000000.0),duration,state)
            sleep(float(duration)/100000.0)
        GPIO.output(pin, False)

    def destroy(self):
        GPIO.cleanup()
