from Emtity import Emtity
from Shop import Shop
from Collector import Collector

class Transactions():

    def __init__(self, price: float) -> None:
        self.__price__ = price

    def set_price(self, price: float) -> None:
        self.__price__ = price

    def get_price(self) -> float:
        return self.__price__

    def buy(self, C: Collector, s: Shop, quantidade: int) -> str:

        if(c.get_money < quantidade*self.get_price):
            return f"Não foi possivel finalizar a compra, Colecionador {C.get_name} não possui dinheiro suficiente"
    
        c.set_money = c.get_money - quantidade*self.get_price
        c.set_count_packages = c.get_count_packages + quantidade 

        s.set_stock = s.set_stock - quantidade 

        return f"Compra tealizada com sucesso"

    def trade(Collector, Collector, ):



