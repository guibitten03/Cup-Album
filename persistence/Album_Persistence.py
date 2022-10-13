import json
from models import Album
from models.Sticker import Sticker
from persistence.Persistence import IPersistence
from persistence.Sticker_Persistence import StickerPersistence

class AlbumPersistence(IPersistence):
    
    albuns = dict()

    @staticmethod
    def insert(a: Album) -> None:
        AlbumPersistence.albuns[a.id] = a
    
    @staticmethod
    def remove(id : int) -> None:
        if id in AlbumPersistence.albuns:
            AlbumPersistence.albuns.pop(id)
    
    @staticmethod
    def modify(id : int, name : str = "", owner : str = "") -> None:
        if id in AlbumPersistence.albuns:
            album = AlbumPersistence.albuns[id]
            album.name = name if name != "" else album.name
            album.owner = owner if owner != "" else album.owner

    @staticmethod
    def search_by_id(id : int) -> Album:
        if id in AlbumPersistence.albuns:
            return AlbumPersistence.albuns[id]
        return None

    @staticmethod
    def search_by_str(name : str) -> Album:        
        for _, album in AlbumPersistence.albuns.items():
            if album.name == name:
                return album
        return None
    
    @staticmethod
    def view_data()-> None:
        for _, album in AlbumPersistence.albuns.items():
            print(album)
    
    @staticmethod
    def save():
        with open("data/album.txt", "w") as f:
            for _,a in AlbumPersistence.albuns.items():
                string : str = ""
                string += f"{a.id}, {a.name}, {a.owner}"
                for player in a.album:
                    string += f", {player.id}"
                string += "\n"
                f.write(string)
                

    @staticmethod
    def load():
        AlbumPersistence.albuns.clear()
        with open("data/album.txt","a+") as f:
            f.seek(0)
            for line in f:
                data = line.split(",")
                a = Album(id = int(data[0]),
                          name = data[1].rstrip(),
                          owner = data[2].rstrip())
                for id_player in data[3:]:
                    a.stick(StickerPersistence.stickers[int(id_player.strip())])
                AlbumPersistence.insert(a)