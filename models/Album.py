from models import *


class Album(Entity):

    def __init__(self, name: str, owner: str, **kwargs) -> None:
        super().__init__(Album, **kwargs)

        self.name: str = name.strip()
        self.owner = owner # self.owner: Collector = owner
        self.album: list[Sticker] = list()
        # self.album_size = 0

    def stick(self, sticker) -> None:
        self.album.append(sticker)
        # self.album_size += 1

    def remove_sticker(self, name: str, team: str, position: str) -> None:
        for index, sticker in enumerate(self.album):
            if sticker.name == name:
                if sticker.team == team:
                    if sticker.position == position:
                        self.album.pop(index)
                        # self.album_size -= 1
                        return True

    def sticker_in_album(self, name: str, team: str, position: str) -> bool:
        for sticker in self.album:
            if sticker.name == name:
                if sticker.team == team:
                    if sticker.position == position:
                        return True
        return False

    def get_album_name(self) -> str:
        return self.name

    def get_album_owner(self) -> str:
        return self.owner

    def get_album(self) -> list[Sticker]:
        return self.album

    # def get_album_size(self) -> int:
    #   return self.album_size

    def set_album_name(self, name: str) -> str:
        self.name = name

    def set_album_owner(self, owner: str) -> str:
        self.owner = owner

    def set_album(self, album: list[Sticker]):
        self.album = album

    # def set_album_size(self, size):
    #   self.album_size = size

    def __str__(self):
        string = f"Id: {self.id}| Collector Id: {self.owner}| Album Name: {self.name}\nStickers: "

        for index, player in enumerate(self.album):
            if index == (len(self.album) - 1):
                string += f"{player.id}";
                break
            string += f" {player.id},"

        return string