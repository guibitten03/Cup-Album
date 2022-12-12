from abc import ABC, abstractmethod

class Interface(ABC):

    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def home(self) -> None:
        pass

    @abstractmethod
    def insert(self) -> None:
        pass

    @abstractmethod
    def remove(self) -> None:
        pass

    @abstractmethod
    def modify(self) -> None:
        pass

    @abstractmethod
    def search(self) -> None:
        pass

