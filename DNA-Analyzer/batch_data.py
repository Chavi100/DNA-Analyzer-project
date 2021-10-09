

class Batch_Data():
    __instance = None

    def __new__(cls, *args, **kwargs):
        if Batch_Data.__instance == None:
            Batch_Data.__instance = object.__new__(cls)
        return Batch_Data.__instance

    def __init__(self):
        self.__batch_dict={}


    def get_batch_dict(self):
        return self.__batch_dict

    def add_batch(self,name,batch):
        self.__batch_dict[name]=batch


