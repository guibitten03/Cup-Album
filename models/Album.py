from models import *


class Album(Entity):

    def __init__(self, name: str, colr: Collector, **kwargs) -> None:
        super().__init__(Album, **kwargs)

        self.name: str = name.strip()
        self.colr = colr
        self.album: list[Sticker] = list()

    def stick(self, stk: Sticker) -> None:
        self.album.append(stk)

    def remove_sticker(self, stk: Sticker) -> None:
        if stk in self.album:
            self.album.remove(stk)

    def sticker_in_album(self, stk: Sticker) -> bool:
        return stk in self.album

    def get_name(self) -> str:
        return self.name

    def get_colr(self) -> Collector:
        return self.colr

    def get_album(self) -> list[Sticker]:
        return self.album

    def set_name(self, name: str) -> None:
        self.name = name

    def set_colr(self, colr: Collector) -> None:
        self.colr = colr

    def set_album(self, album: list[Sticker]):
        self.album = album

    def __str__(self):
        string = f"Id: {self.id}| Collector Id: {self.colr.id}| Album Name: {self.name}\nStickers: "

        for index, player in enumerate(self.album):
            if index == (len(self.album) - 1):
                string += f"{player.id}"
                break
            string += f" {player.id},"

        return string
