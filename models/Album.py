from xml.dom.minidom import Entity
from Sticker import *
from database.

class Album(Entity):

    def __init__(self) -> None:
        super().__init__()

        self.album = {}
        self.album_size = 0


    def stick(self, sticker) -> None:
        if not self.album[sticker.team]:
            self.album[sticker.team] = [sticker]

        else:
            self.album[sticker.team].append(sticker)

        self.album_size += 1


    def __str__(self) -> str:
        return "{} stickers are in album\n".format(self.album_size) 