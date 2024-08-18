import enum


class CommandTypes(enum.Enum):
   Command =1
   CancelCommand = 2



class Command:
   def __init__(self):
      self.command_type = CommandTypes.Command
      pass

   def run(self):
      pass

   def is_finished(self):
      return True