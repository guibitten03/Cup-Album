#from models import *
import os

try:
    from simple_term_menu import TerminalMenu ######
except ImportError as impErr:
    print(f"[Error]: Failed to import --> {impErr.args[0]}.")
    print("Use: pip install simple_term_menu")
    exit(1)

import pyfiglet

class command_lines():

    @staticmethod
    def __clear() -> None:
        os.system("cls" if os.name=="nt" else "clear") or None

    @staticmethod
    def message(mensagens: str, font: str = "slant") -> None:
        result = pyfiglet.figlet_format(mensagens, font = "slant")
        print(result)

    @staticmethod
    def choice(options: list[str], cursor_style: tuple[str] = ("fg_red", "bold"), highlight_style = "standout") -> str:
        command_lines.__clear()

        mainMenu = TerminalMenu(options, menu_cursor_style = cursor_style, menu_highlight_style = (highlight_style,), )
        user_choice = mainMenu.show()
        return options[user_choice]

options = ['a', 'b', 'c', 'd']

#if command_lines.choice(options) == 'a':
#    print('deu certo')
  
command_lines.message("tete")