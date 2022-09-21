from xml.dom.minidom import Entity

class Package(Entity):
    def __init__(self) -> None:
        super().__init__()

        self.stickers = []
        self.nb_stickers = 5


    def open(self) -> list:
        return self.stickers