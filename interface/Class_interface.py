from abc import ABC, abstractmethod

class Interface(ABC):

    def __init__(self, controle, home_interface) -> None:
        self.controle = controle
        self.home_interface = home_interface

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

    @abstractmethod
    def callback(self, P):
        pass

    @abstractmethod
    def muda_tela(self, event, current_frame, future_frame):
        pass

    @abstractmethod
    def insert_event(self, event, args):
        pass
    
    @abstractmethod
    def remove_event(self, event, text):
        pass

    @abstractmethod
    def modify_event(self, event, text):
        pass

    @abstractmethod
    def search_event(self, event, text):
        pass


