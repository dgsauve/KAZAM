import sys
from account import show_current_account_info
from startup import startup
from menu import show_menu, get_choice
from cli import execute_cli_command

if __name__ == "__main__":
    startup()
    if len(sys.argv) > 1:
        execute_cli_command()
    show_current_account_info()
    while True:
        show_menu()
        get_choice()
