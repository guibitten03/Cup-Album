from Shop import Shop
from models.Pessoa import Collector

class Transactions():

    def __init__(self, price: float) -> None:
        self.__price__ = price
        #troca dois colecionadores 
        #

    def set_price(self, price: float) -> None:
        self.__price__ = price

    def get_price(self) -> float:
        return self.__price__

    def buy(self, c: Collector, s: Shop, quantidade: int) -> str:

        if c.get_money() < quantidade*self.get_price() or s.get_stock() < quantidade:
            return "Não foi possivel finalizar a compra"

        c.set_money(c.get_money() - quantidade*self.get_price())
        c.set_count_packages(c.get_count_packages() + quantidade)

        s.set_stock(s.get_stock() - quantidade )

        return f"Compra realizada com sucesso"
#separar metodos
    def trade(c1: Pessoa, s_id_1: int, s_id_2: int) -> str:
        
        if c1.stiker_in_not_stickeds(s_id_1_to_2) == 0 or c2.stiker_in_not_stickeds(s_id_2_to_1):
            return "Não foi possivel realizar a troca"

        stiker = c1.remove_not_stickeds(s_id_1_to_2)
        c2.add_not_stickeds(stiker) #stiker sendo objeto de Stiker

        stiker = c2.remove_not_stickeds(s_id_2_to_1)
        c1.add_not_stickeds(stiker) #stiker sendo objeto de Stiker

        return "Troca realizada com sucesso"

