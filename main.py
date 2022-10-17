from genericpath import exists
from interface.command_line import command_lines
from persistence.Album_Persistence import AlbumPersistence
from persistence.Collector_Persistence import CollectorPersistence
from persistence.Sticker_Persistence import StickerPersistence
from persistence.Trade_Persistence import TradePersistence
import os
def main():

	os.makedirs("data",exist_ok=True)

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