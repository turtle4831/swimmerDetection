from micro_controller_side import status_enum
from micro_controller_side.CameraStream.camera import Camera
from micro_controller_side.Subsystems.subsystem import Subsystem


class ArducoCam(Subsystem):
   def __init__(self):
      self.camera = Camera().__init__("arduco_cam", 1)

      super().__init__()
   def get_camera(self):
      return self.camera
   def initialize(self):
      self.mechanism_state = status_enum.MechanismStatus.ENABLED
      pass
   def update(self):
      pass
