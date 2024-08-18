from time import sleep

from micro_controller_side.Subsystems.movement import Movement
from micro_controller_side.Subsystems.subsystem import Subsystem


movement = Movement()
subsystems = [Subsystem]

subsystems.append(movement)

for system in subsystems:
   system.initialize()


sleep(5)#allow hardware to be setup

#TODO wait for signal from webapp

while True:#TODO add stop case
   pass