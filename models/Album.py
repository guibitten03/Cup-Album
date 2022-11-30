from models import *


class Album(Entity):

    def __init__(self, name: str, colr: Collector, **kwargs) -> None:
        super().__init__(Album, **kwargs)

        self.name: str = name.strip()
        self.colr = colr
        self.album: list[Sticker] = list()

    def stick(self, stk: Sticker) -> None:
        self.album.append(stk)

    def remove_sticker(self,stk: Sticker, name: str, team: str, position: str) -> None:
        
        if stk in self.album:
            self.album.remove(stk)
        # for index, stk in enumerate(self.album):
        #     if stk.name == name:
        #         if stk.team == team:
        #             if stk.position == position:
        #                 self.album.pop(index)
        #                 return True

    def sticker_in_album(self, stk: Sticker, name: str, team: str, position: str) -> bool:
        
        return stk in self.album
        
        # for stk in self.album:
        #     if stk.name == name:
        #         if stk.team == team:
        #             if stk.position == position:
        #                 return True
        # return False

    def get_name(self) -> str:
        return self.name

    def get_colr(self) -> Collector:
        return self.colr

    def get_album(self) -> list[Sticker]:
        return self.album

    # def get_album_size(self) -> int:
    #   return self.album_size

    def set_name(self, name: str) -> None:
        self.name = name

    def set_colr(self, colr: Collector) -> None:
        self.colr = colr

    def set_album(self, album: list[Sticker]):
        self.album = album

    # def set_album_size(self, size):
    #   self.album_size = size

    def __str__(self):
        string = f"Id: {self.id}| Collector Id: {self.colr.id}| Album Name: {self.name}\nStickers: "

        for index, player in enumerate(self.album):
            if index == (len(self.album) - 1):
                string += f"{player.id}";
                break
            string += f" {player.id},"

        return string