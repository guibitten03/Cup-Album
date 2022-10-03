from models.Sticker import Sticker
from persistence.Persistence import IPersistence

class StickerPersistence(IPersistence):
    
    stickers = dict()

    @staticmethod
    def insert(s: Sticker) -> None:
        StickerPersistence.stickers[s.id] = s
    
    @staticmethod
    def remove(id : int) -> None:
        if id in StickerPersistence.stickers:
            StickerPersistence.stickers.pop(id)
    
    @staticmethod
    def modify(id : int, name : str) -> None:
        if id in StickerPersistence.stickers:
            StickerPersistence.stickers[id].name = name

    @staticmethod
    def search_by_id(id : int) -> Sticker:
        if id in StickerPersistence.stickers:
            return StickerPersistence.stickers[id]
        return None

    @staticmethod
    def search_by_str(name : str) -> Sticker:        
        for _, s in StickerPersistence.stickers.items():
            if s.name == name:
                return s
        return None
    
    @staticmethod
    def view_data()-> None:
        for _, s in StickerPersistence.stickers.items():
            print(s)
    
    @staticmethod
    def save():
        with open("collector.txt", "w") as f:
            for _,s in StickerPersistence.stickers.items():
                f.write("{},{}\n".format(s.id, s.name))

    @staticmethod
    def load():
        StickerPersistence.stickers.clear()
        with open("sticker.txt","a+") as f:
            f.seek(0)
            for line in f:
                data = line.split(",")
                c = Sticker(data[1].rstrip(),id = int(data[0]))
                StickerPersistence.insert(c)
