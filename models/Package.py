from Entity import Entity

class Package(Entity):
    def __init__(self) -> None:
        super().__init__(Package)

        self.stickers = []
        self.nb_stickers = 5


    def open(self) -> list:
        # Sortear stickers
        return self.stickers

    def random_stickers(self) -> None: