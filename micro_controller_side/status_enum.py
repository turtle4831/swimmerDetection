import enum


class MechanismStatus(enum.Enum):
   DISABLED = 1
   ENABLED = 2
   LOADING = 3
   CALIBRATING_SYSTEM = 4
   SAFETY_ERROR = 5
   MODEL_ERROR = 6
