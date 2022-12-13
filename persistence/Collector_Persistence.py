from models import *
from persistence import *
from utilities import check_type

class CollectorPersistence(Persistence):
    collectors: dict[int, Collector] = dict()

    def __init__(self) -> None:
        self.load()

    def insert(self, e : Entity) -> None:
        check_type(e, Collector)

        CollectorPersistence.collectors[e.id] = e

    def remove(self, e: Entity) -> bool:
        check_type(e, Collector)

        if e.id in CollectorPersistence.collectors:
            CollectorPersistence.collectors.pop(e.id)
            return True
        return False

    def modify(self, e: Entity) -> bool:
        check_type(e, Collector)

        if e.id in CollectorPersistence.collectors.key():
            CollectorPersistence.collectors[e.id] = e
            return True
        return False

    def search_by_id(self, id : int) -> Collector:
        if id in CollectorPersistence.collectors:
            return CollectorPersistence.collectors[id]
        return None

    def search_by_str(self, s: str) -> Collector:        
        for _,clt in CollectorPersistence.collectors.items():
            if clt.name == s:
                return clt
        return None

    def view_data(self)-> None:
        for _,clt in CollectorPersistence.collectors.items():
            print(clt)

    def save(self) -> bool:
        try:
            with open("data/collector.csv", "w") as f:
                for _,c in CollectorPersistence.collectors.items():
                    f.write("{},{}\n".format(c.id,c.name))
            return True
        except:
            return False
    
    def load(self) -> bool:
        
        try:
            CollectorPersistence.collectors.clear()
            with open("data/collector.csv","a+") as f:
                f.seek(0)
                for line in f:
                    data = line.split(",")
                    c = Collector(data[1].rstrip(), id = int(data[0]))
                    self.insert(c)
            return True
        except:
            return False