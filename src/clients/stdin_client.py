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
            "w": "up",
            "s": "down",
            "a": "left",
            "d": "right",
            "q": "play-stop",
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
                else:
                    #call action
                    self.control.send(action)
            else:
                print('.', end='', flush=True)
        print("Stop listening from STDIN")


