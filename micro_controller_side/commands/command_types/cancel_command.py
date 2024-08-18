from micro_controller_side.commands.command import Command, CommandTypes


class CancelCommand(Command):
   def __init__(self):

      self.command_type = CommandTypes.CancelCommand
      super().__init__()

   def get_canceled_command(self):
      return self.canceled_command

