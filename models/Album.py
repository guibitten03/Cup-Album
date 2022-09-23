from xml.dom.minidom import Entity
from Sticker import *


class Album(Entity):

    def __init__(self) -> None:
        super().__init__(Album)

        self.album = {}
        self.album_size = 0


    def stick(self, sticker) -> None:
        if not self.album[sticker.team]:
            self.album[sticker.team] = [sticker]

        else:
            self.album[sticker.team].append(sticker)

        self.album_size += 1

    def get_album(self): return self.album
    def get_album_size(self): return self.album_size
    
    def set_album(self, album): self.album = album
    def set_album_size(self, size): self.album_size = size

#     def menu(self):
#         input = int(input('''Selecione uma opção:\n
# 0 - Sair\n
# 1 - Olhar album\n
# 2 - Album está completo?'''))

#         while True:
#             match:
#                 case 0:
#                     break
#                 case 1:
#                     if self.album_size == 0:
#                         print("Você ainda não colou figurinhas no album")
#                     else:   
#                         for team in self.album.keys():
#                             for players in self.album[team]:
#                                 print("{}: {}".format(self.album[team]))

    def __str__(self) -> str:
        return "{} stickers are in album\n".format(self.album_size) 
    
    
if __name__ == "__main__":
    album = Album()
    print(album.album_size)