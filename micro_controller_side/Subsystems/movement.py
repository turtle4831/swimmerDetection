import enum
from adafruit_servokit import ServoKit
from simple_pid import PID

from micro_controller_side import status_enum
from micro_controller_side.Subsystems import subsystem
from micro_controller_side.status_enum import MechanismStatus


class CalibrationStatus(enum.Enum):
   NOT_CALIBRATED = 1
   CALIBRATED = 2


class MotorStatus(enum.Enum):
   NOMINAL = 1
   NO_MOTOR_FOUND = 2


class Movement(subsystem.Subsystem):#TODO create state machine
   def __init__(self):
      self.kit = ServoKit(channels=16)
      self.motor = self.kit.continuous_servo[0]
      self.pid = PID(0.000001, 0, 0, setpoint=0)
      self.pid.output_limits = (-1, 1)
      self.calibration_status = CalibrationStatus.NOT_CALIBRATED
      self.motor_status = MotorStatus.NOMINAL
      self.mechanism_state = MechanismStatus.DISABLED
      self.throttle = self.motor.throttle
      super().__init__()


   def set_motor_power(self, throttle:float):
      self.throttle = throttle
      self.motor.throttle = throttle

   def pid_control(self, point, measurement):
      self.pid.setpoint = point

      return self.pid(measurement)

   def is_at_setpoint(self):
      return self.errorTolerance(-0.1,self.throttle)


   def errorTolerance(self, tolerance: float, value):
      """

      :param tolerance: negative value
      :param value:
      :return:
      """
      return tolerance <= value <= tolerance.__abs__()
   def update(self):
      pass

   def initialize(self):
      self.mechanism_state = status_enum.MechanismStatus.CALIBRATING_SYSTEM



