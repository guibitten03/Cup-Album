from Class_interface import Interface
from Collector_interface import CollectorInterface
from tkinter import *

class HomeInterface(Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent
        self.Home = Frame(self.parent)

        self.parent.title('Cup Album')
        
        self.Sticker = CollectorInterface(parent, 'Sticker', self)
        self.Collector = CollectorInterface(parent, 'Collector', self)
        self.Album = CollectorInterface(parent, 'Album', self)
        self.Trade = CollectorInterface(parent, 'Trade', self)
        
        self.home()
        
    def home(self):

        self.Home.grid()

        self.msg1 = Label(self.Home, text='Cup Album')
        self.msg1.grid(row=0,columnspan=5)

        self.to_sticker = Button(self.Home, text="Sticker", fg="red")
        self.to_sticker.bind("<Button-1>", lambda event, future_frame=self.Sticker.Home: self.muda_tela(event, future_frame))
        self.to_sticker.grid(row=1, column=0)

        self.to_collector = Button(self.Home, text="Collector", fg="red")
        self.to_collector.bind("<Button-1>", lambda event, future_frame=self.Collector.Home: self.muda_tela(event, future_frame))
        self.to_collector.grid(row=1,column=1)

        self.to_album = Button(self.Home, text="Album", fg="red")
        self.to_album.bind("<Button-1>", lambda event, future_frame=self.Album.Home: self.muda_tela(event, future_frame))
        self.to_album.grid(row=1,column=2)

        self.to_trade = Button(self.Home, text="Trade", fg="red")
        self.to_trade.bind("<Button-1>", lambda event, future_frame=self.Trade.Home: self.muda_tela(event, future_frame))
        self.to_trade.grid(row=1,column=3)

        self.exit = Button(self.Home, text="Exit", fg="red", command=self.parent.quit)
        self.exit.grid(row=1,column=4)

    def muda_tela(self, event, future_frame):
        self.Home.grid_forget()
        future_frame.grid()

if __name__ == '__main__':
    root = Tk()

    m = HomeInterface(root)
    m.grid()

    m.mainloop()