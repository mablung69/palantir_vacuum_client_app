"""Entry script."""

from vacuum_control.ir_control import IRControl
from clients.stdin_client import STDINClient

client = None

ir_control = IRControl()
client = STDINClient(ir_control)

client.listen()

ir_control.destroy()
