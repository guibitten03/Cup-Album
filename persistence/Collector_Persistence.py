from models import *
from persistence import *


class CollectorPersistence(Persistence):
    collectors: dict[int, Collector] = dict()

    def __init__(self) -> None:
        self.load()

    def insert(self, c : Collector) -> None:
        CollectorPersistence.collectors[c.id] = c

    def remove(self, id : int) -> None:
        if id in CollectorPersistence.collectors:
            CollectorPersistence.collectors.pop(id)

    def modify(self, id : int, name : str) -> None:
        if id in CollectorPersistence.collectors:
            CollectorPersistence.collectors[id].name = name

    def search_by_id(self, id : int) -> Collector:
        if id in CollectorPersistence.collectors:
            return CollectorPersistence.collectors[id]
        return None

    def search_by_str(self, name : str) -> Collector:        
        for _,c in CollectorPersistence.collectors.items():
            if c.name == name:
                return c
        return None

    def view_data(self)-> None:
        for _,c in CollectorPersistence.collectors.items():
            print(c)

    def save(self):
        with open("data/collector.csv", "w") as f:
            for _,c in CollectorPersistence.collectors.items():
                f.write("{},{}\n".format(c.id,c.name))

    def load(self):
        CollectorPersistence.collectors.clear()
        with open("data/collector.csv","a+") as f:
            f.seek(0)
            for line in f:
                data = line.split(",")
                c = Collector(data[1].rstrip(), id = int(data[0]))
                self.insert(c)
