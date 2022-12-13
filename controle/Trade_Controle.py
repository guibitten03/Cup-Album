from controle import Controle
from persistence.Trade_Persistence import TradePersistence

class TradeControle(Controle):

    def __init__(self) -> None:
        super().__init__(TradePersistence())