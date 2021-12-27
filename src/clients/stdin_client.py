"""Class member on client module."""
import sys
from time import sleep
from select import select

class STDINClient:
    """ """

    def __init__(self, control):
        """ """
        self.control = control
        self.timeout = 5 #timeout in seconds
        self.commands = {
            "up": "up",
            "down": "down",
            "left": "left",
            "right": "right",
            "t": "test1",
            "p": "test2",
            "o":"test3",
            "w":["mode5","PIN_16"],
            "a":["mode5","PIN_15"],
            "d":["mode5","PIN_13"],
            "q":["mode5","PIN_11"],
            "s":["mode5","PIN_18"],
            "exit": "exit"
        }

    def processCommand(self, command):
        """ """        
        return self.commands[command] if command in self.commands.keys() else "invalid"

    def listen(self):
        """ """
        print("Listening from STDIN")
        while True:
            command = ""
            action = ""
            #read stdin
            rlist, _, _ = select([sys.stdin], [], [], self.timeout)
            if rlist:
                command = sys.stdin.readline()
                #process input
                action = self.processCommand(command.strip())
                if action == "invalid":
                    print("Invalid Command!")
                elif action == "exit":
                    break
                elif action == "test1":
                    self.control.send("up")
                    sleep(0.5)
                    self.control.send("up")
                    sleep(0.5)
                    self.control.send("up")
                    sleep(0.5)
                    self.control.send("up")
                    sleep(0.5)
                    self.control.send("up")
                elif type(action) is list:
                    #call action using mode and pin
                    self.control.send(action[0],action[1])
                else:
                    #call action
                    self.control.send(action)
            else:
                print('.', end='', flush=True)
        print("Stop listening from STDIN")


