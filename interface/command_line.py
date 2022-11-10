import os
from copy import deepcopy

from simple_term_menu import TerminalMenu
import pyfiglet

from persistence import *
from models import *


class CLI():
    @staticmethod
    def __clear() -> None:
        os.system("cls" if os.name == "nt" else "clear") or None

    @staticmethod
    def __message(mensagens: str, font: str = "slant") -> None:
        result = pyfiglet.figlet_format(mensagens, font)
        print(result)

    @staticmethod
    def __choice(options: list[str], cursor_style: tuple[str] = ("fg_red", "bold"), highlight_style: str = "standout", title: str = "" ) -> int:
        mainMenu = TerminalMenu(options, menu_cursor_style = cursor_style, menu_highlight_style = (highlight_style,), title= title)
        user_choice = mainMenu.show()
        return user_choice

    @staticmethod
    def __click_to_exit() -> None:
        option = ["Exit"]
        CLI.__choice(option)

    @staticmethod
    def __get_input(text: str, int_type: bool = False) -> str: 
        LOOP = True

        if int_type == False:
            return input(text)
        
        while LOOP:
            x: str = input(text)
            if x.isdigit():
                LOOP = False
            else:
                print("incorrect data type, please try again")
        
        return x
        
    @staticmethod
    def home(sp: StickerPersistence, ap: AlbumPersistence, cp: CollectorPersistence, tp: TradePersistence) -> None:
        options = [
            "[1] Stickers",
            "[2] Collector",
            "[3] Album",
            "[4] Trade",
            "[5] exit"
        ]

        LOOP = True

        while(LOOP):
            CLI.__clear() 
            CLI.__message("Fifa WC Album")

            user_choice = CLI.__choice(options, title = "choose one option")

            if user_choice == 0:
                CLI.Stickers(sp)

            elif user_choice == 1:
                CLI.Collector(cp)

            elif user_choice == 2:
                CLI.Album(ap, sp, cp)

            elif user_choice == 3:
                CLI.Trade(tp, cp, sp)

            elif user_choice == 4:
                # Salva modificações.
                LOOP = False

    @staticmethod
    def Stickers(sp: StickerPersistence) -> None:
        options = [
            "[1] Insert", 
            "[2] Remove", 
            "[3] Modify", 
            "[4] Search", 
            "[5] Exit"
        ]

        modify_list = [ "[1] Team", "[2] Position", "[3] Name", "[4] Exit" ]

        sticker_list_position = Sticker.positions
        sticker_list_teams = deepcopy(Sticker.teams)
        sticker_list_teams.append("Other")

        LOOP = True

        while LOOP:
            CLI.__clear()
            CLI.__message("stickers")

            user_choise = CLI.__choice(options)

            if user_choise == 0: 
                CLI.__clear()
                CLI.__message("Insert stickers")

                insert_teams = sticker_list_teams[CLI.__choice(sticker_list_teams, title = "Team name:")]
                if insert_teams == "Other":
                    insert_teams = CLI.__get_input("Team name: ")

                insert_position = sticker_list_position[CLI.__choice(sticker_list_position, title = "Position:")]

                insert_name = CLI.__get_input("Player name: ")

                CLI.__clear()
                CLI.__message("Insert stickers")
                print(f"    Team: {insert_teams}\n    Position: {insert_position}\n    Name: {insert_name}")
                
                if CLI.__choice(["[1] Insert", "[2] Cancel"]) == 0:
                    sp.insert(Sticker(team = insert_teams, position= insert_position, name= insert_name))
                    print("\n    sticker successfully inserted")
                    CLI.__click_to_exit()
                
            elif user_choise == 1:
                CLI.__clear()
                CLI.__message("Remove stickers")

                remove_id = (int)(CLI.__get_input("sticker id: ", int_type = True))
                
                CLI.__clear()
                CLI.__message("Remove stickers")

                if sp.search_by_id(remove_id) == None:
                    print(f"There is no sticker with id {remove_id}")
                    CLI.__click_to_exit()

                else:
                    print(f"    Remove ID {remove_id} sticker")
                    if CLI.__choice([ "[1] Remove", "[2] Cancel" ]) == 0:
                        sp.remove(remove_id)
                        print("    successful sticker remove")
                        CLI.__click_to_exit()
                    else:
                        print("    sticker not removed")
                        CLI.__click_to_exit()

            elif user_choise == 2: 
                CLI.__clear()
                CLI.__message("Modify stickers")

                modify_id = (int)(CLI.__get_input("sticker id: ", int_type = True))

                if sp.search_by_id(modify_id) == None:
                    print(f"There is no sticker with id {modify_id}.")
                    CLI.__click_to_exit()

                else:
                    modify_loop = True

                    while modify_loop:
                        CLI.__clear()
                        CLI.__message("Modify stickers")

                        print(f"Modify ID {modify_id} sticker")

                        modify_choise = CLI.__choice(modify_list)

                        if modify_choise == 0:
                            modify_team = sticker_list_teams[CLI.__choice(sticker_list_teams, title = "\nNew team:")]

                            if modify_team == "Other":
                                modify_team = CLI.__get_input("Team name: ")
                                
                            CLI.__clear()
                            CLI.__message("Modify stickers")
                            print(f"Modify ID {modify_id} sticker\n\n    New team: {modify_team}")

                            if CLI.__choice(["Modify team", "Cancel"]) == 0:
                                sp.modify(modify_id, team = modify_team) ##função de modify
                                print("    Team successful modify")
                                CLI.__click_to_exit()
                            else:
                                print("    Team not modify")
                                CLI.__click_to_exit()

                        elif modify_choise == 1:
                            modify_position = CLI.__choice(sticker_list_position, title = "\nNew position: ")

                            CLI.__clear()
                            CLI.__message("Modify stickers")
                            print(f"Modify ID {modify_id} sticker\n\n    New position: {modify_position}")

                            if CLI.__choice(["Modify position", "Cancel"]) == 0:
                                sp.modify(modify_id, position = modify_position) ##função de modify
                                print("    position successful modify")
                                CLI.__click_to_exit()
                            else:
                                print("    position not modify")
                                CLI.__click_to_exit()

                        elif modify_choise == 2:
                            modify_name = CLI.__get_input("\nNew name: ")

                            CLI.__clear()
                            CLI.__message("Modify stickers")
                            print(f"Modify ID {modify_id} sticker\n\n    New name: {modify_name}")

                            if CLI.__choice(["Modify name", "Cancel"]) == 0:
                                sp.modify(modify_id, name = modify_name) ##função de modify
                                print("    name successful modify")
                                CLI.__click_to_exit()
                            else:
                                print("    name not modify")
                                CLI.__click_to_exit()

                        elif modify_choise == 3:
                            modify_loop = False

            elif user_choise == 3:
                    CLI.__clear()
                    CLI.__message("Search stikers")

                    search_choise = CLI.__choice(["[1] By id","[2] By name", "[3] show all stikers"])
                    
                    if search_choise == 0:

                        search_id = (int)(CLI.__get_input("stiker id: ", int_type=True))

                        stiker_search = sp.search_by_id(search_id)

                        if stiker_search == None:
                            print(f"\n    There is no stiker with id {search_id}")
                            CLI.__click_to_exit()

                        else:
                            CLI.__clear()
                            CLI.__message("Search stikers")
                            print(stiker_search)
                            CLI.__click_to_exit()

                    elif search_choise == 1:

                        search_name = CLI.__get_input("stiker name: ")
                        
                        stiker_search = sp.search_by_str(search_name)

                        if stiker_search == None:
                            print(f"\n    There is no stiker with name {search_name}")
                            CLI.__click_to_exit()

                        else:
                            CLI.__clear()
                            CLI.__message("Search stikers")
                            print(stiker_search)
                            CLI.__click_to_exit()

                    elif search_choise == 2:
                        CLI.__clear()
                        CLI.__message("Search stikers")
                        sp.view_data()
                        CLI.__click_to_exit()

            elif user_choise == 4:
                #salvar alteracoes
                LOOP = False

    @staticmethod
    def Collector(cp: CollectorPersistence) -> None:

        options = ["[1] Insert", 
                   "[2] Remove", 
                   "[3] Modify", 
                   "[4] Search", 
                   "[5] Exit"]
        
        LOOP = True
        
        while LOOP:
            CLI.__clear()  
            CLI.__message("Collector") 

            user_choise = CLI.__choice(options)    
            
            if user_choise == 0:
                CLI.__clear()  
                CLI.__message("Insert collector") 

                insert_name = CLI.__get_input("Collector Name: ")

                CLI.__clear()
                CLI.__message("Insert collector")
                print(f"    Collector Name: {insert_name}\n")

                if CLI.__choice(["[1] Insert", "[2] Cancel"]) == 0:

                    cp.insert(Collector(insert_name))

                    print("    Collector successfully inserted")
                    CLI.__click_to_exit()

                else:
                    print("    Collector not inserted")
                    CLI.__click_to_exit()

            elif user_choise == 1:
                CLI.__clear()
                CLI.__message("Remove collector")

                remove_id = (int)(CLI.__get_input("Collector id: ", int_type = True))
                
                CLI.__clear()
                CLI.__message("Remove collector")

                if cp.search_by_id(remove_id) == None:
                    print(f"There is no collector with id {remove_id}")
                    CLI.__click_to_exit()

                else:
                    print(f"    Remove ID {remove_id} collector")
                    if CLI.__choice(["[1] Remove", "[2] Cancel"]) == 0:
                        cp.remove(remove_id)
                        print("\n    successful collector remove")
                        CLI.__click_to_exit()
                        
                    else:
                        print("\n    collector not removed")
                        CLI.__click_to_exit()

            elif user_choise == 2:
                CLI.__clear()
                CLI.__message("Modify Collectors")

                modify_id = (int)(CLI.__get_input("Collector id: ", int_type = True))

                CLI.__clear()
                CLI.__message("Modify Collectors")

                if cp.search_by_id(modify_id) == None:
                    print(f"There is no Collector with id {modify_id}")
                    CLI.__click_to_exit()
                
                else:
                    
                    print(f"Modify ID {modify_id} collectors\n")

                    modify_name = CLI.__get_input("New name: ")

                    if CLI.__choice(["Modify name", "Cancel"]) == 0:
                        cp.modify(modify_id, name = modify_name) 
                        print("\n    Name successful modify")
                        CLI.__click_to_exit()

                    else:
                        print("    Name not modify")
                        CLI.__click_to_exit()

            elif user_choise == 3:
                CLI.__clear()
                CLI.__message("Search Collectors")

                search_choise = CLI.__choice(["[1] By id","[2] By name", "[3] show all collectors"])
                
                if search_choise == 0:

                    search_id = (int)(CLI.__get_input("Collector id: ", int_type=True))

                    collector_search = cp.search_by_id(search_id)

                    if collector_search == None:
                        print(f"\n    There is no Collector with id {search_id}")
                        CLI.__click_to_exit()

                    else:
                        CLI.__clear()
                        CLI.__message("Search Collectors")
                        print(collector_search)
                        CLI.__click_to_exit()

                elif search_choise == 1:

                    search_name = CLI.__get_input("Collector name: ")
                    
                    collector_search = cp.search_by_str(search_name)

                    if collector_search == None:
                        print(f"\n    There is no Collector with name {search_name}")
                        CLI.__click_to_exit()

                    else:
                        CLI.__clear()
                        CLI.__message("Search Collectors")
                        print(collector_search)
                        CLI.__click_to_exit()

                elif search_choise == 2:
                    CLI.__clear()
                    CLI.__message("Search Collectors")
                    cp.view_data()
                    CLI.__click_to_exit()

            elif user_choise == 4:
                LOOP = False

    @staticmethod
    def Album(ap: AlbumPersistence, sp: StickerPersistence, cp: CollectorPersistence) -> None:
        options = ["[1] Paste sticker", 
                   "[2] Remove sticker", 
                   "[3] Insert", 
                   "[4] Remove", 
                   "[5] Modify", 
                   "[6] Search", 
                   "[7] Exit"]
        LOOP = True

        while LOOP:
            CLI.__clear()
            CLI.__message("sticker album")

            user_choise = CLI.__choice(options)

            if user_choise == 0:
                CLI.__clear()
                CLI.__message("Paste sticker")

                paste_id = (int)(CLI.__get_input("Album id: ", int_type = True))

                paste_album = ap.search_by_id(paste_id)

                if paste_album == None:
                    print(f"    There is no album with id {paste_id}")
                    CLI.__click_to_exit()
                
                else:
                    paste_sticker_id = (int)(CLI.__get_input("Sticker id: ", int_type = True))

                    paste_sticker = sp.search_by_id(paste_sticker_id)

                    if paste_sticker == None:
                        print(f"    There is no sticker with id {paste_sticker_id}")
                        CLI.__click_to_exit()

                    else:
                        CLI.__clear()
                        CLI.__message("Paste sticker")

                        print("\n", paste_sticker)

                        if CLI.__choice(["[1] Paste", "[2] Cancel"]) == 0:
                            paste_album.stick(paste_sticker)
                            print("\n    Sticker successfully pasted")
                            CLI.__clear()
                        else:
                            print("\n    Sticker not pasted")
                            CLI.__clear()

            elif user_choise == 1:
                CLI.__clear()
                CLI.__message("Remove sticker")

                remove_id = (int)(CLI.__get_input("Album id: ", int_type = True))

                remove_album = ap.search_by_id(remove_id)

                if remove_album == None:
                    print(f"    There is no album with id {remove_id}")
                    CLI.__click_to_exit()
                
                else:
                    remove_sticker_id = (int)(CLI.__get_input("Sticker id: ", int_type=True))

                    remove_sticker = sp.search_by_id(remove_sticker_id)

                    if remove_sticker == None:
                        print(f"    There is no sticker with id {remove_sticker_id}")
                        CLI.__click_to_exit()

                    else:

                        if remove_album.sticker_in_album(name=remove_sticker.get_name(), team=remove_sticker.get_time(), position=remove_sticker.get_position()) == None:
                            print("\n    No sticker in album")
                            CLI.__click_to_exit()

                        else:
                            CLI.__clear()
                            CLI.__message("Remove sticker")

                            print("\n", remove_sticker)

                            if CLI.__choice(["[1] Remove", "[2] Cancel"]) == 0:
                                remove_album.remove_sticker(name=remove_sticker.get_name(), team=remove_sticker.get_time(), position=remove_sticker.get_position())
                                print("\n    Sticker successfully Removed")
                                CLI.__click_to_exit()
                            else:
                                print("\n    Sticker not Removed")
                                CLI.__click_to_exit()

            elif user_choise == 2:
                CLI.__clear()
                CLI.__message("Insert album")

                insert_id = (int)(CLI.__get_input("Collector id: ", int_type = True))
                insert_collector = cp.search_by_id(insert_id)

                if insert_collector == None:
                    print(f"\n    There is no collector with id {insert_id}")
                    CLI.__click_to_exit()
                else:
                    insert_name = CLI.__get_input("Album name: ")
                    
                    if CLI.__choice(["[1] Insert","[2] Cancel"]) == 0:
                        ap.insert(Album(insert_name, insert_collector.id))
                        print("    Album successfully inserted")
                        CLI.__click_to_exit()

                    else:
                        print("    Album not inserted")
                        CLI.__click_to_exit()
    
            elif user_choise == 3:
                CLI.__clear()
                CLI.__message("Remove album")

                remove_id = (int)(CLI.__get_input("Album id: ", int_type = True))
                remove_album = ap.search_by_id(remove_id)

                if remove_album == None:
                    print(f"\n    There is no album with id {remove_id}")
                    CLI.__click_to_exit()

                else:
                    CLI.__clear()
                    CLI.__message("Remove album")

                    print("\n", remove_album)

                    if CLI.__choice(["[1] remove","[2] Cancel"]) == 0:
                        ap.remove(remove_id)
                        print("    Album successfully removed")
                        CLI.__click_to_exit()

                    else:
                        print("    Album not removed")
                        CLI.__click_to_exit()
            
            elif user_choise == 4:
                CLI.__clear()
                CLI.__message("Modify album")

                modify_id = (int)(CLI.__get_input("Album id: ", int_type = True))
                modify_album = ap.search_by_id(modify_id)

                if modify_album == None:
                    print(f"\n    There is no album with id {modify_id}")
                    CLI.__click_to_exit()

                else:
                    modify_loop = True

                    while modify_loop:
                        CLI.__clear()
                        CLI.__message("Modify album")

                        modify_choice = CLI.__choice(["[1] Modify name","[2] Modify Collector", "[3] Exit"])

                        if modify_choice == 2:
                            modify_loop = False
                        
                        elif modify_choice == 1:
                            modify_collector_id = (int)(CLI.__get_input("New collector id: ", int_type= True))
                            modify_collector = cp.search_by_id(modify_collector_id)
                            if modify_collector == None:
                                print(f"\n    There is no collector with id {modify_collector_id}")
                                CLI.__click_to_exit()
                            else:
                                CLI.__clear()
                                CLI.__message("Modify album")
                                print(f"    New Collector\n    {modify_collector}")
                                if CLI.__choice(["[1] Modify","[2] Cancel"]) == 0:
                                    ap.modify(modify_id, owner=modify_collector)
                                    print("\n    Album successfully modify")
                                    CLI.__click_to_exit()

                                else:
                                    print("\n    Album not modify")
                                    CLI.__click_to_exit()

                        elif modify_choice == 0:
                            modify_name = CLI.__get_input("New name:")

                            CLI.__clear()
                            CLI.__message("Modify album")

                            print(f"    New name\n    {modify_name}")
                            if CLI.__choice(["[1] Modify","[2] Cancel"]) == 0:
                                ap.modify(modify_id, name=modify_name)
                                print("\n    Album successfully modify")
                                CLI.__click_to_exit()

                            else:
                                print("\n    Album not modify")
                                CLI.__click_to_exit()

            elif user_choise == 5:
                CLI.__clear()
                CLI.__message("Search album")

                search_choise = CLI.__choice(["[1] By id","[2] By name", "[3] show all album"])
                
                if search_choise == 0:

                    search_id = (int)(CLI.__get_input("Album id: ", int_type=True))

                    Album_search = ap.search_by_id(search_id)

                    if Album_search == None:
                        print(f"\n    There is no Album with id {search_id}")
                        CLI.__click_to_exit()

                    else:
                        CLI.__clear()
                        CLI.__message("Search Albums")
                        print(Album_search)
                        CLI.__click_to_exit()

                elif search_choise == 1:

                    search_name = CLI.__get_input("Album name: ")
                    
                    Album_search = ap.search_by_str(search_name)

                    if Album_search == None:
                        print(f"\n    There is no Album with name {search_name}")
                        CLI.__click_to_exit()

                    else:
                        CLI.__clear()
                        CLI.__message("Search Albums")
                        print(Album_search)
                        CLI.__click_to_exit()

                elif search_choise == 2:
                    CLI.__clear()
                    CLI.__message("Search Albums")
                    ap.view_data()
                    CLI.__click_to_exit()

            elif user_choise == 6:
                LOOP = False

    @staticmethod
    def Trade(tp: TradePersistence, cp: CollectorPersistence, sp: StickerPersistence) -> None:
        options = ["[1] Trade", 
                   "[2] Remove", 
                   "[3] Modify", 
                   "[4] Search", 
                   "[5] Exit"]
        LOOP = True
        

        while LOOP:
            CLI.__clear()
            CLI.__message("Trade")
            
            user_choise = CLI.__choice(options)

            if user_choise == 0:

                trade1_collector_id = (int)(CLI.__get_input("Collector 1 id: ", int_type=True))
                trade1_collector = cp.search_by_id(trade1_collector_id)

                if trade1_collector == None:
                    print(f"\n    There is no collector with id {trade1_collector_id}")
                    CLI.__click_to_exit()

                else:
                    trade1_sticker_id = (int)(CLI.__get_input("Sticker 1 id: ", int_type = True))
                    trade1_sticker = sp.search_by_id(trade1_sticker_id)

                    if trade1_sticker == None:
                        print(f"\n    There is no Sticker with id {trade1_sticker_id}")
                        CLI.__click_to_exit()
                    
                    else:
                        trade2_collector_id = (int)(CLI.__get_input("Collector 2 id: ", int_type=True))
                        trade2_collector = cp.search_by_id(trade2_collector_id)

                        if trade2_collector == None:
                            print(f"\n    There is no collector with id {trade2_collector_id}")
                            CLI.__click_to_exit()

                        else:
                            trade2_sticker_id = (int)(CLI.__get_input("Sticker 2 id: ", int_type = True))
                            trade2_sticker = sp.search_by_id(trade2_sticker_id)

                            if trade2_sticker == None:
                                print(f"\n    There is no Sticker with id {trade2_sticker_id}")
                                CLI.__click_to_exit()
                    
                            else:
                                trade_obj = Trade(trade1_collector.get_id(), trade1_sticker_id, trade2_collector.get_name(), trade2_sticker_id)
                                CLI.__clear()
                                CLI.__message("stickers")
                                print(trade_obj)

                                if CLI.__choice(["[1] Trade", "[2] Cancel"]) == 0:
                                    tp.insert(trade_obj)
                                    print("\n    Trade successfully finished")
                                    CLI.__click_to_exit()
                                else:
                                    print("\n    Trade not finished")
                                    CLI.__click_to_exit()

            elif user_choise == 1:
                CLI.__clear()
                CLI.__message("Remove Trade")

                remove_id = (int)(CLI.__get_input("Trade id: ", int_type = True))
                
                CLI.__clear()
                CLI.__message("Remove Trade")

                if tp.search_by_id(remove_id) == None:
                    print(f"There is no Trade with id {remove_id}")
                    CLI.__click_to_exit()

                else:
                    print(f"    Remove ID {remove_id} Trade")
                    if CLI.__choice(["[1] Remove", "[2] Cancel"]) == 0:
                        tp.remove(remove_id)
                        print("\n    successful Trade remove")
                        CLI.__click_to_exit()
                        
                    else:
                        print("\n    Trade not removed")
                        CLI.__click_to_exit()

            elif user_choise == 2:
                CLI.__clear()
                CLI.__message("Modify Trade")

                modify_id = (int)(CLI.__get_input("Trade id: ", int_type = True))
                modify_Trade = tp.search_by_id(modify_id)

                if modify_Trade == None:
                    print(f"\n    There is no Trade with id {modify_id}")
                    CLI.__click_to_exit()

                else:
                    modify_loop = True

                    while modify_loop:
                        CLI.__clear()
                        CLI.__message("Modify Trade")

                        modify_choice = CLI.__choice(["[1] Modify collector 1","[2] Modify Collector 2", "[3] Modify sticker 1", "[4] Modify sticker 2", "[5] Exit"])

                        if modify_choice == 4:
                            modify_loop = False
                        
                        elif modify_choice == 0:
                            modify_collector1_id = (int)(CLI.__get_input("New collector id: ", int_type=True))
                            modify_collector1 = cp.search_by_id(modify_collector1_id)
                            if modify_collector1 == None:
                                print(f"\n    There is no collector with id {modify_collector1_id}")
                                CLI.__click_to_exit()
                            else:
                                CLI.__clear()
                                CLI.__message("Modify Trade")
                                print(f"    New Collector\n{modify_collector1}")
                                if CLI.__choice(["[1] Modify","[2] Cancel"]) == 0:
                                    tp.modify(modify_id,c1=modify_collector1.get_id())
                                    print("\n    Trade successfully modify")
                                    CLI.__click_to_exit()

                                else:
                                    print("\n    Trade not modify")
                                    CLI.__click_to_exit()

                        elif modify_choice == 1:
                            modify_collector2_id = (int)(CLI.__get_input("New collector id: ", int_type=True))
                            modify_collector2 = cp.search_by_id(modify_collector2_id)
                            if modify_collector2 == None:
                                print(f"\n    There is no collector with id {modify_collector2_id}")
                                CLI.__click_to_exit()
                            else:
                                CLI.__clear()
                                CLI.__message("Modify Trade")
                                print(f"    New Collector\n{modify_collector2}")
                                if CLI.__choice(["[1] Modify","[2] Cancel"]) == 0:
                                    tp.modify(modify_id, c2=modify_collector2.get_id())
                                    print("\n    Trade successfully modify")
                                    CLI.__click_to_exit()

                                else:
                                    print("\n    Trade not modify")
                                    CLI.__click_to_exit()
                    
                        elif modify_choice == 2:
                            modify_sticker1_id = (int)(CLI.__get_input("New sticker id: ", int_type= True))
                            modify_sticker1 = sp.search_by_id(modify_sticker1_id)
                            if modify_sticker1 == None:
                                print(f"\n    There is no sticker with id {modify_sticker1_id}")
                                CLI.__click_to_exit()
                            else:
                                CLI.__clear()
                                CLI.__message("Modify Trade")
                                print(f"    New sticker\n{modify_sticker1}")
                                if CLI.__choice(["[1] Modify","[2] Cancel"]) == 0:
                                    tp.modify(modify_id, s1=modify_sticker1_id)
                                    print("\n    Trade successfully modify")
                                    CLI.__click_to_exit()

                                else:
                                    print("\n    Trade not modify")
                                    CLI.__click_to_exit()
                        
                        elif modify_choice == 3:
                            modify_sticker2_id = (int)(CLI.__get_input("New sticker id: ", int_type= True))
                            modify_sticker2 = sp.search_by_id(modify_sticker2_id)
                            if modify_sticker2 == None:
                                print(f"\n    There is no sticker with id {modify_sticker2_id}")
                                CLI.__click_to_exit()
                            else:
                                CLI.__clear()
                                CLI.__message("Modify Trade")
                                print(f"    New sticker\n{modify_sticker2}")
                                if CLI.__choice(["[1] Modify","[2] Cancel"]) == 0:
                                    tp.modify(modify_id, s2=modify_sticker2_id)
                                    print("\n    Trade successfully modify")
                                    CLI.__click_to_exit()

                                else:
                                    print("\n    Trade not modify")
                                    CLI.__click_to_exit()
                                    
            elif user_choise == 3:
                CLI.__clear()
                CLI.__message("Search Trade")

                search_choice = CLI.__choice(["[1] Search by id","[2] Search by date", "[4] show all trade"])

                if search_choice == 0:
                    search_Trade_id = (int)(CLI.__get_input("Trade id: ", int_type= True))
                    search_Trade = tp.search_by_id(search_Trade_id)
                    if search_Trade == None:
                        print(f"\n    There is no trade with id {search_Trade_id}")
                        CLI.__click_to_exit()
                    else:
                        CLI.__clear()
                        CLI.__message("Search Trade")
                        print(f"\n{search_Trade}")
                        CLI.__click_to_exit()

                elif search_choice == 1:
                    search_date = CLI.__get_input("Date: ")
                    search_date = tp.search_by_str(search_date)
                    if search_date == None:
                        print(f"\n    There is no trade with date {search_date}")
                        CLI.__click_to_exit()
                    else:
                        CLI.__clear()
                        CLI.__message("Search Trade")
                        print(f"\n{search_date}")
                        CLI.__click_to_exit()
                
                elif search_choice == 2:
                    tp.view_data()
                    CLI.__click_to_exit()

            elif user_choise == 4:
                LOOP = False