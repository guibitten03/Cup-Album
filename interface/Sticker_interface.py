from interface import *
from controle import *
from tkinter import *
from models import *

class StickerInterface(Frame, Interface):
    def __init__(self, parent, nome, home_interface):
        super().__init__(parent)

        self.parent = parent
        self.Home = Frame(self.parent)
        self.Insert = Frame(self.parent)
        self.Remove = Frame(self.parent)
        self.Modify = Frame(self.parent)
        self.Search = Frame(self.parent)
        self.Modify_aux = Frame(self.parent)
        self.sticker_controler = StickerControle()
        self.widgets_make_invisible = []
        self.widgets_make_visibol = []
        
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
        
        self.__modify_aux__()
        self.Modify_aux.grid_forget()
        
      
    def home(self):

        self.Home.grid()

        Label(self.Home, text='Voce esta no ' + self.nome).grid(row=0,columnspan=5)

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

        Label(self.Insert, text='Sticker insert').grid(row=0,columnspan=5)
        
        self.insert_msg_error = Label(self.Insert, text='Please enter a name, team and position for Sticker', fg='red')
        self.insert_msg_error.grid(row=1,columnspan=5, sticky=E+W, padx=5, pady=5)
        self.insert_msg_error.grid_forget()
        self.insert_msg_error.visibol = 0
        self.widgets_make_invisible.append(self.insert_msg_error)

        self.insert_msg_hit = Label(self.Insert, text='Sticker inserted successfully')
        self.insert_msg_hit.grid(row=1,columnspan=5, sticky=E+W, padx=5, pady=5)
        self.insert_msg_hit.grid_forget()
        self.insert_msg_hit.visibol = 0
        self.widgets_make_invisible.append(self.insert_msg_hit)
        
        Label(self.Insert,text='Sticker Name:').grid(row=2, column=0, pady=5, padx=5)

        self.insert_name_sticker = Entry(self.Insert, width=10)
        self.insert_name_sticker.grid(row=2, column=1, sticky=E+W, pady=5, padx=5)
        self.insert_name_sticker.focus_force()
        
        Label(self.Insert,text='Sticker Team:').grid(row=4, column=0, pady=5, padx=5)

        self.insert_team_sticker=Entry(self.Insert, width=10)
        self.insert_team_sticker.grid(row=4, column=1, sticky=E+W, pady=5, padx=5)
        self.insert_team_sticker.focus_force()
        
        Label(self.Insert,text='Sticker Position:').grid(row=6, column=0, pady=5, padx=5)

        self.insert_position_sticker=Entry(self.Insert, width=10)
        self.insert_position_sticker.grid(row=6, column=1, sticky=E+W, pady=5, padx=5)
        self.insert_position_sticker.focus_force()

        self.confirm_insert = Button(self.Insert, text="Insert", fg="red")
        self.confirm_insert.bind("<Button-1>", 
                                 lambda event: self.insert_event(event, self.insert_name_sticker, self.insert_team_sticker, self.insert_position_sticker))
        self.confirm_insert.grid(row=8,column=0, sticky=W,pady=5,padx=5)

        self.exit_insert = Button(self.Insert, text="Exit", fg="red")
        self.exit_insert.bind("<Button-1>", lambda event, future_frame=self.Home: 
                                            self.muda_tela(event, self.Insert, future_frame))
        self.exit_insert.grid(row=8,column=1, sticky=E,pady=5,padx=5)

    def remove(self):

        self.Remove.grid()

        Label(self.Remove, text='Sticker remove').grid(row=0,columnspan=5)
        
        self.remove_msg_error = Label(self.Remove, text='Please enter a valid Id for Sticker', fg='red')
        self.remove_msg_error.grid(row=1,columnspan=5, sticky=E+W, padx=5, pady=5)
        self.remove_msg_error.grid_forget()
        self.remove_msg_error.visibol = 0
        self.widgets_make_invisible.append(self.remove_msg_error)

        self.remove_msg_hit = Label(self.Remove, text='Sticker removed successfully')
        self.remove_msg_hit.grid(row=1,columnspan=5, sticky=E+W, padx=5, pady=5)
        self.remove_msg_hit.grid_forget()
        self.remove_msg_hit.visibol = 0
        self.widgets_make_invisible.append(self.remove_msg_hit)
        
        Label(self.Remove,text='Sticker ID:').grid(row=2, column=0, pady=5, padx=5)

        vcmd = (self.Remove.register(self.callback))
        self.remove_id_sticker = Entry(self.Remove, width=10, validate='all', validatecommand=(vcmd, '%P'))
        self.remove_id_sticker.grid(row=2, column=1, sticky=E+W, pady=5, padx=5)
        self.remove_id_sticker.focus_force()

        self.confirm_remove = Button(self.Remove, text="Remove", fg="red")
        self.confirm_remove.bind("<Button-1>", lambda event: self.remove_event(event, self.remove_id_sticker))
        self.confirm_remove.grid(row=4,column=0, sticky=W,pady=5,padx=5)

        self.exit_remove = Button(self.Remove, text="Exit", fg="red")
        self.exit_remove.bind("<Button-1>", lambda event, future_frame=self.Home: 
                                            self.muda_tela(event, self.Remove, future_frame))
        self.exit_remove.grid(row=4,column=1, sticky=E,pady=5,padx=5)
    
    def modify(self):

        self.Modify.grid()

        Label(self.Modify, text='Sticker modify').grid(row=0,columnspan=5)

        self.modify_msg_error = Label(self.Modify, text='Sticker not found', fg='red')
        self.modify_msg_error.grid(row=1,columnspan=5, sticky=E+W, padx=5, pady=5)
        self.modify_msg_error.grid_forget()
        self.modify_msg_error.visibol = 0
        self.widgets_make_invisible.append(self.modify_msg_error)

        self.modify_msg_hit = Label(self.Modify, text='Sticker successfully modified')
        self.modify_msg_hit.grid(row=1,columnspan=5, sticky=E+W, padx=5, pady=5)
        self.modify_msg_hit.grid_forget()
        self.modify_msg_hit.visibol = 0
        self.widgets_make_invisible.append(self.modify_msg_hit)

        Label(self.Modify,text='Sticker ID:').grid(row=2, column=0, pady=5, padx=5)

        vcmd = (self.Modify.register(self.callback))
        self.modify_id_sticker=Entry(self.Modify, width=10, validate='all', validatecommand=(vcmd, '%P'))
        self.modify_id_sticker.grid(row=2, column=1, sticky=E+W, pady=5, padx=5)
        self.modify_id_sticker.focus_force()

        self.confirm_modify = Button(self.Modify, text="Modify", fg="red")
        self.confirm_modify.bind("<Button-1>", lambda event: self.modify_event(event, self.modify_id_sticker))
        self.confirm_modify.grid(row=4,column=0, sticky=W,pady=5,padx=5)

        self.exit_modify = Button(self.Modify, text="Exit", fg="red")
        self.exit_modify.bind("<Button-1>", lambda event, future_frame=self.Home: 
                                     self.muda_tela(event, self.Modify, future_frame))
        self.exit_modify.grid(row=4,column=1, sticky=E,pady=5,padx=5)
    
    def search(self):

        self.Search.grid()

        Label(self.Search, text='Sticker search').grid(row=0,columnspan=5)

        self.search_msg_error = Label(self.Search, text='Sticker not found', fg='red')
        self.search_msg_error.grid(row=1,columnspan=5, sticky=E+W, padx=5, pady=5)
        self.search_msg_error.grid_forget()
        self.search_msg_error.visibol = 0
        self.widgets_make_invisible.append(self.search_msg_error)


        self.search_msg_id = Label(self.Search,text='Search ID:')
        self.search_msg_id.grid(row=2, column=0, pady=5, padx=5)
        self.search_msg_id.grid_forget()
        self.search_msg_id.visibol = 0

        vcmd = (self.Search.register(self.callback))
        self.search_id_sticker=Entry(self.Search, width=10, validate='all', validatecommand=(vcmd, '%P'))
        self.search_id_sticker.grid(row=2, column=2, sticky=E+W, pady=5, padx=5)
        self.search_id_sticker.focus_force()
        self.search_id_sticker.grid_forget()
        self.search_id_sticker.visibol = 0

        self.search_msg_name = Label(self.Search,text='Search Name:')
        self.search_msg_name.grid(row=2, column=0, pady=5, padx=5)
        self.search_msg_name.grid_forget()
        self.search_msg_name.visibol = 0

        vcmd = (self.Search.register(self.callback))
        self.search_name_sticker=Entry(self.Search, width=10)
        self.search_name_sticker.grid(row=2, column=2, sticky=E+W, pady=5, padx=5)
        self.search_name_sticker.focus_force()
        self.search_name_sticker.grid_forget()
        self.search_name_sticker.visibol = 0

        self.confirm_search = Button(self.Search, text="search", fg="red")
        self.confirm_search.bind("<Button-1>", lambda event: self.search_event(event, self.search_chosen))
        self.confirm_search.grid(row=4,column=0, sticky=W,pady=5,padx=5)
        self.confirm_search.grid_forget()
        self.confirm_search.visibol = 0

        self.search_id_button = Button(self.Search, text="search by id", fg="red")
        self.search_id_button.bind("<Button-1>", lambda event: self.search_event_show(event, self.search_id_button))
        self.search_id_button.grid(row=4,column=0, sticky=W,pady=5,padx=5)
        self.search_id_button.visibol = 1

        self.search_str_button = Button(self.Search, text="search by str", fg="red")
        self.search_str_button.bind("<Button-1>", lambda event: self.search_event_show(event, self.search_str_button))
        self.search_str_button.grid(row=4,column=1, sticky=W,pady=5,padx=5)
        self.search_str_button.visibol = 1

        self.exit_search = Button(self.Search, text="Exit", fg="red")
        self.exit_search.bind("<Button-1>", self.search_event_to_normal)
        self.exit_search.bind("<Button-1>", lambda event, future_frame=self.Home: 
                                     self.muda_tela(event, self.Search, future_frame), add='+')
        self.exit_search.grid(row=4,column=2, sticky=E,pady=5,padx=5)


    def callback(self, P):
        if str.isdigit(P) or P == "":
            return True
        else:
            return False

    def muda_tela(self, event, current_frame, future_frame):
        current_frame.grid_forget()
        future_frame.grid()
        
        for w in self.widgets_make_invisible:
            if w.visibol == 1:
                w.grid_forget()
                w.visibol == 0
                

    def insert_event(self, event, name, team, position):
        if (name.get()!= "") & (team.get() != "") & (position.get() != ""):
            self.sticker_controler.insert(Sticker(name.get(), team.get(), position.get()))
            if self.insert_msg_error.visibol == 1:
                self.insert_msg_error.grid_forget()
                self.insert_msg_error.visibol = 0
            self.insert_msg_hit.grid(row=1,columnspan=5, sticky=E+W, padx=5, pady=5)
            self.insert_msg_hit.visibol = 1
        else:
            if self.insert_msg_hit.visibol == 1:
                self.insert_msg_hit.grid_forget()
                self.insert_msg_hit.visibol = 0
            self.insert_msg_error.grid(row=1,columnspan=5, sticky=E+W, padx=5, pady=5)
            self.insert_msg_error.visibol = 1
        name.delete(0, END)
        name.insert(0, "")
        
        team.delete(0, END)
        team.insert(0, "")
        
        position.delete(0, END)
        position.insert(0, "")
    
    def remove_event(self, event, text):
        if text.get() == "":
            if self.remove_msg_hit.visibol == 1:
                self.remove_msg_hit.grid_forget()
                self.remove_msg_hit.visibol = 0
            self.remove_msg_error.grid(row=1,columnspan=5, sticky=E+W, padx=5, pady=5)
            self.remove_msg_error.visibol = 1
        else:
            
            sticker_remove = self.sticker_controler.search_by_id(int(text.get()))

            if sticker_remove == None:
                if self.remove_msg_hit.visibol == 1:
                    self.remove_msg_hit.grid_forget()
                    self.remove_msg_hit.visibol = 0
                self.remove_msg_error.grid(row=1,columnspan=5, sticky=E+W, padx=5, pady=5)
                self.remove_msg_error.visibol = 1
            else: 
                if self.remove_msg_error.visibol == 1:
                    self.remove_msg_error.grid_forget()
                    self.remove_msg_error.visibol = 0
                self.remove_msg_hit.grid(row=1,columnspan=5, sticky=E+W, padx=5, pady=5)
                self.remove_msg_hit.visibol = 1

                self.sticker_controler.remove(sticker_remove)

        text.delete(0, END)
        text.insert(0, "")
        
    def modify_event(self, event, text):
        if text.get() == "":
            if self.modify_msg_hit.visibol == 1:
                self.modify_msg_hit.grid_forget()
                self.modify_msg_hit.visibol = 0
            self.modify_msg_error.grid(row=1,columnspan=5, sticky=E+W, padx=5, pady=5)
            self.modify_msg_error.visibol = 1

            text.delete(0, END)
            text.insert(0, "")
        else:

            if self.sticker_controler.search_by_id(int(text.get())) == None:
                if self.modify_msg_hit.visibol == 1:
                    self.modify_msg_hit.grid_forget()
                    self.modify_msg_hit.visibol = 0
                self.modify_msg_error.grid(row=1,columnspan=5, sticky=E+W, padx=5, pady=5)
                self.modify_msg_error.visibol = 1

                text.delete(0, END)
                text.insert(0, "")
            else: 
                self.Modify.grid_forget()
                self.Modify_aux.grid()

    def __modify_aux__(self):

        self.Modify_aux.grid()

        Label(self.Modify_aux,text='New name:').grid(row=0, column=0, pady=5, padx=5)

        self.modify_aux_name_sticker=Entry(self.Modify_aux, width=10)
        self.modify_aux_name_sticker.grid(row=0, column=1, sticky=E+W, pady=5, padx=5)
        self.modify_aux_name_sticker.focus_force()
        
        Label(self.Modify_aux,text='New team:').grid(row=2, column=0, pady=5, padx=5)

        self.modify_aux_team_sticker=Entry(self.Modify_aux, width=10)
        self.modify_aux_team_sticker.grid(row=2, column=1, sticky=E+W, pady=5, padx=5)
        self.modify_aux_team_sticker.focus_force()
        
        Label(self.Modify_aux,text='New position:').grid(row=4, column=0, pady=5, padx=5)

        self.modify_aux_position_sticker=Entry(self.Modify_aux, width=10)
        self.modify_aux_position_sticker.grid(row=4, column=1, sticky=E+W, pady=5, padx=5)
        self.modify_aux_position_sticker.focus_force()

        self.confirm_modify_aux = Button(self.Modify_aux, text="Modify", fg="red")
        self.confirm_modify_aux.bind("<Button-1>", lambda event:
            self.__modify_event_aux__(event, self.modify_aux_name_sticker, self.modify_aux_team_sticker, self.modify_aux_position_sticker))
        self.confirm_modify_aux.grid(row=6,column=1, sticky=W,pady=5,padx=5)
        

    def __modify_event_aux__(self, event, name, team, position):

        modify_sticker = self.sticker_controler.search_by_id(int(self.modify_id_sticker.get()))
        modify_sticker.set_name(name.get())
        modify_sticker.set_time(team.get())
        modify_sticker.set_position(position.get())

        name.delete(0, END)
        name.insert(0, "")
        
        team.delete(0, END)
        team.insert(0, "")
        
        position.delete(0, END)
        position.insert(0, "")
        
        self.modify_id_sticker.delete(0, END)
        self.modify_id_sticker.insert(0, "")

        self.Modify_aux.grid_forget()
        self.Modify.grid()

        if self.modify_msg_error.visibol == 1:
                self.modify_msg_error.grid_forget()
                self.modify_msg_error.visibol = 0
        self.modify_msg_hit.grid(row=1,columnspan=5, sticky=E+W, padx=5, pady=5)
        self.modify_msg_hit.visibol = 1
    
    def search_event(self, event, text):

        if text == 1 :
            if self.search_name_sticker.get() == "":
                self.search_msg_error.grid(row=1,columnspan=5, sticky=E+W, padx=5, pady=5)
                self.search_msg_error.visibol = 1
            else:
                sticker_search_name_ = self.sticker_controler.search_by_str(self.search_name_sticker.get())

                if sticker_search_name_ == None:
                    self.search_msg_error.grid(row=1,columnspan=5, sticky=E+W, padx=5, pady=5)
                    self.search_msg_error.visibol = 1
                else:
                    self.search_msg_error.grid_forget()
                    self.search_msg_error.visibol = 0

                    self.Search_aux = Frame(self.parent)
                    
                    self.Search.grid_forget()

                    self.search_aux(sticker_search_name_)
                    self.Search_aux.grid()
        elif text == 2:
            if self.search_id_sticker.get() == "":
                self.search_msg_error.grid(row=1,columnspan=5, sticky=E+W, padx=5, pady=5)
                self.search_msg_error.visibol = 1
            else:
                sticker_search_id_ = self.sticker_controler.search_by_id(int(self.search_id_sticker.get()))

                if sticker_search_id_ == None:
                    self.search_msg_error.grid(row=1,columnspan=5, sticky=E+W, padx=5, pady=5)
                    self.search_msg_error.visibol = 1
                else:
                    self.search_msg_error.grid_forget()
                    self.search_msg_error.visibol = 0

                    self.Search_aux = Frame(self.parent)

                    self.Search.grid_forget()

                    self.search_aux(sticker_search_id_)
                    self.Search_aux.grid()
        
        self.search_name_sticker.delete(0, END)
        self.search_name_sticker.insert(0, "")
        self.search_id_sticker.delete(0, END)
        self.search_id_sticker.insert(0, "")

    def search_aux(self, *stickers):
        self.Search_aux.grid()

        Label(self.Search_aux, text='Sticker search').grid(row=0,columnspan=5)

        for num, cli in enumerate(stickers):
            Label(self.Search_aux, text=cli).grid(row=num+1,columnspan=5, sticky=E,pady=5,padx=5)
        
        self.exit_search_aux = Button(self.Search_aux, text="Exit", fg="red")
        self.exit_search_aux.bind("<Button-1>",self.search_aux_exit)
        self.exit_search_aux.grid(row=len(stickers)+2,column=2, sticky=E,pady=5,padx=5)

    def search_aux_exit(self, event) -> None:
        self.Search_aux.destroy()

        self.Search.grid()

    def search_event_show(self, event, chosen_whidget):
        if chosen_whidget == self.search_str_button:
            self.search_chosen = 1 #1 = str
            
            self.search_msg_name.grid(row=2, column=0, pady=5, padx=5)
            self.search_msg_name.visibol = 1
            
            self.search_name_sticker.grid(row=2, column=2, sticky=E+W, pady=5, padx=5)
            self.search_name_sticker.visibol = 1

        else: 
            self.search_chosen = 2 #2 = id

            self.search_msg_id.grid(row=2, column=0, pady=5, padx=5)
            self.search_msg_id.visibol = 1
            
            self.search_id_sticker.grid(row=2, column=2, sticky=E+W, pady=5, padx=5)
            self.search_id_sticker.visibol = 1

        self.search_id_button.grid_forget()
        self.search_id_button.visibol = 0
        self.search_str_button.grid_forget()
        self.search_str_button.visibol = 0
        self.confirm_search.grid(row=4,column=0, sticky=W,pady=5,padx=5)
        self.confirm_search.visibol = 1
    
    def search_event_to_normal(self, event):
        
        if self.confirm_search.visibol == 1:
            self.confirm_search.grid_forget()
            self.confirm_search.visibol = 0

        if (self.search_msg_id.visibol == 1) or (self.search_id_sticker.visibol == 1):
            self.search_msg_id.grid_forget()
            self.search_msg_id.visibol = 0
            
            self.search_id_sticker.grid_forget()
            self.search_id_sticker.visibol = 0

        if (self.search_msg_name.visibol == 1) or (self.search_name_sticker.visibol == 1):
            self.search_msg_name.grid_forget()
            self.search_msg_name.visibol = 0
            
            self.search_name_sticker.grid_forget()
            self.search_name_sticker.visibol = 0

        if (self.search_id_button.visibol == 0) or (self.search_str_button.visibol == 0):
            self.search_id_button.grid()

            self.search_id_button.grid(row=4,column=0, sticky=W,pady=5,padx=5)
            self.search_id_button.visibol = 1
            self.search_str_button.grid(row=4,column=1, sticky=W,pady=5,padx=5)
            self.search_str_button.visibol = 1
