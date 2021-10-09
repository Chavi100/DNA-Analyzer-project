from  new import New
from dup import Dup
from  load import Load
from  batch import Batch
from  batchlist import Batchlist
from batchshow import Batchshow


class Controller:

    def __init__(self):
        self.__controller_dict={
            "new":New,
            "load":Load,
            "dup":Dup,
            "batch":Batch,
            "batchlist":Batchlist,
            "batchshow":Batchshow
        }

    def get_controller(self,kind_of_command):
        try:
            return self.__controller_dict[kind_of_command]()
        except(Exception):
            raise







