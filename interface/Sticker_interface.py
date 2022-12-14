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
        self.Modify_Window = Frame(self.parent)
        self.Search_Window_ID = Frame(self.parent)
        self.Search_Window_Name = Frame(self.parent)
        self.Show_Sticker = Frame(self.parent)
        self.sticker_controler = StickerControle()
        self.widgets_make_invisible = []
        
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
        
        self.modify_window()
        self.Modify_Window.grid_forget()

        self.search()
        self.Search.grid_forget()
        
        self.search_by_id()
        self.Search_Window_ID.grid_forget()
        
        self.search_by_name()
        self.Search_Window_Name.grid_forget()
        
        self.show_sticker()
        self.Show_Sticker.grid_forget()
        
        
        
      
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
        
        self.modify_msg_error = Label(self.Modify, text='Please enter a valid Id for Sticker', fg='red')
        self.modify_msg_error.grid(row=1,columnspan=5, sticky=E+W, padx=5, pady=5)
        self.modify_msg_error.grid_forget()
        self.modify_msg_error.visibol = 0
        self.widgets_make_invisible.append(self.modify_msg_error)

        self.modify_msg_hit = Label(self.Modify, text='Sticker modified successfully')
        self.modify_msg_hit.grid(row=1,columnspan=5, sticky=E+W, padx=5, pady=5)
        self.modify_msg_hit.grid_forget()
        self.modify_msg_hit.visibol = 0
        self.widgets_make_invisible.append(self.modify_msg_hit)
        
        Label(self.Modify,text='Sticker ID:').grid(row=2, column=0, pady=5, padx=5)

        vcmd = (self.Modify.register(self.callback))
        self.modify_id_sticker = Entry(self.Modify, width=10, validate='all', validatecommand=(vcmd, '%P'))
        self.modify_id_sticker.grid(row=2, column=1, sticky=E+W, pady=5, padx=5)
        self.modify_id_sticker.focus_force()

        self.confirm_modify = Button(self.Modify, text="Modify", fg="red")
        self.confirm_modify.bind("<Button-1>", lambda event: self.modify_event(event, self.modify_id_sticker))
        self.confirm_modify.grid(row=4,column=0, sticky=W,pady=5,padx=5)

        self.exit_modify = Button(self.Modify, text="Exit", fg="red")
        self.exit_modify.bind("<Button-1>", lambda event, future_frame=self.Home: 
                                     self.muda_tela(event, self.Modify, future_frame))
        self.exit_modify.grid(row=4,column=1, sticky=E,pady=5,padx=5)
        
    def modify_window(self):
        
        self.Modify_Window.grid()
        
        Label(self.Modify_Window, text='Sticker Modify Traits').grid(row=0,columnspan=5)
        
        self.modifyS_msg_error = Label(self.Modify_Window, text='Sticker was not modified', fg='red')
        self.modifyS_msg_error.grid(row=1,columnspan=5, sticky=E+W, padx=5, pady=5)
        self.modifyS_msg_error.grid_forget()
        self.modifyS_msg_error.visibol = 0
        self.widgets_make_invisible.append(self.modifyS_msg_error)

        self.modifyS_msg_hit = Label(self.Modify_Window, text='Sticker modified successfully')
        self.modifyS_msg_hit.grid(row=1,columnspan=5, sticky=E+W, padx=5, pady=5)
        self.modifyS_msg_hit.grid_forget()
        self.modifyS_msg_hit.visibol = 0
        self.widgets_make_invisible.append(self.modifyS_msg_hit)
        
        Label(self.Modify_Window,text='Modify Name:').grid(row=2, column=0, pady=5, padx=5)

        self.modify_name_sticker = Entry(self.Modify_Window, width=10, validate='all')
        self.modify_name_sticker.grid(row=2, column=1, sticky=E+W, pady=5, padx=5)
        self.modify_name_sticker.focus_force()
        
        Label(self.Modify_Window,text='Modify Team:').grid(row=4, column=0, pady=5, padx=5)

        self.modify_team_sticker = Entry(self.Modify_Window, width=10, validate='all')
        self.modify_team_sticker.grid(row=4, column=1, sticky=E+W, pady=5, padx=5)
        self.modify_team_sticker.focus_force()
        
        Label(self.Modify_Window,text='Modify Position:').grid(row=6, column=0, pady=5, padx=5)

        self.modify_position_sticker = Entry(self.Modify_Window, width=10, validate='all')
        self.modify_position_sticker.grid(row=6, column=1, sticky=E+W, pady=5, padx=5)
        self.modify_position_sticker.focus_force()


        self.confirm_modify_window = Button(self.Modify_Window, text="Modify Sticker", fg="red")
        self.confirm_modify_window.bind("<Button-1>", lambda event: 
                        self.confirm_modify_envent(event, 
                                                   self.modify_name_sticker, 
                                                   self.modify_team_sticker, 
                                                   self.modify_position_sticker
                                                   ))
        self.confirm_modify_window.grid(row=8,column=0, sticky=W,pady=5,padx=5)

        self.exit_modify_window = Button(self.Modify_Window, text="Exit", fg="red")
        self.exit_modify_window.bind("<Button-1>", lambda event, future_frame=self.Modify: 
                                     self.muda_tela(event, self.Modify_Window, future_frame))
        self.exit_modify_window.grid(row=8,column=1, sticky=E,pady=5,padx=5)
        

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
                print(text.get())
                if self.remove_msg_error.visibol == 1:
                    self.remove_msg_error.grid_forget()
                    self.remove_msg_error.visibol = 0
                self.remove_msg_hit.grid(row=1,columnspan=5, sticky=E+W, padx=5, pady=5)
                self.remove_msg_hit.visibol = 1

                self.sticker_controler.remove(sticker_remove)

        text.delete(0, END)
        text.insert(0, "")
        
    def confirm_modify_envent(self, event, name, team, position):
        e = Sticker(name.get(), team.get(), position.get())
        e.id = self.current_modified_id
        confirm = self.sticker_controler.modify(e)
        
        if not confirm:
            if self.modifyS_msg_hit.visibol == 1:
                self.modifyS_msg_hit.grid_forget()
                self.modifyS_msg_hit.visibol = 0
            self.modifyS_msg_error.grid(row=1,columnspan=5, sticky=E+W, padx=5, pady=5)
            self.modifyS_msg_error.visibol = 1
        else:
            if self.modifyS_msg_error.visibol == 1:
                self.modifyS_msg_error.grid_forget()
                self.modifyS_msg_error.visibol = 0
            self.modifyS_msg_hit.grid(row=1,columnspan=5, sticky=E+W, padx=5, pady=5)
            self.modifyS_msg_hit.visibol = 1
        
    def modify_event(self, event, text):
        if text.get() == "":
            if self.modify_msg_hit.visibol == 1:
                self.modify_msg_hit.grid_forget()
                self.modify_msg_hit.visibol = 0
            self.modify_msg_error.grid(row=1,columnspan=5, sticky=E+W, padx=5, pady=5)
            self.modify_msg_error.visibol = 1
        else:
            
            sticker_modify = self.sticker_controler.search_by_id(int(text.get()))

            if sticker_modify == None:
                if self.modify_msg_hit.visibol == 1:
                    self.modify_msg_hit.grid_forget()
                    self.modify_msg_hit.visibol = 0
                self.modify_msg_error.grid(row=1,columnspan=5, sticky=E+W, padx=5, pady=5)
                self.modify_msg_error.visibol = 1
            else: 
                self.current_modified_id = int(text.get())
                self.muda_tela(None, self.Modify, self.Modify_Window)
                
                if self.modify_msg_error.visibol == 1:
                    self.modify_msg_error.grid_forget()
                    self.modify_msg_error.visibol = 0
                self.modify_msg_hit.grid(row=1,columnspan=5, sticky=E+W, padx=5, pady=5)
                self.modify_msg_hit.visibol = 1


        text.delete(0, END)
        text.insert(0, "")
        
        
    def search_event(self, event, text):
        if text.get() == "":
            if self.search_msg_hit.visibol == 1:
                self.search_msg_hit.grid_forget()
                self.search_msg_hit.visibol = 0
            self.search_msg_error.grid(row=1,columnspan=5, sticky=E+W, padx=5, pady=5)
            self.search_msg_error.visibol = 1
        else:
            collector_search = self.collector_controler.search_by_id(int(text.get()))

            if collector_search == None:
                if self.search_msg_hit.visibol == 1:
                    self.search_msg_hit.grid_forget()
                    self.search_msg_hit.visibol = 0
                self.search_msg_error.grid(row=1,columnspan=5, sticky=E+W, padx=5, pady=5)
                self.search_msg_error.visibol = 1
            else: 
                if self.search_msg_error.visibol == 1:
                    self.search_msg_error.grid_forget()
                    self.search_msg_error.visibol = 0
                self.search_msg_hit.grid(row=1,columnspan=5, sticky=E+W, padx=5, pady=5)
                self.search_msg_hit.visibol = 1

                #self.collector_controler.search(collector_search)

        text.delete(0, END)
        text.insert(0, "")

    def search_event_show(self, event, chosen_whidget):
        if chosen_whidget == self.search_str_button:
            self.search_chosen = 1 #1 = str
            
            self.search_msg_name.grid(row=2, column=0, pady=5, padx=5)
            self.search_msg_name.visibol = 1
            
            self.search_name_collector.grid(row=2, column=2, sticky=E+W, pady=5, padx=5)
            self.search_name_collector.visibol = 1

        else: 
            self.search_chosen = 2 #2 = id

            self.search_msg_id.grid(row=2, column=0, pady=5, padx=5)
            self.search_msg_id.visibol = 1
            
            self.search_id_collector.grid(row=2, column=2, sticky=E+W, pady=5, padx=5)
            self.search_id_collector.visibol = 1

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

        if (self.search_msg_id.visibol == 1) or (self.search_id_collector.visibol == 1):
            self.search_msg_id.grid_forget()
            self.search_msg_id.visibol = 0
            
            self.search_id_collector.grid_forget()
            self.search_id_collector.visibol = 0


        if (self.search_msg_name.visibol == 1) or (self.search_name_collector.visibol == 1):
            self.search_msg_name.grid_forget()
            self.search_msg_name.visibol = 0
            
            self.search_name_collector.grid_forget()
            self.search_name_collector.visibol = 0

        if (self.search_id_button.visibol == 0) or (self.search_str_button.visibol == 0):
            self.search_id_button.grid()

            self.search_id_button.grid(row=4,column=0, sticky=W,pady=5,padx=5)
            self.search_id_button.visibol = 1
            self.search_str_button.grid(row=4,column=1, sticky=W,pady=5,padx=5)
            self.search_str_button.visibol = 1