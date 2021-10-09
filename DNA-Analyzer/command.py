from dna_data import Dna_Data
from  batch_data import Batch_Data

class Command:

    __sequence_data=Dna_Data()
    __batch_data = Batch_Data()

    def get_batch_data(self):
        return Command.__batch_data

    def get_sequence_data(self):
        return Command.__sequence_data

    def execute(self,command):
        return