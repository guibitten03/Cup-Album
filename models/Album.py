from Entity import Entity
from Sticker import *


class Album(Entity):

    def __init__(self) -> None:
        super().__init__(Album)

        self.album = {}
        self.positions_label = ['Goalkeeper', 'Defender', 'Midfilder', 'Foward']
        self.positions = self.init_position_dict()
        self.album_size = 0


    def init_position_dict(self):
        positions_size = {}
        sizes = [1,4,3,3]

        index = 0
        for position in self.positions_label:
            positions_size[position] = [0, sizes[index]]
            index += 1
        return positions_size


    def stick(self, sticker) -> None:
        if not (sticker.team in self.album.keys()):
            self.album[sticker.team] = self.positions

        else:
            if self.album[sticker.team][sticker.position][0] == self.album[sticker.team][sticker.position][1]:
                print(f"There is not more spaces to {sticker.position}s in {sticker.team}")
                return  
            
            self.album[sticker.team][sticker.position].append(sticker)
            self.album[sticker.team][sticker.position][0] += 1

        self.album_size += 1
                
                
    def show_album(self):
        for team in self.album.keys():
            print(f"{team}:")
            for position in self.album[team].keys():
                if len(self.album[team][position]) > 2:
                    print(f"{position}:")
                    for player in range(2, len(self.album[team][position])):
                        print(self.album[team][position][player])
                

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

    def __str__(self) -> str:
        return "{} stickers are in album\n".format(self.album_size) 
    
    
if __name__ == "__main__":
    album = Album()
    
    s1 = Sticker('Gui', 3, 'Brazil', 1, 2, 'Foward')
    s2 = Sticker('Gui', 3, 'Brazil', 1, 2, 'Foward')
    s3 = Sticker('Gui', 3, 'Brazil', 1, 2, 'Foward')
    s4 = Sticker('Gui', 3, 'Brazil', 1, 2, 'Foward')
    s5 = Sticker('Gui', 3, 'Brazil', 1, 2, 'Foward')
    album.stick(s1)
    album.stick(s2)
    album.stick(s3)
    album.stick(s4)
    album.stick(s5)
    album.show_album()