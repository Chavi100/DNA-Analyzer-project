from command import Command

class Dup(Command):
    __name_giver = 1

    def execute(self,command):
        if len(command) > 3 or len(command) < 2:
            print("no such command")
            return
        if command[1][0] == '#':
            try:
                id=(int)(command[1][1:])
                seq=self.get_sequence_data().get_data_by_id()[id]
                seq_name = ""
                for key in self.get_sequence_data().get_data_by_name():
                    if self.get_sequence_data().get_data_by_name()[key] == seq:
                        seq_name = key
                if len(command) == 3:
                    if command[2][0] == '@':
                        name = command[2][1:]
                    else:
                        print("no such command")
                        return
                else:
                    name = seq_name + "_{}".format(self.__name_giver)
                    self.__name_giver += 1
                seq = seq + seq
                self.get_sequence_data().get_data_by_id()[command[1]] = seq
                self.get_sequence_data().get_data_by_name().pop(seq_name)
                self.get_sequence_data().get_data_by_name()[name]=seq
                print("[{}] {}: {}".format(id, name,seq))
            except(Exception):
                print("seq not found")
        else:
            print("not a valid command")


        return