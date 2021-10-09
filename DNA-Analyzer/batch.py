from command import Command


class Batch(Command):

    def __init__(self):
        self.__batch_commands=[]

    def execute(self,command):
        if len(command)==2:
            comm=None
            while comm!="end":
                print("> batch >>>")
                comm=input()
                self.__batch_commands.append(comm)
            self.get_batch_data().add_batch(command[1],self)
        else:
            print("not a valid batch command")


    def get_batch_commands(self):
        return self.__batch_commands