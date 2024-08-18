from micro_controller_side.commands.command import Command, CommandTypes


class CommandScheduler:
   def __init__(self):
      self.commands = []
      pass

   def schedule_command(self, command: Command):
      self.commands.append(command)

   def loop(self):
      self.current_command = self.commands[0]
      self.current_command.run()

      #looking for any cancel commands
      for command in self.commands:
         if command.command_type == CommandTypes.CancelCommand:
            self.commands.clear()

      if self.current_command.is_finised == True:
         self.commands.pop(0)

   def wait_until_all_commands(self):
      if len(self.commands) == 0:
         return True
      return False