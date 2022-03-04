"""Entry script."""

#from vacuum_control.ir_control import IRControl
from vacuum_control.fake_ir_control import FakeIRControl
from clients.stdin_client import STDINClient
from clients.mqtt_client import MQTTClient

#ir_control = IRControl()

#client = None
#client = STDINClient(ir_control)
#client.listen()
#ir_control.destroy()

fake_ir_control = FakeIRControl()

client = None
client = MQTTClient(fake_ir_control)
client.listen()
fake_ir_control.destroy()

