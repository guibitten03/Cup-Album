from abc import ABC, abstractmethod
from persistence import Persistence
from models import Entity

class Controle(ABC):

    def __init__(self, p : Persistence) -> None:
        self.persistence = p
    
    def insert(self, e : Entity) -> None:
        self.persistence.insert(e)
    
    def remove(self, e : Entity) -> bool:
        return self.persistence.remove(e)
    
    def modify(self, e : Entity) -> bool:
        return self.persistence.modify(e)
    
    def search_by_id(self, id : int) -> Entity:
        return self.persistence.search_by_id(id)
    
    def search_by_str(self, s : str) -> Entity:
        return self.persistence.search_by_str(s)
    
    def load(self) -> bool:
        return self.persistence.load()
    
    def save(self) -> bool:
        return self.persistence.save()