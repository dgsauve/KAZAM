import sys
from account import list_accounts, switch_account, show_current_account_info

def execute_cli_command():
    if sys.argv[1] == "list":
        list_accounts()
    elif sys.argv[1] == "switch":
        switch_account()
    elif sys.argv[1] == "show":
        show_current_account_info()
    elif sys.argv[1] == "help":
        print("Available commands: list, switch, show, help.")
        print("Run `kazam` without arguments to enter interactive mode.")
    else:
        print(f"Unknown command: {sys.argv[1]}")
        sys.exit(1)
    sys.exit(0)