from models import *
from persistence import *


class StickerPersistence(Persistence):
    stickers: dict[int, Sticker] = dict()

    def __init__(self) -> None:
        self.load()

    def insert(self, e: Entity) -> None:
        if not (isinstance(e, Sticker)):
            raise Exception("Recived object is not of Sticker Type")

        StickerPersistence.stickers[e.id] = e

    def remove(self, e: Entity) -> None:
        if not (isinstance(e, Sticker)):
            raise Exception("Recived object is not of Sticker Type")

        if e.id in StickerPersistence.stickers:
            StickerPersistence.stickers.pop(e.id)

    def modify(self, e: Entity) -> None:
        if not (isinstance(e, Sticker)):
            raise Exception("Recived object is not of Sticker Type")

        StickerPersistence.stickers[e.id] = e

    def search_by_id(self, e: Entity) -> Sticker:
        if not (isinstance(e, Sticker)):
            raise Exception("Recived object is not of Sticker Type")

        if e.id in StickerPersistence.stickers:
            return StickerPersistence.stickers[e.id]
        return None

    def search_by_str(self, e: Entity) -> Sticker:
        if not (isinstance(e, Sticker)):
            raise Exception("Recived object is not of Sticker Type")

        for _, s in StickerPersistence.stickers.items():
            if s.name == e.name:
                return s
        return None

    def view_data(self)-> None:
        for _, s in StickerPersistence.stickers.items():
            print(s)

    def save(self) -> None:
        with open("data/sticker.csv", "w") as f:
            for _, sticker in StickerPersistence.stickers.items():
                f.write(f"{sticker.id},{sticker.name},{sticker.team},{sticker.position}\n")

    def load(self) -> None:
        StickerPersistence.stickers.clear()
        with open("data/sticker.csv","a+") as f:
            f.seek(0)
            for line in f:
                data = line.split(",")
                c = Sticker(id = int(data[0]), 
                            name = data[1].strip(), 
                            team = data[2].strip(), 
                            position = data[3].strip())
                self.insert(c)
