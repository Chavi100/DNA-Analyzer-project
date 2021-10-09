from DnaSequence import DnaSequence

class Dna_Data:

    __instance=None

    def __new__(cls, *args, **kwargs):
        if  Dna_Data.__instance==None:
            Dna_Data.__instance = object.__new__(cls)
        return Dna_Data.__instance

    def __init__(self):
        self.__data_dict_by_id={}
        self.__data_dict_by_name = {}

    def get_data_by_id(self):
        return self.__data_dict_by_id

    def get_data_by_name(self):
        return self.__data_dict_by_name

    def add_data(self,name,id,sequence):
        try:
            dna_sequence=DnaSequence(sequence,name,id)
            self.__data_dict_by_id[id]=dna_sequence
            self.__data_dict_by_name[name]=dna_sequence
        except(Exception):
            raise



