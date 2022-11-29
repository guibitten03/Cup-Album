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
    def modify(self, e: Entity) -> None:
        pass

    @abstractmethod
    def remove(self, e: Entity) -> None:
        pass

    @abstractmethod
    def save(self) -> None:
        pass

    @abstractmethod
    def load(self) -> None:
        pass

    @abstractmethod
    def view_data(self) -> None:
        pass

    @abstractmethod
    def search_by_id(self, id: int):
        pass

    @abstractmethod
    def search_by_str(self, s: str):
        pass
