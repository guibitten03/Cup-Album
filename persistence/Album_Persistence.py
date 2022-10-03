import json
from models.Album import Album
from persistence.Persistence import IPersistence

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
    def modify(id : int, name : str, owner : str) -> None:
        if id in AlbumPersistence.albuns:
            AlbumPersistence.albuns[id].name = name
            AlbumPersistence.albuns[id].owner = owner

    @staticmethod
    def search_by_id(id : int) -> Album:
        if id in AlbumPersistence.albuns:
            return AlbumPersistence.albuns[id]
        return None

    @staticmethod
    def search_by_str(name : str) -> Album:        
        for _, s in AlbumPersistence.albuns.items():
            if s.name == name:
                return s
        return None
    
    @staticmethod
    def view_data()-> None:
        for _, s in AlbumPersistence.albuns.items():
            print(s)
    
    @staticmethod
    def save():
        with open("album.txt", "w") as f:
            for album in AlbumPersistence.albuns:
                json.dumps(album, f)

    @staticmethod
    def load():
        AlbumPersistence.albuns.clear()
        with open("album.txt") as f:
            AlbumPersistence.albuns = json.loads(f)
            
            

