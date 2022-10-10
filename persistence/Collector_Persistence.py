from models import Collector
from persistence import IPersistence

class CollectorPersistence(IPersistence):

    collectors = dict()

    @staticmethod
    def insert(c : Collector) -> None:
        CollectorPersistence.collectors[c.id] = c
    
    @staticmethod
    def remove(id : int) -> None:
        if id in CollectorPersistence.collectors:
            CollectorPersistence.collectors.pop(id)
    
    @staticmethod
    def modify(id : int, name : str) -> None:
        if id in CollectorPersistence.collectors:
            CollectorPersistence.collectors[id].name = name

    @staticmethod
    def search_by_id(id : int) -> Collector:
        if id in CollectorPersistence.collectors:
            return CollectorPersistence.collectors[id]
        return None

    @staticmethod
    def search_by_str( name : str) -> Collector:        
        for _,c in CollectorPersistence.collectors.items():
            if c.name == name:
                return c
        return None
    
    @staticmethod
    def view_data()-> None:
        for _,c in CollectorPersistence.collectors.items():
            print(c)
    
    @staticmethod
    def save():
        with open("collector.txt", "w") as f:
            for _,c in CollectorPersistence.collectors.items():
                f.write("{},{}\n".format(c.id,c.name))

    @staticmethod
    def load():
        CollectorPersistence.collectors.clear()
        with open("collector.txt","a+") as f:
            f.seek(0)
            for line in f:
                data = line.split(",")
                c = Collector(data[1].rstrip(),id = int(data[0]))
                CollectorPersistence.insert(c)