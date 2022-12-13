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

    def remove(self, e: Entity) -> bool:
        check_type(e, Sticker)

        if e.id in StickerPersistence.stickers:
            StickerPersistence.stickers.pop(e.id)
            return True
        
        return False

    def modify(self, e: Entity) -> bool:
        check_type(e, Sticker)

        if e.id in StickerPersistence.stickers.keys():
            StickerPersistence.stickers[e.id] = e
            return True
        return False

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


    def save(self) -> bool:
        try:
            with open("data/sticker.csv", "w") as f:
                for _, sticker in StickerPersistence.stickers.items():
                    f.write(f"{sticker.id},{sticker.name},{sticker.team},{sticker.position}\n")
            return True
        except:
            return False
    def load(self) -> bool:
        try:
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
            return True
        except:
            return False