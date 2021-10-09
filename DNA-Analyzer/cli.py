from Parser import Parser
from controller import Controller
from command import Command

class Cli(Command):

    def __init__(self):
        self.controller=Controller()

    def run_cli(self):
        while True:
            print("> cmd >>>;")
            command=input()
            self.send_command_to_controller(command)

    def send_command_to_controller(self, command):
        command = Parser(command).get__parsed()
        try:
            self.controller.get_controller(command[0]).execute(command)
        except(Exception):
            if command[0]=="run":
                if len(command) == 2:
                   batch=self.get_batch_data().get_batch_dict()[command[1]]
                   batch=batch.get_batch_commands()
                   for elem in batch:
                       if elem!="end":
                        self.send_command_to_controller(elem)
                else:
                    print("doesn't know which batch to run")
            else:
              print("not valid command")



cli=Cli()
cli.run_cli()