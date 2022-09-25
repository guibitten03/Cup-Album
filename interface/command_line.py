#from models import *
import os

try:
    from simple_term_menu import TerminalMenu ######
except ImportError as impErr:
    print(f"[Error]: Failed to import --> {impErr.args[0]}.")
    print("Use: pip install simple_term_menu")
    exit(1)

try:
    import pyfiglet  ######
except ImportError as impErr:
    print(f"[Error]: Failed to import --> {impErr.args[0]}.")
    print("Use: pip install pyfiglet")
    exit(1)



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
    def home():
        
        options = ['collector', 'sticker album', 'stikers', 'exit']
        LOOP = True

        while(LOOP):
            command_lines.__clear() 
            command_lines.__message("Fifa WC Album")
            user_choice = command_lines.__choice(options, title = 'choose one option')

            if user_choice == 0:
                command_lines.Collector()

            elif user_choice == 1:
                command_lines.Sticker_album()

            elif user_choice == 2:
                command_lines.Stikers()

            elif user_choice == 3:
                LOOP = False
    
    @staticmethod
    def Collector():
        #uma opção para cada colecionador na permenencia, colocar um atributo com o nome de cada colecionador
        options = ['colecionador1', 'colecionador2', 'colecionador3', 'ADD collector', 'Exit']
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
                # cria e salva um collector
                print('aqui')
                command_lines.__click_to_exit()        

            ## Função q seleciona um collector atraves do nome
            else:
                print(options[user_choise])
                command_lines.__click_to_exit() 

    @staticmethod
    def Sticker_album():
        #uma opção para cada colecionador na permenencia, colocar um atributo com o nome de cada colecionador
        options = ['colecionador1','colecionador2','colecionador3','Exit']
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
    def Stikers():
        options = ['view', 'ADD sticker', 'Delete', 'Exit']
        LOOP = True

        while LOOP:
            command_lines.__clear()
            command_lines.__message('stikers')

            user_choise = command_lines.__choice(options)

            if user_choise == 3: 
                LOOP = False

            elif user_choise == 2:
                #deletar
                print('deletar')
                command_lines.__click_to_exit()

            elif user_choise == 1: 
                #add sticker
                print('add sticker')
                command_lines.__click_to_exit()
            
            elif user_choise == 0:
                #view novo menu
                print('view novo menu')
                command_lines.__click_to_exit()
            
            

command_lines.home()