import numpy as np
from models.Entity import Entity
from models.Sticker import *


class Album(Entity):

    def __init__(self, name, owner, **kwargs) -> None:
        super().__init__(Album, **kwargs)

        self.name = name.strip()
        self.owner = owner
        self.album = []
        self.album_size = 0
 

    def stick(self, sticker) -> None:
        self.album.append(sticker)
        self.album_size += 1

        
    def remove_sticker(self, name, team, position) -> None:
        for index, player in enumerate(self.album):
            if player.name == name:
                if player.team == team:
                    if player.position == position:
                        self.album.pop(index)
                        self.album_size -= 1
                        return True


    def sticker_in_album(self, name, team, position) -> bool:
        for player in self.album:
            if player.name == name:
                if player.team == team:
                    if player.position == position:
                        return True
        return None
    

    def get_album_name(self) -> str: return self.name
    def get_album_owner(self) -> str: return self.owner
    def get_album(self): return self.album
    def get_album_size(self): return self.album_size
    
    def set_album_name(self, name) -> str: self.name = name
    def set_album_owner(self, owner) -> str: self.owner = owner
    def set_album(self, album): self.album = album
    def set_album_size(self, size): self.album_size = size
    

    def __str__(self):
        string = f"Id: {self.id}, Collector Id: {self.owner}, Album Name: {self.name}\nStickers: "
        for index, player in enumerate(self.album):
            if index == (self.album_size - 1): string += f"{player.id}"; break
            string += f" {player.id},"
        return string