from operator import ne
from Entity import Entity
from datetime import datetime

class Sticker(Entity):

    id: int = 0

    def __init__(self, name, team, position) -> None:
        super().__init__(Sticker)

        self.name: str = name
        self.team: str = team
        self.position: str = position


    def get_time(self) -> str: return self.team
    def get_name(self) -> str: return self.name
    def get_position(self) -> str: return self.position
    
    def set_time(self, team) -> None: self.team = team
    def set_name(self, name) -> None: self.name = name
    def set_position(self, position) -> None: self.position

    def __str__(self) -> None:
        return "{}, {}, {}".format(self.name, self.team, self.position)