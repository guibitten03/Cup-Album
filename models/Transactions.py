from Shop import Shop
from Collector import Collector

class Transactions():

    def __init__(self, price: float) -> None:
        self.__price__ = price

    def set_price(self, price: float) -> None:
        self.__price__ = price

    def get_price(self) -> float:
        return self.__price__

    def buy(self, c: Collector, s: Shop, quantidade: int) -> str:

        if c.get_money() < quantidade*self.get_price():
            return f"Não foi possivel finalizar a compra, Colecionador {c.get_name()} não possui dinheiro suficiente"

        if s.get_stock() < quantidade:
            return f"Não foi possivel finalizar a compra, Loja {s.get_name()} não possui dinheiro suficiente"

        c.set_money(c.get_money() - quantidade*self.get_price())
        c.set_count_packages(c.get_count_packages() + quantidade)

        s.set_stock(s.get_stock() - quantidade )

        return f"Compra realizada com sucesso"

    def trade(Collector, Collctor ):
        pass



