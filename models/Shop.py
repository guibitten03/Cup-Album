from xml.dom.minidom import Entity

from models.Transactions import Transactions


class Shop(Entity):

    def __init__(self) -> None:
        super().__init__()
        self.__stock = 100

    def get_stock(self):
        return self.__stock
    def set_stock(self,qtd : int):
        self.__stock = qtd
    
    def __str__(self) -> str:
        return "{}".format(self.__stock)
