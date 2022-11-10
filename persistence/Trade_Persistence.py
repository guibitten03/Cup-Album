from models import *
from persistence import *


class TradePersistence(Persistence):
    trades: dict[int, Trade] = dict()

    @staticmethod
    def insert(t : Trade) -> None:
        TradePersistence.trades[t.get_id()] = t

    @staticmethod
    def remove(id : int) -> None:
        if id in TradePersistence.trades:
            TradePersistence.trades.pop(id)

    @staticmethod
    def modify(id : int, c1: int = -1, c2: int = -1, s1: int = -1, s2: int = -1) -> None:
        if id in TradePersistence.trades:
            trade = TradePersistence.trades[id]
            trade.collector1 = c1 if c1 != -1 else trade.collector1
            trade.collector2 = c2 if c2 != -1 else trade.collector2
            trade.sticker1 = s1 if s1 != -1 else trade.sticker1
            trade.sticker2 = s2 if s2 != -1 else trade.sticker2

    @staticmethod
    def search_by_id(id: int) -> Trade:
        if id in TradePersistence.trades:
            return TradePersistence.trades[id]
        return None

    @staticmethod
    def search_by_str(date: str = "") -> Trade:
        for _, t in TradePersistence.trades.items():
            if t.date == date:
                return t
        return None

    @staticmethod
    def view_data()-> None:
        for _, t in TradePersistence.trades.items():
            print(t)

    @staticmethod
    def save():
        with open("data/trade.csv", "w") as f:
            for _, t in TradePersistence.trades.items():
                f.write(
                    "{},{},{},{},{},{}\n" \
                    .format(t.id, t.date, t.collector1, t.sticker1, t.collector2, t.sticker2)
                )

    @staticmethod
    def load():
        TradePersistence.trades.clear()
        with open("data/trade.csv", "a+") as f:
            f.seek(0)
            for line in f:
                data = line.split(",")
                t = Trade(
                    int(data[2]), int(data[3]), int(data[4]),
                    int(data[5]), data[1], id = int(data[0])
                )
                TradePersistence.insert(t)
