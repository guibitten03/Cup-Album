from models import *


class Sticker(Entity):

    teams = [
        "England",   "Germany",      "Spain",          "Portugal",
        "Belgium",   "Sweden",       "Serbia",         "France",
        "Denmark",   "Switzerland",  "Iceland",        "Poland",
        "Croatia",   "Russia",       "Australia",      "Brazil",
        "Argentina", "Mexico",       "Colombia",       "Peru",
        "Uruguay",   "Costa Rica",   "Korea Republic", "Iran",
        "Morocco",   "Nigeria",      "Tunisia",        "Egypt",
        "Senegal",   "Saudi Arabia", "Japan",          "Panama",
    ]

    positions = [ "Goalkeeper", "Defender", "Midfilder", "Foward" ]

    def __init__(self, name: str, team: str, position: str, **kwargs) -> None:
        super().__init__(Sticker, **kwargs)

        self.name: str = name
        self.team: str = team
        self.position: str = position

    def get_time(self) -> str:
        return self.team

    def get_name(self) -> str:
        return self.name

    def get_position(self) -> str:
        return self.position

    def set_time(self, team: str) -> None:
        self.team = team

    def set_name(self, name: str) -> None:
        self.name = name

    def set_position(self, position: str) -> None:
        self.position = position

    def __str__(self) -> None:
        return "Id: {}| Name: {}| Team: {}| Position: {}".format(self.id, self.name, self.team, self.position)
