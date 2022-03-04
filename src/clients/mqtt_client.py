"""Class member on client module."""
import sys
from time import sleep
from select import select
import paho.mqtt.client as mqtt

class MQTTClient:
    """ """

    def __init__(self, control):
        """ """
        self.control = control
        self.host = "172.10.0.21"
        self.host = "192.168.50.236"        
        self.port = 2883
        self.keep_alives = 60
        self.topic_command = "topic/command"
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

    def onConnect(self, client, userdata, flags, rc):
        """ """
        print("Connected with result code "+str(rc))
        #to renew subscriptions after disconnect
        client.subscribe(self.topic_command)

    def onMessage(self, client, userdata, msg):
        """ """
        print(msg.topic+" "+str(msg.payload))
        #process input
        a = msg.payload.decode("utf-8")
        action = self.processCommand(a.strip())
        print("Action:", action)
        if action == "invalid":
            print("Invalid Command!")
        elif action == "exit":
            pass
        else:
            #call action
            self.control.send(action)

    def onDisconnect(self, client, userdata, rc):
        """ """
        print("Disconnected with result code "+str(rc))

    def listen(self):
        """ """
        print("Listening from  MQTT Server")
        client = mqtt.Client()
        client.on_connect = self.onConnect
        client.on_message = self.onMessage
        client.on_disconnect = self.onDisconnect
        client.connect(self.host, self.port, self.keep_alives)
        client.loop_forever()
        print("Stop listening from MQTT Server")


