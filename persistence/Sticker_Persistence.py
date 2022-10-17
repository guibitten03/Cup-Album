import json
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
    def modify(id : int, name : str = "", team = "", position = "") -> None:
        sticker = StickerPersistence.stickers[id]
        if id in StickerPersistence.stickers:
            sticker.name = name if name != "" else sticker.name
            sticker.team = team if team != "" else sticker.team
            sticker.position = position if position != "" else sticker.position

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
        with open("data/sticker.csv", "w") as f:
            for _,sticker in StickerPersistence.stickers.items():
                f.write(f"{sticker.id},{sticker.name},{sticker.team},{sticker.position}\n")

    @staticmethod
    def load():
        StickerPersistence.stickers.clear()
        with open("data/sticker.csv","a+") as f:
            f.seek(0)
            for line in f:
                data = line.split(",")
                c = Sticker(id = int(data[0]), 
                            name = data[1].strip(), 
                            team = data[2].strip(), 
                            position = data[3].strip())
                StickerPersistence.insert(c)
