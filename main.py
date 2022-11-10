import os

from interface.command_line import command_lines
from persistence import *


def main():
    os.makedirs("data", exist_ok=True)

    StickerPersistence.load()
    AlbumPersistence.load()
    CollectorPersistence.load()
    TradePersistence.load()

    command_lines.home()

    AlbumPersistence.save()
    CollectorPersistence.save()
    StickerPersistence.save()
    TradePersistence.save()

if __name__ == '__main__':
    main()