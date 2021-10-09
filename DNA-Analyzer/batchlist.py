from command import Command

class Batchlist(Command):

    def execute(self,command):
        names= self.get_batch_data().get_batch_dict().keys()
        for batch in names:
            print(batch)
        return