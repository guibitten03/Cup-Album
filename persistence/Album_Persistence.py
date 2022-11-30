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

    def remove(self, e: Entity) -> None:
        check_type(e, Album)

        if e.id in AlbumPersistence.albuns:
            AlbumPersistence.albuns.pop(e.id)

    def modify(self, e: Entity) -> None:
        check_type(e, Album)

        AlbumPersistence.albuns[e.id] = e

    def search_by_id(self, id : int) -> Album:
        if id in AlbumPersistence.albuns:
            return AlbumPersistence.albuns[id]
        return None

    def search_by_str(self, s : str) -> Album:
        for _, album in AlbumPersistence.albuns.items():
            if album.name == s:
                return album
        return None

    def view_data(self)-> None:
        for _, album in AlbumPersistence.albuns.items():
            print(album)


    def save(self):
        with open("data/album.csv", "w") as f:
            for _,a in AlbumPersistence.albuns.items():
                string : str = ""
                string += f"{a.id},{a.name},{a.owner}"
                for player in a.album:
                    string += f",{player.id}"
                string += "\n"
                f.write(string)

    def load(self):
        AlbumPersistence.albuns.clear()
        with open("data/album.csv","a+") as f:
            f.seek(0)
            for line in f:
                data = line.split(",")
                a = Album(id = int(data[0]),
                          name = data[1].strip(),
                          owner = data[2].strip())
                for id_player in data[3:]:
                    a.stick(StickerPersistence.stickers[int(id_player.strip())])
                self.insert(a)
