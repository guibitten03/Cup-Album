from Pessoa import Pessoa
from persistence import Persistence

class CollectorPersistence(Persistence):

    def __init__(self) -> None:
        self.collectors = [] #Lista de pessoas

    def insert(self, p : Pessoa) -> None:
        self.collectors.append(p)
    
    def delete(self, p : Pessoa) -> None:
        self.collectors.remove(p)
    
    def modify(self,id : int, name : str= "", money : float= -1) -> None:
        for i,p in enumerate(self.collectors):
            if p.id == id:
                p.name = name if name >= 0 else p.name 
                p.money = money if money >= 0 else p.money 

    def search_by_id(self, id : int) -> Pessoa:
        
        for p in self.collectors:
            if p.id == id:
                return p
        return NULL    
    
    def search_by_str(self, name : str) -> Pessoa:
        
        for p in self.collectors:
            if p.name == name:
                return p
        return NULL
    
    def save(collectors):
        f = open("collector.txt","a")
        for p in collectors:
            f.write("{}\t{}\t{}\t{}\t{}".format(
                p.id,p.name,p.money,p.count_packages,','.join(p.not_stickeds)))
        f.close()

    def load():
        load_collectors = Collectors()
        with open("collector.txt","r") as f:
            for line in f:
                data = line.split("\t")
                p = Pessoa(data[1],data[2])
                p.set_count_packages(data[3])
                p.set_not_stickeds(data[4].split(","))
                load_collectors.collectors.append(p)
        return load_collectors