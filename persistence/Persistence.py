from abc import ABC, abstractmethod

from models import *

class Persistence(ABC):

    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def insert(self, e: Entity) -> None:
        pass

    @abstractmethod
    def modify(self, e: Entity) -> bool:
        pass

    @abstractmethod
    def remove(self, e: Entity) -> bool:
        pass

    @abstractmethod
    def save(self) -> bool:
        pass

    @abstractmethod
    def load(self) -> bool:
        pass

    @abstractmethod
    def view_data(self) -> None:
        pass

    @abstractmethod
    def search_by_id(self, id: int) -> Entity:
        pass

    @abstractmethod
    def search_by_str(self, s: str) -> Entity:
        pass