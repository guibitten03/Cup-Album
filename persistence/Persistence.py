from abc import ABC, abstractmethod

from models import *


class Persistence(ABC):

    @abstractmethod
    def insert(e: Entity) -> None:
        pass

    @abstractmethod
    def modify(e: Entity) -> None:
        pass

    @abstractmethod
    def remove(e: Entity) -> None:
        pass

    @abstractmethod
    def save() -> None:
        pass

    @abstractmethod
    def load() -> None:
        pass

    @abstractmethod
    def view_data() -> None:
        pass

    @abstractmethod
    def search_by_id(id: int):
        pass

    @abstractmethod
    def search_by_str(s: str):
        pass