from xml.dom.minidom import Entity
from datetime import datetime

class Sticker(Entity):

    id: int = 0

    def __init__(self, name, birth_date, team, height, weight, position) -> None:
        super().__init__()
        self.name: str = name
        birth_date: datetime = birth_date
        team: str = team
        height: float = height
        weight: float = weight
        position: str = position
        probability: float = 0.5


    def __str__(self) -> None:
        return "{}, {}, {}".format(self.name, self.team, self.position)