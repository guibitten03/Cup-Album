from Entity import Entity
from datetime import datetime

class Sticker(Entity):

    id: int = 0

    def __init__(self, name, birth_date, team, height, weight, position) -> None:
        super().__init__(Sticker)

        self.name: str = name
        self.team: str = team
        self.position: str = position


    def __str__(self) -> None:
        return "{}, {}, {}".format(self.name, self.team, self.position)