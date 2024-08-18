from time import sleep

from micro_controller_side.commands.zero_mechanism import ZeroCommand
from micro_controller_side.Subsystems.arduco_cam import ArducoCam
from micro_controller_side.Subsystems.movement import Movement
from micro_controller_side.Subsystems.subsystem import Subsystem
from micro_controller_side.commands import command_scheduler


sleep(10)

movement = Movement()
arduco_cam = ArducoCam()

subsystems = [Subsystem]
subsystems.append(movement)
subsystems.append(arduco_cam)

commandScheduler = command_scheduler.CommandScheduler()


for system in subsystems:
   system.initialize()

print("setting up hardware")
sleep(5)#allow hardware to be setup

commandScheduler.schedule_command(ZeroCommand(movement,arduco_cam.get_camera()))


print("waiting for web signal")
#TODO wait for signal from webapp

while True:#TODO add stop case

   commandScheduler.loop()
   for system in subsystems:
      system.update()

