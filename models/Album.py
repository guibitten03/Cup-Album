from Entity import Entity
from Sticker import *


class Album(Entity):

    def __init__(self, name, owner) -> None:
        super().__init__(Album)

        self.name = name
        self.owner = owner
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
        
    def remove_sticker(self, name, team, position) -> None:
        if not len(self.album[team]) > 0: 
            print(f"There are any players in {team}...")
            return
        if not self.album[team][position][0] > 0:
            print(f"There are any {position}s in {team}...")
            return 
        
        index_player : int
        for player in range(2, len(self.album[team][position])):
            if self.album[team][position][player].name == name:
                index_player = player
                break
            if player == (len(self.album[team][position]) - 1):
                print(f"There are any player with name {name}...")
                return
            
        self.album[team][position].pop(index_player)
        self.album[team][position][0] -= 1
        self.album_size -= 1
                
                
    def show_album(self):
        for team in self.album.keys():
            print(f"{team}:")
            for position in self.album[team].keys():
                if len(self.album[team][position]) > 2:
                    print(f"\t{position}s:")
                    string = ""
                    for player in range(2, len(self.album[team][position])):
                        string = string + '\t' + self.album[team][position][player].name
                    print(string + '\n')
                

    def get_album_name(self) -> str: return self.name
    def get_album_owner(self) -> str: return self.owner
    def get_album(self): return self.album
    def get_album_size(self): return self.album_size
    
    def set_album_name(self, name) -> str: self.name = name
    def set_album_owner(self, owner) -> str: self.owner = owner
    def set_album(self, album): self.album = album
    def set_album_size(self, size): self.album_size = size
    

    def __str__(self) -> str:
        return "{} stickers are in album\n".format(self.album_size) 
    
    
if __name__ == "__main__":
    album = Album('Grande', 'Homem')
    
    s1 = Sticker('Gui', 'Brazil', 'Foward')
    s2 = Sticker('Gui', 'Brazil', 'Foward')
    s3 = Sticker('Gui', 'Brazil', 'Foward')
    s4 = Sticker('Gui', 'Brazil', 'Midfilder')
    s5 = Sticker('Gui', 'Brazil', 'Midfilder')
    s6 = Sticker('Gui', 'Brazil', 'Midfilder')
    s7 = Sticker('Gui', 'Brazil', 'Defender')
    s8 = Sticker('Gui', 'Brazil', 'Defender')
    s9 = Sticker('Gui', 'Brazil', 'Defender')
    s10 = Sticker('Gui', 'Brazil', 'Defender')
        
    album.stick(s1)
    album.stick(s2)
    album.stick(s3)
    album.stick(s4)
    album.stick(s5)
    album.stick(s6)
    album.stick(s7)
    album.stick(s7)
    album.stick(s8)
    album.stick(s9)
    album.stick(s10)
    album.show_album()