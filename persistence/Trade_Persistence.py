from models import *
from persistence import *


class TradePersistence(Persistence):
    trades: dict[int, Trade] = dict()

    def __init__(self) -> None:
        self.load()

    def insert(self, t: Trade) -> None:
        TradePersistence.trades[t.get_id()] = t

    def remove(self, id: int) -> None:
        if id in TradePersistence.trades:
            TradePersistence.trades.pop(id)

    def modify(self, id: int, c1: int = -1, c2: int = -1, s1: int = -1, s2: int = -1) -> None:
        if id in TradePersistence.trades:
            trade = TradePersistence.trades[id]
            trade.collector1 = c1 if c1 != -1 else trade.collector1
            trade.collector2 = c2 if c2 != -1 else trade.collector2
            trade.sticker1 = s1 if s1 != -1 else trade.sticker1
            trade.sticker2 = s2 if s2 != -1 else trade.sticker2

    def search_by_id(self, id: int) -> Trade:
        if id in TradePersistence.trades:
            return TradePersistence.trades[id]
        return None

    def search_by_str(self, date: str = "") -> Trade:
        for _, t in TradePersistence.trades.items():
            if t.date == date:
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
