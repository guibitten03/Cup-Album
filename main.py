import os
from tkinter import *
from persistence import *
from controle import *
from models import *
from interface import *

def main():
    os.makedirs("data", exist_ok=True)

    root = Tk()

    m = HomeInterface(root)
    m.grid()

    m.mainloop()

if __name__ == '__main__':
    main()