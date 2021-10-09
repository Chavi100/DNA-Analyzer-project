from command import Command

class Batchshow(Command):
    def execute(self,command):
        if len(command)==2:
            try:
              batch=self.get_batch_data().get_batch_dict()[command[1]].get_batch_commands()
              for comm in batch:
                  print(comm)
              return
            except(Exception):
                print("no batch with name:"+command[1])
        else:
            print("not right syntax for batchshow")