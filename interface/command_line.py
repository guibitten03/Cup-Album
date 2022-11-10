import os
from copy import deepcopy

from simple_term_menu import TerminalMenu
import pyfiglet

from persistence import *
from models import *


class command_lines():
    @staticmethod
    def __clear() -> None:
        os.system("cls" if os.name=="nt" else "clear") or None

    @staticmethod
    def __message(mensagens: str, font: str = "slant") -> None:
        result = pyfiglet.figlet_format(mensagens, font = "slant")
        print(result)

    @staticmethod
    def __choice(options: list[str], cursor_style: tuple[str] = ("fg_red", "bold"), highlight_style: str = "standout", title: str = "" ) -> int:
        mainMenu = TerminalMenu(options, menu_cursor_style = cursor_style, menu_highlight_style = (highlight_style,), title= title)
        user_choice = mainMenu.show()
        return user_choice

    @staticmethod
    def __click_to_exit() -> None:
        option = ["Exit"]
        command_lines.__choice(option)

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
    def home() -> None:
        options = [
            "[1] Stickers",
            "[2] Collector",
            "[3] Album",
            "[4] Trade",
            "[5] exit"
        ]
        LOOP = True

        while(LOOP):
            command_lines.__clear() 
            command_lines.__message("Fifa WC Album")

            user_choice = command_lines.__choice(options, title = "choose one option")

            if user_choice == 0:
                command_lines.Stickers()

            elif user_choice == 1:
                command_lines.Collector()

            elif user_choice == 2:
                command_lines.Album()

            elif user_choice == 3:
                command_lines.Trade()

            elif user_choice == 4:
                # Salva modificações.
                LOOP = False

    @staticmethod
    def Stickers() -> None:
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
            command_lines.__clear()
            command_lines.__message("stickers")

            user_choise = command_lines.__choice(options)

            if user_choise == 0: 
                command_lines.__clear()
                command_lines.__message("Insert stickers")

                insert_teams = sticker_list_teams[command_lines.__choice(sticker_list_teams, title = "Team name:")]
                if insert_teams == "Other":
                    insert_teams = command_lines.__get_input("Team name: ")

                insert_position = sticker_list_position[command_lines.__choice(sticker_list_position, title = "Position:")]

                insert_name = command_lines.__get_input("Player name: ")

                command_lines.__clear()
                command_lines.__message("Insert stickers")
                print(f"    Team: {insert_teams}\n    Position: {insert_position}\n    Name: {insert_name}")
                
                if command_lines.__choice(["[1] Insert", "[2] Cancel"]) == 0:
                    StickerPersistence.insert(Sticker(team = insert_teams, position= insert_position, name= insert_name))
                    print("\n    sticker successfully inserted")
                    command_lines.__click_to_exit()
                
            elif user_choise == 1:
                command_lines.__clear()
                command_lines.__message("Remove stickers")

                remove_id = (int)(command_lines.__get_input("sticker id: ", int_type = True))
                
                command_lines.__clear()
                command_lines.__message("Remove stickers")

                if StickerPersistence.search_by_id(remove_id) == None:
                    print(f"There is no sticker with id {remove_id}")
                    command_lines.__click_to_exit()

                else:
                    print(f"    Remove ID {remove_id} sticker")
                    if command_lines.__choice([ "[1] Remove", "[2] Cancel" ]) == 0:
                        StickerPersistence.remove(remove_id)
                        print("    successful sticker remove")
                        command_lines.__click_to_exit()
                    else:
                        print("    sticker not removed")
                        command_lines.__click_to_exit()

            elif user_choise == 2: 
                command_lines.__clear()
                command_lines.__message("Modify stickers")

                modify_id = (int)(command_lines.__get_input("sticker id: ", int_type = True))

                if StickerPersistence.search_by_id(modify_id) == None:
                    print(f"There is no sticker with id {modify_id}.")
                    command_lines.__click_to_exit()

                else:
                    modify_loop = True

                    while modify_loop:
                        command_lines.__clear()
                        command_lines.__message("Modify stickers")

                        print(f"Modify ID {modify_id} sticker")

                        modify_choise = command_lines.__choice(modify_list)

                        if modify_choise == 0:
                            modify_team = sticker_list_teams[command_lines.__choice(sticker_list_teams, title = "\nNew team:")]

                            if modify_team == "Other":
                                modify_team = command_lines.__get_input("Team name: ")
                                
                            command_lines.__clear()
                            command_lines.__message("Modify stickers")
                            print(f"Modify ID {modify_id} sticker\n\n    New team: {modify_team}")

                            if command_lines.__choice(["Modify team", "Cancel"]) == 0:
                                StickerPersistence.modify(modify_id, team = modify_team) ##função de modify
                                print("    Team successful modify")
                                command_lines.__click_to_exit()
                            else:
                                print("    Team not modify")
                                command_lines.__click_to_exit()

                        elif modify_choise == 1:
                            modify_position = command_lines.__choice(sticker_list_position, title = "\nNew position: ")

                            command_lines.__clear()
                            command_lines.__message("Modify stickers")
                            print(f"Modify ID {modify_id} sticker\n\n    New position: {modify_position}")

                            if command_lines.__choice(["Modify position", "Cancel"]) == 0:
                                StickerPersistence.modify(modify_id, position = modify_position) ##função de modify
                                print("    position successful modify")
                                command_lines.__click_to_exit()
                            else:
                                print("    position not modify")
                                command_lines.__click_to_exit()

                        elif modify_choise == 2:
                            modify_name = command_lines.__get_input("\nNew name: ")

                            command_lines.__clear()
                            command_lines.__message("Modify stickers")
                            print(f"Modify ID {modify_id} sticker\n\n    New name: {modify_name}")

                            if command_lines.__choice(["Modify name", "Cancel"]) == 0:
                                StickerPersistence.modify(modify_id, name = modify_name) ##função de modify
                                print("    name successful modify")
                                command_lines.__click_to_exit()
                            else:
                                print("    name not modify")
                                command_lines.__click_to_exit()

                        elif modify_choise == 3:
                            modify_loop = False

            elif user_choise == 3:
                    command_lines.__clear()
                    command_lines.__message("Search stikers")

                    search_choise = command_lines.__choice(["[1] By id","[2] By name", "[3] show all stikers"])
                    
                    if search_choise == 0:

                        search_id = (int)(command_lines.__get_input("stiker id: ", int_type=True))

                        stiker_search = StickerPersistence.search_by_id(search_id)

                        if stiker_search == None:
                            print(f"\n    There is no stiker with id {search_id}")
                            command_lines.__click_to_exit()

                        else:
                            command_lines.__clear()
                            command_lines.__message("Search stikers")
                            print(stiker_search)
                            command_lines.__click_to_exit()

                    elif search_choise == 1:

                        search_name = command_lines.__get_input("stiker name: ")
                        
                        stiker_search = StickerPersistence.search_by_str(search_name)

                        if stiker_search == None:
                            print(f"\n    There is no stiker with name {search_name}")
                            command_lines.__click_to_exit()

                        else:
                            command_lines.__clear()
                            command_lines.__message("Search stikers")
                            print(stiker_search)
                            command_lines.__click_to_exit()

                    elif search_choise == 2:
                        command_lines.__clear()
                        command_lines.__message("Search stikers")
                        StickerPersistence.view_data()
                        command_lines.__click_to_exit()

            elif user_choise == 4:
                #salvar alteracoes
                LOOP = False

    @staticmethod
    def Collector() -> None:

        options = ["[1] Insert", 
                   "[2] Remove", 
                   "[3] Modify", 
                   "[4] Search", 
                   "[5] Exit"]
        
        LOOP = True
        
        while LOOP:
            command_lines.__clear()  
            command_lines.__message("Collector") 

            user_choise = command_lines.__choice(options)    
            
            if user_choise == 0:
                command_lines.__clear()  
                command_lines.__message("Insert collector") 

                insert_name = command_lines.__get_input("Collector Name: ")

                command_lines.__clear()
                command_lines.__message("Insert collector")
                print(f"    Collector Name: {insert_name}\n")

                if command_lines.__choice(["[1] Insert", "[2] Cancel"]) == 0:

                    CollectorPersistence.insert(Collector(insert_name))

                    print("    Collector successfully inserted")
                    command_lines.__click_to_exit()

                else:
                    print("    Collector not inserted")
                    command_lines.__click_to_exit()

            elif user_choise == 1:
                command_lines.__clear()
                command_lines.__message("Remove collector")

                remove_id = (int)(command_lines.__get_input("Collector id: ", int_type = True))
                
                command_lines.__clear()
                command_lines.__message("Remove collector")

                if CollectorPersistence.search_by_id(remove_id) == None:
                    print(f"There is no collector with id {remove_id}")
                    command_lines.__click_to_exit()

                else:
                    print(f"    Remove ID {remove_id} collector")
                    if command_lines.__choice(["[1] Remove", "[2] Cancel"]) == 0:
                        CollectorPersistence.remove(remove_id)
                        print("\n    successful collector remove")
                        command_lines.__click_to_exit()
                        
                    else:
                        print("\n    collector not removed")
                        command_lines.__click_to_exit()

            elif user_choise == 2:
                command_lines.__clear()
                command_lines.__message("Modify Collectors")

                modify_id = (int)(command_lines.__get_input("Collector id: ", int_type = True))

                command_lines.__clear()
                command_lines.__message("Modify Collectors")

                if CollectorPersistence.search_by_id(modify_id) == None:
                    print(f"There is no Collector with id {modify_id}")
                    command_lines.__click_to_exit()
                
                else:
                    
                    print(f"Modify ID {modify_id} collectors\n")

                    modify_name = command_lines.__get_input("New name: ")

                    if command_lines.__choice(["Modify name", "Cancel"]) == 0:
                        CollectorPersistence.modify(modify_id, name = modify_name) 
                        print("\n    Name successful modify")
                        command_lines.__click_to_exit()

                    else:
                        print("    Name not modify")
                        command_lines.__click_to_exit()

            elif user_choise == 3:
                command_lines.__clear()
                command_lines.__message("Search Collectors")

                search_choise = command_lines.__choice(["[1] By id","[2] By name", "[3] show all collectors"])
                
                if search_choise == 0:

                    search_id = (int)(command_lines.__get_input("Collector id: ", int_type=True))

                    collector_search = CollectorPersistence.search_by_id(search_id)

                    if collector_search == None:
                        print(f"\n    There is no Collector with id {search_id}")
                        command_lines.__click_to_exit()

                    else:
                        command_lines.__clear()
                        command_lines.__message("Search Collectors")
                        print(collector_search)
                        command_lines.__click_to_exit()

                elif search_choise == 1:

                    search_name = command_lines.__get_input("Collector name: ")
                    
                    collector_search = CollectorPersistence.search_by_str(search_name)

                    if collector_search == None:
                        print(f"\n    There is no Collector with name {search_name}")
                        command_lines.__click_to_exit()

                    else:
                        command_lines.__clear()
                        command_lines.__message("Search Collectors")
                        print(collector_search)
                        command_lines.__click_to_exit()

                elif search_choise == 2:
                    command_lines.__clear()
                    command_lines.__message("Search Collectors")
                    CollectorPersistence.view_data()
                    command_lines.__click_to_exit()

            elif user_choise == 4:
                LOOP = False

    @staticmethod
    def Album() -> None:
        options = ["[1] Paste sticker", 
                   "[2] Remove sticker", 
                   "[3] Insert", 
                   "[4] Remove", 
                   "[5] Modify", 
                   "[6] Search", 
                   "[7] Exit"]
        LOOP = True

        while LOOP:
            command_lines.__clear()
            command_lines.__message("sticker album")

            user_choise = command_lines.__choice(options)

            if user_choise == 0:
                command_lines.__clear()
                command_lines.__message("Paste sticker")

                paste_id = (int)(command_lines.__get_input("Album id: ", int_type = True))

                paste_album = AlbumPersistence.search_by_id(paste_id)

                if paste_album == None:
                    print(f"    There is no album with id {paste_id}")
                    command_lines.__click_to_exit()
                
                else:
                    paste_sticker_id = (int)(command_lines.__get_input("Sticker id: ", int_type = True))

                    paste_sticker = StickerPersistence.search_by_id(paste_sticker_id)

                    if paste_sticker == None:
                        print(f"    There is no sticker with id {paste_sticker_id}")
                        command_lines.__click_to_exit()

                    else:
                        command_lines.__clear()
                        command_lines.__message("Paste sticker")

                        print("\n", paste_sticker)

                        if command_lines.__choice(["[1] Paste", "[2] Cancel"]) == 0:
                            paste_album.stick(paste_sticker)
                            print("\n    Sticker successfully pasted")
                            command_lines.__clear()
                        else:
                            print("\n    Sticker not pasted")
                            command_lines.__clear()

            elif user_choise == 1:
                command_lines.__clear()
                command_lines.__message("Remove sticker")

                remove_id = (int)(command_lines.__get_input("Album id: ", int_type = True))

                remove_album = AlbumPersistence.search_by_id(remove_id)

                if remove_album == None:
                    print(f"    There is no album with id {remove_id}")
                    command_lines.__click_to_exit()
                
                else:
                    remove_sticker_id = (int)(command_lines.__get_input("Sticker id: ", int_type=True))

                    remove_sticker = StickerPersistence.search_by_id(remove_sticker_id)

                    if remove_sticker == None:
                        print(f"    There is no sticker with id {remove_sticker_id}")
                        command_lines.__click_to_exit()

                    else:

                        if remove_album.sticker_in_album(name=remove_sticker.get_name(), team=remove_sticker.get_time(), position=remove_sticker.get_position()) == None:
                            print("\n    No sticker in album")
                            command_lines.__click_to_exit()

                        else:
                            command_lines.__clear()
                            command_lines.__message("Remove sticker")

                            print("\n", remove_sticker)

                            if command_lines.__choice(["[1] Remove", "[2] Cancel"]) == 0:
                                remove_album.remove_sticker(name=remove_sticker.get_name(), team=remove_sticker.get_time(), position=remove_sticker.get_position())
                                print("\n    Sticker successfully Removed")
                                command_lines.__click_to_exit()
                            else:
                                print("\n    Sticker not Removed")
                                command_lines.__click_to_exit()

            elif user_choise == 2:
                command_lines.__clear()
                command_lines.__message("Insert album")

                insert_id = (int)(command_lines.__get_input("Collector id: ", int_type = True))
                insert_collector = CollectorPersistence.search_by_id(insert_id)

                if insert_collector == None:
                    print(f"\n    There is no collector with id {insert_id}")
                    command_lines.__click_to_exit()
                else:
                    insert_name = command_lines.__get_input("Album name: ")
                    
                    if command_lines.__choice(["[1] Insert","[2] Cancel"]) == 0:
                        AlbumPersistence.insert(Album(insert_name, insert_collector.id))
                        print("    Album successfully inserted")
                        command_lines.__click_to_exit()

                    else:
                        print("    Album not inserted")
                        command_lines.__click_to_exit()
    
            elif user_choise == 3:
                command_lines.__clear()
                command_lines.__message("Remove album")

                remove_id = (int)(command_lines.__get_input("Album id: ", int_type = True))
                remove_album = AlbumPersistence.search_by_id(remove_id)

                if remove_album == None:
                    print(f"\n    There is no album with id {remove_id}")
                    command_lines.__click_to_exit()

                else:
                    command_lines.__clear()
                    command_lines.__message("Remove album")

                    print("\n", remove_album)

                    if command_lines.__choice(["[1] remove","[2] Cancel"]) == 0:
                        AlbumPersistence.remove(remove_id)
                        print("    Album successfully removed")
                        command_lines.__click_to_exit()

                    else:
                        print("    Album not removed")
                        command_lines.__click_to_exit()
            
            elif user_choise == 4:
                command_lines.__clear()
                command_lines.__message("Modify album")

                modify_id = (int)(command_lines.__get_input("Album id: ", int_type = True))
                modify_album = AlbumPersistence.search_by_id(modify_id)

                if modify_album == None:
                    print(f"\n    There is no album with id {modify_id}")
                    command_lines.__click_to_exit()

                else:
                    modify_loop = True

                    while modify_loop:
                        command_lines.__clear()
                        command_lines.__message("Modify album")

                        modify_choice = command_lines.__choice(["[1] Modify name","[2] Modify Collector", "[3] Exit"])

                        if modify_choice == 2:
                            modify_loop = False
                        
                        elif modify_choice == 1:
                            modify_collector_id = (int)(command_lines.__get_input("New collector id: ", int_type= True))
                            modify_collector = CollectorPersistence.search_by_id(modify_collector_id)
                            if modify_collector == None:
                                print(f"\n    There is no collector with id {modify_collector_id}")
                                command_lines.__click_to_exit()
                            else:
                                command_lines.__clear()
                                command_lines.__message("Modify album")
                                print(f"    New Collector\n    {modify_collector}")
                                if command_lines.__choice(["[1] Modify","[2] Cancel"]) == 0:
                                    AlbumPersistence.modify(modify_id, owner=modify_collector)
                                    print("\n    Album successfully modify")
                                    command_lines.__click_to_exit()

                                else:
                                    print("\n    Album not modify")
                                    command_lines.__click_to_exit()

                        elif modify_choice == 0:
                            modify_name = command_lines.__get_input("New name:")

                            command_lines.__clear()
                            command_lines.__message("Modify album")

                            print(f"    New name\n    {modify_name}")
                            if command_lines.__choice(["[1] Modify","[2] Cancel"]) == 0:
                                AlbumPersistence.modify(modify_id, name=modify_name)
                                print("\n    Album successfully modify")
                                command_lines.__click_to_exit()

                            else:
                                print("\n    Album not modify")
                                command_lines.__click_to_exit()

            elif user_choise == 5:
                command_lines.__clear()
                command_lines.__message("Search album")

                search_choise = command_lines.__choice(["[1] By id","[2] By name", "[3] show all album"])
                
                if search_choise == 0:

                    search_id = (int)(command_lines.__get_input("Album id: ", int_type=True))

                    Album_search = AlbumPersistence.search_by_id(search_id)

                    if Album_search == None:
                        print(f"\n    There is no Album with id {search_id}")
                        command_lines.__click_to_exit()

                    else:
                        command_lines.__clear()
                        command_lines.__message("Search Albums")
                        print(Album_search)
                        command_lines.__click_to_exit()

                elif search_choise == 1:

                    search_name = command_lines.__get_input("Album name: ")
                    
                    Album_search = AlbumPersistence.search_by_str(search_name)

                    if Album_search == None:
                        print(f"\n    There is no Album with name {search_name}")
                        command_lines.__click_to_exit()

                    else:
                        command_lines.__clear()
                        command_lines.__message("Search Albums")
                        print(Album_search)
                        command_lines.__click_to_exit()

                elif search_choise == 2:
                    command_lines.__clear()
                    command_lines.__message("Search Albums")
                    AlbumPersistence.view_data()
                    command_lines.__click_to_exit()

            elif user_choise == 6:
                LOOP = False

    @staticmethod
    def Trade() -> None:
        options = ["[1] Trade", 
                   "[2] Remove", 
                   "[3] Modify", 
                   "[4] Search", 
                   "[5] Exit"]
        LOOP = True
        

        while LOOP:
            command_lines.__clear()
            command_lines.__message("Trade")
            
            user_choise = command_lines.__choice(options)

            if user_choise == 0:

                trade1_collector_id = (int)(command_lines.__get_input("Collector 1 id: ", int_type=True))
                trade1_collector = CollectorPersistence.search_by_id(trade1_collector_id)

                if trade1_collector == None:
                    print(f"\n    There is no collector with id {trade1_collector_id}")
                    command_lines.__click_to_exit()

                else:
                    trade1_sticker_id = (int)(command_lines.__get_input("Sticker 1 id: ", int_type = True))
                    trade1_sticker = StickerPersistence.search_by_id(trade1_sticker_id)

                    if trade1_sticker == None:
                        print(f"\n    There is no Sticker with id {trade1_sticker_id}")
                        command_lines.__click_to_exit()
                    
                    else:
                        trade2_collector_id = (int)(command_lines.__get_input("Collector 2 id: ", int_type=True))
                        trade2_collector = CollectorPersistence.search_by_id(trade2_collector_id)

                        if trade2_collector == None:
                            print(f"\n    There is no collector with id {trade2_collector_id}")
                            command_lines.__click_to_exit()

                        else:
                            trade2_sticker_id = (int)(command_lines.__get_input("Sticker 2 id: ", int_type = True))
                            trade2_sticker = StickerPersistence.search_by_id(trade2_sticker_id)

                            if trade2_sticker == None:
                                print(f"\n    There is no Sticker with id {trade2_sticker_id}")
                                command_lines.__click_to_exit()
                    
                            else:
                                trade_obj = Trade(trade1_collector.get_id(), trade1_sticker_id, trade2_collector.get_name(), trade2_sticker_id)
                                command_lines.__clear()
                                command_lines.__message("stickers")
                                print(trade_obj)

                                if command_lines.__choice(["[1] Trade", "[2] Cancel"]) == 0:
                                    TradePersistence.insert(trade_obj)
                                    print("\n    Trade successfully finished")
                                    command_lines.__click_to_exit()
                                else:
                                    print("\n    Trade not finished")
                                    command_lines.__click_to_exit()

            elif user_choise == 1:
                command_lines.__clear()
                command_lines.__message("Remove Trade")

                remove_id = (int)(command_lines.__get_input("Trade id: ", int_type = True))
                
                command_lines.__clear()
                command_lines.__message("Remove Trade")

                if TradePersistence.search_by_id(remove_id) == None:
                    print(f"There is no Trade with id {remove_id}")
                    command_lines.__click_to_exit()

                else:
                    print(f"    Remove ID {remove_id} Trade")
                    if command_lines.__choice(["[1] Remove", "[2] Cancel"]) == 0:
                        TradePersistence.remove(remove_id)
                        print("\n    successful Trade remove")
                        command_lines.__click_to_exit()
                        
                    else:
                        print("\n    Trade not removed")
                        command_lines.__click_to_exit()

            elif user_choise == 2:
                command_lines.__clear()
                command_lines.__message("Modify Trade")

                modify_id = (int)(command_lines.__get_input("Trade id: ", int_type = True))
                modify_Trade = TradePersistence.search_by_id(modify_id)

                if modify_Trade == None:
                    print(f"\n    There is no Trade with id {modify_id}")
                    command_lines.__click_to_exit()

                else:
                    modify_loop = True

                    while modify_loop:
                        command_lines.__clear()
                        command_lines.__message("Modify Trade")

                        modify_choice = command_lines.__choice(["[1] Modify collector 1","[2] Modify Collector 2", "[3] Modify sticker 1", "[4] Modify sticker 2", "[5] Exit"])

                        if modify_choice == 4:
                            modify_loop = False
                        
                        elif modify_choice == 0:
                            modify_collector1_id = (int)(command_lines.__get_input("New collector id: ", int_type=True))
                            modify_collector1 = CollectorPersistence.search_by_id(modify_collector1_id)
                            if modify_collector1 == None:
                                print(f"\n    There is no collector with id {modify_collector1_id}")
                                command_lines.__click_to_exit()
                            else:
                                command_lines.__clear()
                                command_lines.__message("Modify Trade")
                                print(f"    New Collector\n{modify_collector1}")
                                if command_lines.__choice(["[1] Modify","[2] Cancel"]) == 0:
                                    TradePersistence.modify(modify_id,c1=modify_collector1.get_id())
                                    print("\n    Trade successfully modify")
                                    command_lines.__click_to_exit()

                                else:
                                    print("\n    Trade not modify")
                                    command_lines.__click_to_exit()

                        elif modify_choice == 1:
                            modify_collector2_id = (int)(command_lines.__get_input("New collector id: ", int_type=True))
                            modify_collector2 = CollectorPersistence.search_by_id(modify_collector2_id)
                            if modify_collector2 == None:
                                print(f"\n    There is no collector with id {modify_collector2_id}")
                                command_lines.__click_to_exit()
                            else:
                                command_lines.__clear()
                                command_lines.__message("Modify Trade")
                                print(f"    New Collector\n{modify_collector2}")
                                if command_lines.__choice(["[1] Modify","[2] Cancel"]) == 0:
                                    TradePersistence.modify(modify_id, c2=modify_collector2.get_id())
                                    print("\n    Trade successfully modify")
                                    command_lines.__click_to_exit()

                                else:
                                    print("\n    Trade not modify")
                                    command_lines.__click_to_exit()
                    
                        elif modify_choice == 2:
                            modify_sticker1_id = (int)(command_lines.__get_input("New sticker id: ", int_type= True))
                            modify_sticker1 = StickerPersistence.search_by_id(modify_sticker1_id)
                            if modify_sticker1 == None:
                                print(f"\n    There is no sticker with id {modify_sticker1_id}")
                                command_lines.__click_to_exit()
                            else:
                                command_lines.__clear()
                                command_lines.__message("Modify Trade")
                                print(f"    New sticker\n{modify_sticker1}")
                                if command_lines.__choice(["[1] Modify","[2] Cancel"]) == 0:
                                    TradePersistence.modify(modify_id, s1=modify_sticker1_id)
                                    print("\n    Trade successfully modify")
                                    command_lines.__click_to_exit()

                                else:
                                    print("\n    Trade not modify")
                                    command_lines.__click_to_exit()
                        
                        elif modify_choice == 3:
                            modify_sticker2_id = (int)(command_lines.__get_input("New sticker id: ", int_type= True))
                            modify_sticker2 = StickerPersistence.search_by_id(modify_sticker2_id)
                            if modify_sticker2 == None:
                                print(f"\n    There is no sticker with id {modify_sticker2_id}")
                                command_lines.__click_to_exit()
                            else:
                                command_lines.__clear()
                                command_lines.__message("Modify Trade")
                                print(f"    New sticker\n{modify_sticker2}")
                                if command_lines.__choice(["[1] Modify","[2] Cancel"]) == 0:
                                    TradePersistence.modify(modify_id, s2=modify_sticker2_id)
                                    print("\n    Trade successfully modify")
                                    command_lines.__click_to_exit()

                                else:
                                    print("\n    Trade not modify")
                                    command_lines.__click_to_exit()
                                    
            elif user_choise == 3:
                command_lines.__clear()
                command_lines.__message("Search Trade")

                search_choice = command_lines.__choice(["[1] Search by id","[2] Search by date", "[4] show all trade"])

                if search_choice == 0:
                    search_Trade_id = (int)(command_lines.__get_input("Trade id: ", int_type= True))
                    search_Trade = TradePersistence.search_by_id(search_Trade_id)
                    if search_Trade == None:
                        print(f"\n    There is no trade with id {search_Trade_id}")
                        command_lines.__click_to_exit()
                    else:
                        command_lines.__clear()
                        command_lines.__message("Search Trade")
                        print(f"\n{search_Trade}")
                        command_lines.__click_to_exit()

                elif search_choice == 1:
                    search_date = command_lines.__get_input("Date: ")
                    search_date = TradePersistence.search_by_str(search_date)
                    if search_date == None:
                        print(f"\n    There is no trade with date {search_date}")
                        command_lines.__click_to_exit()
                    else:
                        command_lines.__clear()
                        command_lines.__message("Search Trade")
                        print(f"\n{search_date}")
                        command_lines.__click_to_exit()
                
                elif search_choice == 2:
                    TradePersistence.view_data()
                    command_lines.__click_to_exit()

            elif user_choise == 4:
                LOOP = False