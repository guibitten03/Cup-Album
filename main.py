import os

from interface.command_line import CLI
from persistence import *


def main():
    os.makedirs("data", exist_ok=True)

    sp_inst = StickerPersistence()
    ap_inst = AlbumPersistence()
    cp_inst = CollectorPersistence()
    tp_inst = TradePersistence()

    CLI.home(sp=sp_inst, ap=ap_inst, cp=cp_inst, tp=tp_inst)

    sp_inst.save()
    ap_inst.save()
    cp_inst.save()
    tp_inst.save()

if __name__ == '__main__':
    main()