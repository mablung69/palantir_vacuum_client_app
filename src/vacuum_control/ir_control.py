"""Class member on vacuum control module."""
import RPi.GPIO as GPIO
import json
from time import time, sleep

class IRControl:
    """ """

    def __init__(self):
        """ """
        self.IR_PIN = 11 #In physical Pin 11
        self.action_pin = {
            "PIN_11": 11,
            "PIN_13": 13,
            "PIN_15": 15,
            "PIN_16": 16,
            "PIN_18": 18
        }
        GPIO.setmode(GPIO.BOARD)
        for pin in self.action_pin.keys():
            GPIO.setup(self.action_pin[pin], GPIO.OUT)
            GPIO.output(self.action_pin[pin], False)
        ir_dict_path="../data/ir_dict.json"
        with open(ir_dict_path) as json_file:
            self.ir_dict = json.load(json_file)
        self.ir_dict["mode1"] = [50000,-50000]        
        self.ir_dict["mode2"] = [100000,-100000]
        self.ir_dict["mode3"] = [10000,-10000]
        self.ir_dict["mode4"] = [5000,-5000]
        self.ir_dict["mode5"] = [1000,-1000]
        self.ir_dict["test3"] = [100000,-100000,100000,-100000]

    def send(self, mode, action="PIN_11"):
        """ """
        #send action
        pin = self.action_pin[action]
        for interval in self.ir_dict[mode]:
            state = True if interval>0 else False
            duration = interval if interval>=0 else -interval
            GPIO.output(pin, state)
            print("SLEEP",str(float(duration)/1000000.0),duration,state)
            sleep(float(duration)/100000.0)
        GPIO.output(pin, False)

    def destroy(self):
        GPIO.cleanup()
