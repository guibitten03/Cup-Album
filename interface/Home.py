from interface import *
from controle import *
from tkinter import *
from models import *

class HomeInterface(Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent
        self.Home = Frame(self.parent)

        self.parent.title('Cup Album')
        
        self.cControle = CollectorControle()
        self.sControle = StickerControle()
        self.aControle = AlbumControle()
        self.tControle = TradeControle()
        
        self.Sticker = StickerInterface(parent, 'Sticker',self.sControle, self)
        self.Collector = CollectorInterface(parent, 'Collector', self.cControle, self)
        self.Album = AlbumInterface(parent, 'Album', self.cControle, self.sControle, self.aControle, self)
        self.Trade = TradeInterface(parent, 'Trade', self.cControle, self.sControle, self.tControle, self)

        self.home()
        
    def home(self):
        
        #Add mensagem de erro
        if not self.cControle.load():
            print("Erro ao carregar o arquivo")
        if not self.sControle.load():
            print("Erro ao carregar o arquivo")
        if not self.aControle.load():
            print("Erro ao carregar o arquivo")
        if not self.tControle.load():
            print("Erro ao carregar o arquivo")

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

        self.exit = Button(self.Home, text="Exit", fg="red", command=self.fim)
        self.exit.grid(row=1,column=4)

    def fim(self):
    
        #Add mensagem de erro
        if not self.cControle.save():
            print("Erro ao salvar o arquivo")
        if not self.sControle.save():
            print("Erro ao salvar o arquivo")
        if not self.aControle.save():
            print("Erro ao salvar o arquivo")
        if not self.tControle.save():
            print("Erro ao salvar o arquivo")

        exit()
    
    
    def muda_tela(self, event, future_frame):
        self.Home.grid_forget()
        future_frame.grid()

if __name__ == '__main__':
    root = Tk()

    m = HomeInterface(root)
    m.grid()

    m.mainloop()