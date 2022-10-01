from simple_term_menu import TerminalMenu
from persistence import *
from copy import deepcopy
from models import * 
import pyfiglet  
import os

"""
#aqui para testes
class StickerPersistence():
    #pra facilitar no menu deixa esses atributos estaticos 👍
    teams = ['Brasil', 'Argentina', '...'] #lista com o nome dos times
    position = ['atacante', 'meia-direita', 'goleiro', '...'] 

    
    def insert(self, x, y, z):
        print("função insert")

    def remove(self, x):
        print("função remove")

    def modify(self, team_modify: str = None, position_modify: str = None, name_modify: str = None):
        print("função modify")
"""

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

        options = ['[1] Stikers', 
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
                command_lines.Stikers(stiker_persistence)

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
    def Stikers(stiker_persistence):
        options = ['[1] Insert', 
                   '[2] Remove', 
                   '[3] Modify', 
                   '[4] Search', 
                   '[5] Exit']

        insert_list_teams = deepcopy(stiker_persistence.teams)
        insert_list_teams.append("Other")

        stiker_list_position = stiker_persistence.position

        modify_list = ['[1] Team', '[2] Position', '[3] Name', '[4] Exit']

        LOOP = True

        while LOOP:
            command_lines.__clear()
            command_lines.__message('stikers')

            user_choise = command_lines.__choice(options)

            if user_choise == 0: 
                command_lines.__clear()
                command_lines.__message('Insert stikers')

                insert_teams = insert_list_teams[command_lines.__choice(insert_list_teams, title = 'Team name:')]
                if insert_teams == "Other":
                    insert_teams = command_lines.__get_input('Team name: ')

                insert_position = stiker_list_position[command_lines.__choice(stiker_list_position, title = 'Position:')]

                insert_name = command_lines.__get_input('Player name: ')

                command_lines.__clear()
                command_lines.__message('Insert stikers')
                print(f"    Team: {insert_teams}\n    Position: {insert_position}\n    Name: {insert_name}")
                
                if command_lines.__choice(['[1] Insert', '[2] Cancel']) == 0:
                    stiker_persistence.insert(insert_teams, insert_position, insert_name)
                    print("\n    sticker successfully inserted")
                    command_lines.__click_to_exit()
                
            elif user_choise == 1:
                command_lines.__clear()
                command_lines.__message('Remove stikers')

                remove_id = command_lines.__get_input('stiker id: ', int_type = True)
                
                command_lines.__clear()
                command_lines.__message('Remove stikers')

                print(f"    Remove ID {remove_id} stiker")
                if command_lines.__choice(['[1] Remove', '[2] Cancel']) == 0:
                    stiker_persistence.remove(remove_id)
                    print("    successful stiker remove")
                    command_lines.__click_to_exit()
                else:
                    print("    sticker not removed")
                    command_lines.__click_to_exit()

            elif user_choise == 2: 
                command_lines.__clear()
                command_lines.__message('Modify stikers')

                modify_id = command_lines.__get_input('stiker id: ', int_type = True)

                modify_loop = True

                while modify_loop:
                    command_lines.__clear()
                    command_lines.__message('Modify stikers')
                    print(f"Modify ID {modify_id} sticker")

                    modify_choise = command_lines.__choice(modify_list)

                    if modify_choise == 0:
                        modify_team = command_lines.__get_input('New team: ')

                        command_lines.__clear()
                        command_lines.__message('Modify stikers')
                        print(f"Modify ID {modify_id} sticker\n\n    New team: {modify_team}")

                        if command_lines.__choice(["Modify team", 'Cancel']) == 0:
                            stiker_persistence.modify(team_modify = modify_team) ##função de modify
                            print("    Team successful modify")
                            command_lines.__click_to_exit()
                        else:
                            print("    Team not modify")
                            command_lines.__click_to_exit()

                    elif modify_choise == 1:
                        modify_position = command_lines.__choice(modify_list, title = 'New position: ')

                        command_lines.__clear()
                        command_lines.__message('Modify stikers')
                        print(f"Modify ID {modify_id} sticker\n\n    New position: {modify_position}")

                        if command_lines.__choice(["Modify position", 'Cancel']) == 0:
                            stiker_persistence.modify(position_modify = modify_position) ##função de modify
                            print("    position successful modify")
                            command_lines.__click_to_exit()
                        else:
                            print("    position not modify")
                            command_lines.__click_to_exit()


                    elif modify_choise == 2:
                        modify_name = command_lines.__get_input('New name: ')

                        command_lines.__clear()
                        command_lines.__message('Modify stikers')
                        print(f"Modify ID {modify_id} sticker\n\n    New name: {modify_name}")

                        if command_lines.__choice(["Modify name", 'Cancel']) == 0:
                            stiker_persistence.modify(name_modify = modify_name) ##função de modify
                            print("    name successful modify")
                            command_lines.__click_to_exit()
                        else:
                            print("    name not modify")
                            command_lines.__click_to_exit()

                    elif modify_choise == 3:
                        modify_loop = False
            
            elif user_choise == 3:
                print("mo grande fazer depois")

            elif user_choise == 4:
                #salvar alteracoes
                LOOP = False

    @staticmethod
    def Collector():
        print("ainda não fiz")
        return
        options = ['[1] Insert', 
                   '[2] Remove', 
                   '[3] Modify', 
                   '[4] Search', 
                   '[5] Exit']
        options_exit = len(options)-1
        options_add = options_exit -1
        LOOP = True
        
        while LOOP:
            command_lines.__clear()  
            command_lines.__message('Collector') 

            user_choise = command_lines.__choice(options, title='choose a collector')    
            
            if user_choise == options_exit:
                LOOP = False
            
            elif user_choise == options_add:
                command_lines.__clear()
                command_lines.__message('Create collector')
                #cria colecionador 
                command_lines.__click_to_exit()        

            ## Função q seleciona um collector atraves do nome
            else:
                print(options[user_choise])
                command_lines.__click_to_exit() 

    @staticmethod
    def Album():
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
    def Trade():
        print("ainda nao fiz")
        return
        options = ['[1] Trade', '[2] Remove', '[3] Modify', '[4] Search', '[5] Exit']
        command_lines.__clear()
        command_lines.__message('stikers')
        command_lines.__click_to_exit()
    




command_lines.home()