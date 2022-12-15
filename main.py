import os
# from interface.command_line import CLI
from tkinter import *
from persistence import *
from controle import *
from models import *
from interface import *

def main():
    os.makedirs("data", exist_ok=True)

    # try:
    #     sp_inst = StickerPersistence()
    #     ap_inst = AlbumPersistence()
    #     cp_inst = CollectorPersistence()
    #     tp_inst = TradePersistence()
        
    # except Exception as e:
    #     print(f"Exception while trying to load file: {e}")

    root = Tk()

    m = HomeInterface(root)
    m.grid()

    m.mainloop()

    # try:
    #     sp_inst.save()
    #     ap_inst.save()
    #     cp_inst.save()
    #     tp_inst.save()
        
    # except Exception as e:
    #     print(f"Exception while trying to save file: {e}")

if __name__ == '__main__':
    main()