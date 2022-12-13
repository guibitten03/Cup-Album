from controle import Controle
from persistence.Album_Persistence import AlbumPersistence

class AlbumControle(Controle):

    def __init__(self) -> None:
        super().__init__(AlbumPersistence())