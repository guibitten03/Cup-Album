from models import *
from persistence import *
from utilities import check_type


class TradePersistence(Persistence):
    trades: dict[int, Trade] = dict()

    def __init__(self) -> None:
        self.load()

    def insert(self, e: Entity) -> None:
        check_type(e, Trade)

        TradePersistence.trades[e.id] = e

    def remove(self, e: Entity) -> bool:
        check_type(e, Trade)
        
        if e.id in TradePersistence.trades:
            TradePersistence.trades.pop(e.id)
            return True
        return False

    def modify(self, e: Entity) -> None:
        check_type(e, Trade)
        if e.id in TradePersistence.trades.keys():
            TradePersistence.trades[e.id] = e
            return True
        return False
    
    def search_by_id(self, id: int) -> Entity:
        if id in TradePersistence.trades:
            return TradePersistence.trades[id]
        return None

    def search_by_str(self, s: str = "") -> Entity:
        for _, t in TradePersistence.trades.items():
            if t.date == s:
                return t
        return None

    def view_data(self)-> None:
        for _, t in TradePersistence.trades.items():
            print(t)

    def save(self) -> bool:
        try:
            with open("data/trade.csv", "w") as f:
                for _, t in TradePersistence.trades.items():
                    f.write(
                        "{},{},{},{},{},{}\n" \
                        .format(t.id,t.date,t.colr1.id,t.stk1.id,t.colr2.id,t.stk2.id)
                    )
            return True
        except:
            return False

    def load(self) -> bool:

        try:
            TradePersistence.trades.clear()
            with open("data/trade.csv", "a+") as f:
                f.seek(0)
                for line in f:
                    data = line.split(",")
                    t = Trade(
                        CollectorPersistence.collectors[int(data[2])], StickerPersistence.stickers[int(data[3])], 
                        CollectorPersistence.collectors[int(data[4])], StickerPersistence.stickers[int(data[5])],
                        data[1], id = int(data[0])
                    )
                    self.insert(t)
            return True
        except:
            return False