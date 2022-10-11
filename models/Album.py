import numpy as np
from models.Entity import Entity
from models.Sticker import *


class Album(Entity):

    def __init__(self, name, owner, **kwargs) -> None:
        super().__init__(Album, **kwargs)

        self.name = name
        self.owner = owner
        self.album = []
        # self.album = {}
        # self.positions = self.init_position_dict()
        self.album_size = 0
        # self.positions_label = ['Goalkeeper', 'Defender', 'Midfielder', 'Foward']
        # self.max_size_positions_allowed = [1, 4, 3, 3]
        # self.positions = self.define_default_positions()


    # def define_default_positions(self):
    #     positions = {}

    #     max_allowed = 0
    #     for position in self.positions_label:
    #         positions[position] = 0, self.max_size_positions_allowed[max_allowed]
    #         max_allowed += 1 
            
    #     return positions


    # def init_position_dict(self):
    #     positions_size = {}
    #     sizes = [1,4,3,3]

    #     index = 0
    #     for position in Sticker.positions:
    #         positions_size[position] = [0, sizes[index]]
    #         index += 1
    #     return positions_size


    def stick(self, sticker) -> None:
        # if not (sticker.team in self.album.keys()):
        #     self.album[sticker.team] = [self.positions.copy(), sticker]
        #     self.album[sticker.team][sticker.position][0] += 1
        # else:
        #     if self.album[sticker.team][sticker.position][0] == self.album[sticker.team][sticker.position][1]:
        #         print(f"There is not more spaces to {sticker.position}s in {sticker.team}")
        #         return  
            
        #     self.album[sticker.team].append(sticker)
        #     self.album[sticker.team][sticker.position][0] += 1

        # self.album_size += 1
        self.album.append(sticker)
        self.album_size += 1

        
    def remove_sticker(self, name, team, position) -> None:
        # if not len(self.album[team]) > 0: 
        #     print(f"There are any players in {team}...")
        #     return False
        # if not self.album[team][position][0] > 0:
        #     print(f"There are any {position}s in {team}...")
        #     return False
        
        # index_player : int
        # for player in range(2, len(self.album[team][position])):
        #     if self.album[team][position][player].name == name:
        #         index_player = player
        #         break
        #     if player == (len(self.album[team][position]) - 1):
        #         print(f"There are any player with name {name}...")
        #         return False
            
        # self.album[team][position].pop(index_player)
        # self.album[team][position][0] -= 1
        # self.album_size -= 1
        index = 0
        for player in self.album:
            if player.name == name:
                if player.team == team:
                    if player.position == position:
                        self.album.pop(index)
                        self.album_size += 1
                        return True

            index += 1
        print(f"There is not player {name}, from {team}, of {position} in album")



    def sticker_in_album(self, name, team, position) -> bool:
        for player in self.album:
            if player.name == name:
                if player.team == team:
                    if player.position == position:
                        return True
        return None
            # if not len(self.album[team]) > 0: 
            #     print(f"\n    There are any players in {team}...")
            #     return None
            # if not self.album[team][position][0] > 0:
            #     print(f"\n    There are any {position}s in {team}...")
            #     return None
            
            # index_player : int
            # for player in range(2, len(self.album[team][position])):
            #     if self.album[team][position][player].name == name:
            #         index_player = player
            #         break
            #     if player == (len(self.album[team][position]) - 1):
            #         print(f"\n    There are any player with name {name}...")
            #         return None
                
            # return self.album[team][position][index_player]

                
                
    # def show_album(self):
    #     for team in self.album.keys():
    #         print(f"{team}:")
    #         for position in self.album[team].keys():
    #             if len(self.album[team][position]) > 2:
    #                 print(f"\t{position}s:")
    #                 string = ""
    #                 for player in range(2, len(self.album[team][position])):
    #                     string = string + '\t' + self.album[team][position][player].name
    #                 print(string + '\n')
                

    def get_album_name(self) -> str: return self.name
    def get_album_owner(self) -> str: return self.owner
    def get_album(self): return self.album
    def get_album_size(self): return self.album_size
    
    def set_album_name(self, name) -> str: self.name = name
    def set_album_owner(self, owner) -> str: self.owner = owner
    def set_album(self, album): self.album = album
    def set_album_size(self, size): self.album_size = size
    

    def __str__(self):
        return f"{self.id}, {self.owner}, {self.name}"