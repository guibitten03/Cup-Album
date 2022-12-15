from models import *
from persistence import *
from utilities import check_type


class AlbumPersistence(Persistence):
    albuns: dict[int, Album] = dict()

    def __init__(self) -> None:
        self.load()

    def insert(self, e: Entity) -> None:
        check_type(e, Album)

        AlbumPersistence.albuns[e.id] = e

    def remove(self, e: Entity) -> bool:
        check_type(e, Album)

        if e.id in AlbumPersistence.albuns:
            AlbumPersistence.albuns.pop(e.id)
            return True

        return False

    def modify(self, e: Entity) -> bool:
        check_type(e, Album)
        
        if e.id in AlbumPersistence.albuns.keys():
            AlbumPersistence.albuns[e.id] = e
            return True
        
        return False

    def search_by_id(self, id : int) -> Entity:
        if id in AlbumPersistence.albuns:
            return AlbumPersistence.albuns[id]
        return None

    def search_by_str(self, s : str) -> Entity:
        for _, album in AlbumPersistence.albuns.items():
            if album.name == s:
                return album
        return None

    def view_data(self)-> None:
        for _, album in AlbumPersistence.albuns.items():
            print(album)

    def save(self)-> bool:
        try:
            with open("data/album.csv", "w") as f:
                for _,a in AlbumPersistence.albuns.items():
                    string : str = ""
                    string += f"{a.id},{a.name},{a.colr.id},{a.colr.name}"
                    for player in a.album:
                        string += f",{player.id}"
                    string += "\n"
                    f.write(string)
            return True
        except:
            return False

    def load(self)  -> bool:

        try:
            AlbumPersistence.albuns.clear()
            with open("data/album.csv","a+") as f:
                f.seek(0)
                for line in f:
                    data = line.rstrip('\n').split(",")
                    
                    colr = Collector(id = data[2].strip(), name = data[3].strip())
                    
                    a = Album(id = int(data[0]), 
                              name = data[1], 
                              colr = colr)
                
                    for id_player in data[4:]:
                        a.stick(StickerPersistence.stickers[int(id_player.strip())])
                    self.insert(a)
            return True
        except:
            return False