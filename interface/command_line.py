from simple_term_menu import TerminalMenu
from persistence import *
from copy import deepcopy
from models import * 
import pyfiglet  
import os

class command_lines():

    @staticmethod
    def __clear() -> None:
        os.system("cls" if os.name=="nt" else "clear") or None

    @staticmethod
    def __message(mensagens: str, font: str = "slant") -> None:
        result = pyfiglet.figlet_format(mensagens, font = "slant")
        print(result)

    @staticmethod
    def __choice(options: list[str], cursor_style: tuple[str] = ("fg_red", "bold"), highlight_style: str = "standout", title: str = '' ) -> int:
        mainMenu = TerminalMenu(options, menu_cursor_style = cursor_style, menu_highlight_style = (highlight_style,), title= title)
        user_choice = mainMenu.show()
        return user_choice

    @staticmethod
    def __click_to_exit() -> None:
        option = ['Exit']
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

        stiker_persistence = StickerPersistence() ##obj stiker

        options = ['[1] Stickers', 
                   '[2] Collector', 
                   '[3] Album', 
                   '[4] Trade', 
                   '[5] exit']
        LOOP = True

        while(LOOP):
            command_lines.__clear() 
            command_lines.__message("Fifa WC Album")
            user_choice = command_lines.__choice(options, title = 'choose one option')

            if user_choice == 0:
                command_lines.Stickers(stiker_persistence)

            elif user_choice == 1:
                command_lines.Collector()

            elif user_choice == 2:
                command_lines.Album()

            elif user_choice == 3:
                command_lines.Trade()

            elif user_choice == 4:
                #salva modificacoes
                LOOP = False
    
    @staticmethod
    def Stickers(sticker_persistence) -> None:

        options = ['[1] Insert', 
                   '[2] Remove', 
                   '[3] Modify', 
                   '[4] Search', 
                   '[5] Exit']     

        modify_list = ['[1] Team', '[2] Position', '[3] Name', '[4] Exit']
        sticker_list_position = sticker_persistence.position
        sticker_list_teams = deepcopy(sticker_persistence.teams)
        sticker_list_teams.append("Other")

        LOOP = True

        while LOOP:
            command_lines.__clear()
            command_lines.__message('stickers')

            user_choise = command_lines.__choice(options)

            if user_choise == 0: 
                command_lines.__clear()
                command_lines.__message('Insert stickers')

                insert_teams = sticker_list_teams[command_lines.__choice(sticker_list_teams, title = 'Team name:')]
                if insert_teams == "Other":
                    insert_teams = command_lines.__get_input('Team name: ')

                insert_position = sticker_list_position[command_lines.__choice(sticker_list_position, title = 'Position:')]

                insert_name = command_lines.__get_input('Player name: ')

                command_lines.__clear()
                command_lines.__message('Insert stickers')
                print(f"    Team: {insert_teams}\n    Position: {insert_position}\n    Name: {insert_name}")
                
                if command_lines.__choice(['[1] Insert', '[2] Cancel']) == 0:
                    sticker_persistence.insert(insert_teams, insert_position, insert_name)
                    print("\n    sticker successfully inserted")
                    command_lines.__click_to_exit()
                
            elif user_choise == 1:
                command_lines.__clear()
                command_lines.__message('Remove stickers')

                remove_id = command_lines.__get_input('sticker id: ', int_type = True)
                
                command_lines.__clear()
                command_lines.__message('Remove stickers')

                if sticker_persistence.search_by_id(remove_id) == None:
                    print(f"There is no sticker with id {remove_id}")
                    command_lines.__click_to_exit()

                else:
                    print(f"    Remove ID {remove_id} sticker")
                    if command_lines.__choice(['[1] Remove', '[2] Cancel']) == 0:
                        sticker_persistence.remove(remove_id)
                        print("    successful sticker remove")
                        command_lines.__click_to_exit()
                    else:
                        print("    sticker not removed")
                        command_lines.__click_to_exit()

            elif user_choise == 2: 
                command_lines.__clear()
                command_lines.__message('Modify stickers')

                modify_id = command_lines.__get_input('sticker id: ', int_type = True)

                if sticker_persistence.search_by_id(modify_id) == None:
                    print(f"There is no sticker with id {modify_id}")
                    command_lines.__click_to_exit()

                else:
                    modify_loop = True

                    while modify_loop:
                        command_lines.__clear()
                        command_lines.__message('Modify stickers')
                        print(f"Modify ID {modify_id} sticker")

                        modify_choise = command_lines.__choice(modify_list)

                        if modify_choise == 0:
                            modify_team = sticker_list_teams[command_lines.__choice(sticker_list_teams, title = '\nNew team:')]
                            if modify_team == "Other":
                                modify_team = command_lines.__get_input('Team name: ')
                                
                            command_lines.__clear()
                            command_lines.__message('Modify stickers')
                            print(f"Modify ID {modify_id} sticker\n\n    New team: {modify_team}")

                            if command_lines.__choice(["Modify team", 'Cancel']) == 0:
                                sticker_persistence.modify(team_modify = modify_team) ##função de modify
                                print("    Team successful modify")
                                command_lines.__click_to_exit()
                            else:
                                print("    Team not modify")
                                command_lines.__click_to_exit()

                        elif modify_choise == 1:
                            modify_position = command_lines.__choice(sticker_list_position, title = '\nNew position: ')

                            command_lines.__clear()
                            command_lines.__message('Modify stickers')
                            print(f"Modify ID {modify_id} sticker\n\n    New position: {modify_position}")

                            if command_lines.__choice(["Modify position", 'Cancel']) == 0:
                                sticker_persistence.modify(position_modify = modify_position) ##função de modify
                                print("    position successful modify")
                                command_lines.__click_to_exit()
                            else:
                                print("    position not modify")
                                command_lines.__click_to_exit()

                        elif modify_choise == 2:
                            modify_name = command_lines.__get_input('\nNew name: ')

                            command_lines.__clear()
                            command_lines.__message('Modify stickers')
                            print(f"Modify ID {modify_id} sticker\n\n    New name: {modify_name}")

                            if command_lines.__choice(["Modify name", 'Cancel']) == 0:
                                sticker_persistence.modify(name_modify = modify_name) ##função de modify
                                print("    name successful modify")
                                command_lines.__click_to_exit()
                            else:
                                print("    name not modify")
                                command_lines.__click_to_exit()

                        elif modify_choise == 3:
                            modify_loop = False

            elif user_choise == 3:
                print("mo grande fazer depois")
                command_lines.__click_to_exit()

            elif user_choise == 4:
                #salvar alteracoes
                LOOP = False

    @staticmethod
    def Collector() -> None:

        options = ['[1] Insert', 
                   '[2] Remove', 
                   '[3] Modify', 
                   '[4] Search', 
                   '[5] Exit']
        
        LOOP = True
        
        while LOOP:
            command_lines.__clear()  
            command_lines.__message('Collector') 

            user_choise = command_lines.__choice(options, title='choose a collector')    
            
            if user_choise == 0:
                command_lines.__clear()  
                command_lines.__message('Insert collector') 

                insert_name = command_lines.__get_input("Collector Name: ")

                command_lines.__clear()
                command_lines.__message('Insert collector')
                print(f"    Collector Name: {insert_name}\n")

                if command_lines.__choice(['[1] Insert', '[2] Cancel']) == 0:
                    ##add collector
                    print("    Collector successfully inserted")
                    command_lines.__click_to_exit()
                else:
                    print("    Collector not inserted")
                    command_lines.__click_to_exit()

            elif user_choise == 1:
                command_lines.__clear()
                command_lines.__message('Remove collector')

                remove_id = command_lines.__get_input('Collector id: ', int_type = True)
                
                command_lines.__clear()
                command_lines.__message('Remove collector')

                if CollectorPersistence.search_by_id(remove_id) == None:
                    print(f"There is no collector with id {remove_id}")
                    command_lines.__click_to_exit()

                else:
                    print(f"    Remove ID {remove_id} collector")
                    if command_lines.__choice(['[1] Remove', '[2] Cancel']) == 0:
                        CollectorPersistence.remove(remove_id)
                        print("\n    successful collector remove")
                        command_lines.__click_to_exit()
                    else:
                        print("\n    collector not removed")
                        command_lines.__click_to_exit()

            elif user_choise == 2:
                pass

            elif user_choise == 3:
                pass

            elif user_choise == 4:
                LOOP = False

    @staticmethod
    def Album() -> None:
        print("ainda nao fiz")
        return
        options = ['[1] colar adesivo', 
                   '[2] Remove sticker', 
                   '[3] Insert', 
                   '[4] Remove', 
                   '[5] Modify', 
                   '[6] Search', 
                   '[7] Exit']
        options_exit = len(options)-1
        LOOP = True

        while LOOP:
            command_lines.__clear()
            command_lines.__message('sticker album')

            user_choise = command_lines.__choice(options)

            if user_choise == options_exit:
                LOOP = False

            else:
                #new page
                print(options[user_choise])
                command_lines.__click_to_exit()
    
    @staticmethod
    def Trade() -> None:
        print("ainda nao fiz")
        return
        options = ['[1] Trade', '[2] Remove', '[3] Modify', '[4] Search', '[5] Exit']
        command_lines.__clear()
        command_lines.__message('stickers')
        command_lines.__click_to_exit()
