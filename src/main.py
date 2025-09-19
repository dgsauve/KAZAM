from account import show_current_account_info
from startup import startup
from menu import show_menu, get_choice

if __name__ == "__main__":
    startup()
    show_current_account_info()
    while True:
        show_menu()
        get_choice()