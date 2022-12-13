from controle import Controle
from persistence.Sticker_Persistence import StickerPersistence

class StickerControle(Controle):

    def __init__(self) -> None:
        super().__init__(StickerPersistence())