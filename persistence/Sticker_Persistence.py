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
        with open("data/sticker.json", "w") as f:
            for album in StickerPersistence.stickers:
                json.dump(album, f)

    @staticmethod
    def load():
        StickerPersistence.stickers.clear()
        with open("data/sticker.json", "a+") as f:
            f.seek(0)
            for line in f:
                print(line)
            # StickerPersistence.stickers = json.loads(f.read())
