from adafruit_servokit import ServoKit
from simple_pid import PID


class Motor:
   def __init__(self):
      self.kit = ServoKit(channels=16)
      self.motor = self.kit.continuous_servo[0]
      self.pid = PID(0.0001,0,0,setpoint=0)
      self.pid.output_limits = (-1,1)

   def setPower(self, throttle):
      self.motor.throttle = throttle

   def pid_control(self, point, measurement):
      self.pid.setpoint = point

      return self.pid(measurement)





