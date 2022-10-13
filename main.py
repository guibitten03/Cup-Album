from typing import Collection
from interface.command_line import command_lines
from models.Album import Album
from persistence.Album_Persistence import AlbumPersistence
from persistence.Collector_Persistence import CollectorPersistence
from persistence.Sticker_Persistence import StickerPersistence
from persistence.Trade_Persistence import TradePersistence

def main():
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