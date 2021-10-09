from command import Command

class Load(Command):
    __name_giver = 1
    __id_giver = 1

    def execute(self,command):
        if len(command) > 3 or len(command) < 2:
            print("no such command")
            return
        if len(command) == 3:
            if command[2][0] == '@':
                name = command[2][1:]
            else:
                print("no such command")
                return
        else:
            name = command[1].split(".")[0]+"{}".format(Load.__name_giver)
            Load.__name_giver += 1
        try:
            f = open(command[1], "r",encoding='utf-8')
            seq = f.read()
            f.close()
            try:
                self.get_sequence_data().add_data(name, Load.__id_giver, seq)
                if len(seq)>40:
                    seq=seq[:33]+"..."+seq[-3:]
                print("[{}] {}: {}".format(self.__id_giver, name, seq))
                Load.__id_giver += 1
            except(Exception):
                print("could not load sequence")

        except(Exception):
            print("file not found")

        return
