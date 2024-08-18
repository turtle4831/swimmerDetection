from micro_controller_side.CameraStream import aruco_helper
from micro_controller_side.CameraStream.camera import Camera
from micro_controller_side.Subsystems.movement import Movement
from micro_controller_side.commands import command


class ZeroCommand(command.Command):
   def __init__(self, movement:Movement,eyes:Camera):
      self.movement = movement
      self.eyes = eyes
      self.aruco = aruco_helper.ArucoHelper()
      super().__init__()

   def run(self):
      distance = self.aruco.get_aruco_info(self.eyes.get_camera_stream())

      self.movement.pid_control(10,distance)#stops when the camera is 10 cm away from the tag

   def is_finished(self):
      return self.movement.is_at_setpoint()
