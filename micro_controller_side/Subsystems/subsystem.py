from micro_controller_side import status_enum


class Subsystem:
   def __init__(self):
      self.mechanism_state = status_enum.MechanismStatus.DISABLED
      pass
   def initialize(self):
      pass
   def update(self):
      pass