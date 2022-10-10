from models.Entity import Entity

class Sticker(Entity):

    teams = ['Brasil', 'Argentina', '...'] 
    positions = ['Goalkeeper', 'Defender', 'Midfilder', 'Foward']

    def __init__(self, name, team, position, **kwargs) -> None:
        super().__init__(Sticker, **kwargs)

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
        return "{}, {}, {}, {}".format(self.id, self.name, self.team, self.position)