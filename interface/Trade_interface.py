from Class_interface import Interface
from controle import *
from tkinter import *

class TradeInterface(Frame, Interface):
    def __init__(self, parent, nome, home_interface):
        super().__init__(parent)

        self.parent = parent
        self.Home = Frame(self.parent)
        self.Insert = Frame(self.parent)
        self.Remove = Frame(self.parent)
        self.Modify = Frame(self.parent)
        self.Search = Frame(self.parent)
        self.trade_controler = TradeControle()
        
        self.home_interface = home_interface
        self.nome = nome

        self.home()
        self.Home.grid_forget()

        self.insert()
        self.Insert.grid_forget()

        self.remove()
        self.Remove.grid_forget()

        self.modify()
        self.Modify.grid_forget()

        self.search()
        self.Search.grid_forget()
      
    def home(self):

        self.Home.grid()

        Label(self.Home, text='Voce esta na ' + self.nome).grid(row=0,columnspan=5)

        self.to_insert = Button(self.Home, text="Insert", fg="red")
        self.to_insert.bind("<Button-1>", lambda event, future_frame=self.Insert: 
                                          self.muda_tela(event, self.Home, future_frame))
        self.to_insert.grid(row=1, column=0)

        self.to_remove = Button(self.Home, text="Remove", fg="red")
        self.to_remove.bind("<Button-1>", lambda event, future_frame=self.Remove: 
                                          self.muda_tela(event, self.Home, future_frame))
        self.to_remove.grid(row=1, column=1)

        self.to_modify = Button(self.Home, text="Modify", fg="red")
        self.to_modify.bind("<Button-1>", lambda event, future_frame=self.Modify: 
                                     self.muda_tela(event, self.Home, future_frame))
        self.to_modify.grid(row=1, column=2)

        self.to_search = Button(self.Home, text="Search", fg="red")
        self.to_search.bind("<Button-1>", lambda event, future_frame=self.Search: 
                                     self.muda_tela(event, self.Home, future_frame))
        self.to_search.grid(row=1, column=3)

        self.exit_home = Button(self.Home, text="Exit", fg="red")
        self.exit_home.bind("<Button-1>", lambda event, future_frame=self.home_interface.Home: 
                                     self.muda_tela(event, self.Home, future_frame))
        self.exit_home.grid(row=1, column=4)

    def insert(self):

        self.Insert.grid()

        vcmd = (self.Insert.register(self.callback))
        Label(self.Insert, text='Trade insert').grid(row=0,columnspan=5)
        Label(self.Insert,text='Collector 1 ID:').grid(row=2, column=0, pady=5, padx=5)
        Label(self.Insert,text='Collector 2 ID:').grid(row=4, column=0, pady=5, padx=5)
        Label(self.Insert,text='Sticker 1 ID:').grid(row=6, column=0, pady=5, padx=5)
        Label(self.Insert,text='Sticker 2 ID:').grid(row=8, column=0, pady=5, padx=5)

        self.insert_collector_1_ID=Entry(self.Insert, width=10, validate='all', validatecommand=(vcmd, '%P'))
        self.insert_collector_1_ID.grid(row=2, column=1, sticky=E+W, pady=5, padx=5)
        self.insert_collector_1_ID.focus_force()

        self.insert_collector_2_ID=Entry(self.Insert, width=10, validate='all', validatecommand=(vcmd, '%P'))
        self.insert_collector_2_ID.grid(row=4, column=1, sticky=E+W, pady=5, padx=5)
        self.insert_collector_2_ID.focus_force()

        self.insert_sticker_1_ID=Entry(self.Insert, width=10, validate='all', validatecommand=(vcmd, '%P'))
        self.insert_sticker_1_ID.grid(row=6, column=1, sticky=E+W, pady=5, padx=5)
        self.insert_sticker_1_ID.focus_force()

        self.insert_sticker_2_ID=Entry(self.Insert, width=10, validate='all', validatecommand=(vcmd, '%P'))
        self.insert_sticker_2_ID.grid(row=8, column=1, sticky=E+W, pady=5, padx=5)
        self.insert_sticker_2_ID.focus_force()

        args = [self.insert_collector_1_ID, self.insert_collector_2_ID, self.insert_sticker_1_ID, self.insert_sticker_2_ID]

        self.confirm_insert = Button(self.Insert, text="Trade", fg="red")
        self.confirm_insert.bind("<Button-1>", lambda event: self.insert_event(event, args))
        self.confirm_insert.grid(row=10,column=0, sticky=W,pady=5,padx=5)

        self.exit_insert = Button(self.Insert, text="Exit", fg="red")
        self.exit_insert.bind("<Button-1>", lambda event, future_frame=self.Home: 
                                            self.muda_tela(event, self.Insert, future_frame))
        self.exit_insert.grid(row=10,column=1, sticky=E,pady=5,padx=5)

    def remove(self):

        self.Remove.grid()

        Label(self.Remove, text='trade remove').grid(row=0,columnspan=5)
        Label(self.Remove,text='trade ID:').grid(row=1, column=0, pady=5, padx=5)

        vcmd = (self.Remove.register(self.callback))
        self.remove_id_trade=Entry(self.Remove, width=10, validate='all', validatecommand=(vcmd, '%P'))
        self.remove_id_trade.grid(row=1, column=1, sticky=E+W, pady=5, padx=5)
        self.remove_id_trade.focus_force()

        self.confirm_remove = Button(self.Remove, text="Remove", fg="red")
        self.confirm_remove.bind("<Button-1>", lambda event: self.remove_event(event, self.remove_id_trade))
        self.confirm_remove.grid(row=2,column=0, sticky=W,pady=5,padx=5)

        self.exit_remove = Button(self.Remove, text="Exit", fg="red")
        self.exit_remove.bind("<Button-1>", lambda event, future_frame=self.Home: 
                                            self.muda_tela(event, self.Remove, future_frame))
        self.exit_remove.grid(row=2,column=1, sticky=E,pady=5,padx=5)
    
    def modify(self):

        self.Modify.grid()

        Label(self.Modify, text='trade modify').grid(row=0,columnspan=5)
        Label(self.Modify,text='trade ID:').grid(row=1, column=0, pady=5, padx=5)

        vcmd = (self.Modify.register(self.callback))
        self.modify_id_trade=Entry(self.Modify, width=10, validate='all', validatecommand=(vcmd, '%P'))
        self.modify_id_trade.grid(row=1, column=1, sticky=E+W, pady=5, padx=5)
        self.modify_id_trade.focus_force()

        self.confirm_remove = Button(self.Modify, text="Modify", fg="red")
        self.confirm_remove.bind("<Button-1>", lambda event: self.modify_event(event, self.modify_id_trade))
        self.confirm_remove.grid(row=2,column=0, sticky=W,pady=5,padx=5)

        self.exit_modify = Button(self.Modify, text="Exit", fg="red")
        self.exit_modify.bind("<Button-1>", lambda event, future_frame=self.Home: 
                                     self.muda_tela(event, self.Modify, future_frame))
        self.exit_modify.grid(row=2,column=1, sticky=E,pady=5,padx=5)
    
    def search(self):

        self.Search.grid()

        Label(self.Search, text='trade search').grid(row=0,columnspan=5)
        Label(self.Search,text='trade ID:').grid(row=1, column=0, pady=5, padx=5)

        vcmd = (self.Search.register(self.callback))
        self.search_id_trade=Entry(self.Search, width=10, validate='all', validatecommand=(vcmd, '%P'))
        self.search_id_trade.grid(row=1, column=1, sticky=E+W, pady=5, padx=5)
        self.search_id_trade.focus_force()

        self.confirm_remove = Button(self.Search, text="search", fg="red")
        self.confirm_remove.bind("<Button-1>", lambda event: self.search_event(event, self.search_id_trade))
        self.confirm_remove.grid(row=2,column=0, sticky=W,pady=5,padx=5)

        self.exit_search = Button(self.Search, text="Exit", fg="red")
        self.exit_search.bind("<Button-1>", lambda event, future_frame=self.Home: 
                                     self.muda_tela(event, self.Search, future_frame))
        self.exit_search.grid(row=2,column=1, sticky=E,pady=5,padx=5)

    def callback(self, P):
        if str.isdigit(P) or P == "":
            return True
        else:
            return False

    def muda_tela(self, event, current_frame, future_frame):
        current_frame.grid_forget()
        future_frame.grid()

    def insert_event(self, event, args):
        for text in args:
            print(text.get())
            text.delete(0, END)
            text.insert(0, "")
    
    def remove_event(self, event, text):
        print(text.get())
        text.delete(0, END)
        text.insert(0, "")

    def modify_event(self, event, text):
        print(text.get())
        text.delete(0, END)
        text.insert(0, "")

    def search_event(self, event, text):
        print(text.get())
        text.delete(0, END)
        text.insert(0, "")