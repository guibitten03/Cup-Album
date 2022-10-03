from persistence.Persistence import IPersistence

class StickerPersistence():
    #pra facilitar no menu deixa esses atributos estaticos 👍
    teams = ['Brasil', 'Argentina', '...'] #lista com o nome dos times
    position = ['atacante', 'meia-direita', 'goleiro', '...'] 

    
    def insert(self, x, y, z):
        print("função insert")

    def remove(self, x):
        print("função remove")

    def modify(self, team_modify: str = None, position_modify: str = None, name_modify: str = None):
        print("função modify")

    def search_by_id(self, id):
        print("função search")
        return 1 #retorna o obj ou None se não existir
