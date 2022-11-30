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

    def remove(self, e: Entity) -> None:
        check_type(e, Trade)
        
        if e.id in TradePersistence.trades:
            TradePersistence.trades.pop(e.id)

    def modify(self, e: Entity) -> None:
        check_type(e, Trade)
        TradePersistence.trades[e.id] = e
        
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

    def save(self) -> None:
        with open("data/trade.csv", "w") as f:
            for _, t in TradePersistence.trades.items():
                f.write(
                    "{},{},{},{},{},{}\n" \
                    .format(t.id, t.date, t.collector1, t.sticker1, t.collector2, t.sticker2)
                )

    def load(self) -> None:
        TradePersistence.trades.clear()
        with open("data/trade.csv", "a+") as f:
            f.seek(0)
            for line in f:
                data = line.split(",")
                t = Trade(
                    int(data[2]), int(data[3]), int(data[4]),
                    int(data[5]), data[1], id = int(data[0])
                )
                self.insert(t)
