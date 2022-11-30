from models import *
from persistence import *
from utilities import check_type


class StickerPersistence(Persistence):
    stickers: dict[int, Sticker] = dict()

    def __init__(self) -> None:
        self.load()

    def insert(self, e: Entity) -> None:
        check_type(e, Sticker)

        StickerPersistence.stickers[e.id] = e

    def remove(self, e: Entity) -> None:
        check_type(e, Sticker)

        if e.id in StickerPersistence.stickers:
            StickerPersistence.stickers.pop(e.id)

    def modify(self, e: Entity) -> None:
        check_type(e, Sticker)

        StickerPersistence.stickers[e.id] = e

    def search_by_id(self, id : int) -> Sticker:
        if id in StickerPersistence.stickers:
            return StickerPersistence.stickers[id]
        return None

    def search_by_str(self, s: str) -> Sticker:
        for _, stk in StickerPersistence.stickers.items():
            if stk.name == s:
                return stk
        return None

    def view_data(self)-> None:
        for _, stk in StickerPersistence.stickers.items():
            print(stk)


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
