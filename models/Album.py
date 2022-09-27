from Entity import Entity
from Sticker import *


class Album(Entity):

    def __init__(self) -> None:
        super().__init__(Album)

        self.album = {}
        self.album_size = 0
        self.positions_label = ['Goalkeeper', 'Defender', 'Midfielder', 'Foward']
        self.max_size_positions_allowed = [1, 4, 3, 3]
        self.positions = self.define_default_positions()


    def define_default_positions(self):
        positions = {}

        max_allowed = 0
        for position in self.positions_label:
            positions[position] = 0, self.max_size_positions_allowed[max_allowed]
            max_allowed += 1 
            
        return positions


    def stick(self, sticker) -> None:

        if not self.album[sticker.team]:
            self.album[sticker.team] = [self.positions.copy(), sticker]
        else:
            if self.album[sticker.team][0][sticker.position][0] > self.album[sticker.team][0][sticker.position][1]:
                return f"Maximun of {sticker.position}s are achieved" 

            self.album[sticker.team].append(sticker)
            self.album[sticker.team][0][sticker.position][0] += 1

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
#             match(input):
#                 case 0:
#                     break
#                 case 1:
#                     if self.album_size == 0:
#                         print("Você ainda não colou figurinhas no album")
#                     else:   
#                         for team in self.album.keys():
#                             for players in self.album[team]:
#                                 print("{}: {}".format(self.album[team]))

    def __str__(self):
        album = Album()
        print(album.album_size)
    
if __name__ == "__main__":
    album = Album()
    sti = Sticker('Gui', 3, 'Brazil', 171, 65, 'Foward')
    
    album.stick(sti)
    print(album.album)