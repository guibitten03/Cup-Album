import json
from models import Album
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
        with open("album.txt", "w") as f:
            for _,a in AlbumPersistence.collectors.items():
                string = f"{a.id}, {a.name}, {a.owner},"
                for player in a.album:
                    string += str(player.id) + "|"
                f.write(string)

    @staticmethod
    def load():
        CollectorPersistence.collectors.clear()
        with open("collector.txt","a+") as f:
            f.seek(0)
            for line in f:
                data = line.split(",")
                c = Collector(data[1].rstrip(),id = int(data[0]))
                CollectorPersistence.insert(c)
            