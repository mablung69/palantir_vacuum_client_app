"""Class member on vacuum control module."""
#import RPi.GPIO as GPIO
import json
from time import time, sleep

class IRControl:
    """ """

    def __init__(self):
        """ """
        self.IR_PIN = 3
        #GPIO.setmode(GPIO.BOARD)
        #GPIO.setup(self.IR_PIN, GPIO.OUT)
        ir_dict_path="../palantir_raw_vacuum_remote_ir_data/data/cleaned/ir_dict.json"
        with open(ir_dict_path) as json_file:
            self.ir_dict = json.load(json_file)

    def send(self, action):
        """ """
        #send action
        for interval in self.ir_dict[action]:
            state = True if interval>0 else False
            duration = interval if interval>=0 else -interval
            #GPIO.output(self.IR_PIN, state)
            print("SLEEP",str(float(duration)/1000000.0))
            sleep(float(duration)/1000000.0)
