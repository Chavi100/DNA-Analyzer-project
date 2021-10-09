from command import Command
class New(Command):

    __name_giver=1
    __id_giver=1

    def execute(self,command):
        if len(command)>3 or len(command)<2 :
            print("no such command")
            return
        if len(command)==3:
            if command[2][0]=='@':
                name=command[2][1:]
            else:
                print("no such command")
                return
        else:
            name = 'seq{}'.format(New.__name_giver)
            New.__name_giver += 1
        try:
            self.get_sequence_data().add_data(name,New.__id_giver,command[1])
            print("[{}] {}: {}".format(self.__id_giver, name,command[1]))
            New.__id_giver+=1
        except(Exception):
            print("could not add sequence")
        return





