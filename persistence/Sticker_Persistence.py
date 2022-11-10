from models import *
from persistence import *


class StickerPersistence(Persistence):
    stickers: dict[int, Sticker] = dict()

    def __init__(self) -> None:
        self.load()

    def insert(self, s: Sticker) -> None:
        StickerPersistence.stickers[s.id] = s

    def remove(self, id : int) -> None:
        if id in StickerPersistence.stickers:
            StickerPersistence.stickers.pop(id)

    def modify(self, id: int, name: str = "", team: str = "", position: str = "") -> None:
        sticker: Sticker = StickerPersistence.stickers[id]
        if id in StickerPersistence.stickers:
            sticker.name = name if name != "" else sticker.name
            sticker.team = team if team != "" else sticker.team
            sticker.position = position if position != "" else sticker.position

    def search_by_id(self, id: int) -> Sticker:
        if id in StickerPersistence.stickers:
            return StickerPersistence.stickers[id]
        return None

    def search_by_str(self, name: str) -> Sticker:
        for _, s in StickerPersistence.stickers.items():
            if s.name == name:
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
