import subprocess
import json
from account import show_current_account_info, add_account, list_accounts, show_account_details_by_name
from startup import startup
import config

def show_menu():
    print("\nMenu:")
    print("1. List Accounts")
    print("2. Switch Account")
    print("3. Add Account")
    print("4. Remove Account")
    print("5. Show Account Details By Name")
    print("0. Exit\n")


def get_choice():
    choice = input("Selection: ")
    print()
    if choice == '1':
        list_accounts()
    elif choice == '3':
        add_account()
    elif choice == '5':
        show_account_details_by_name()
    elif choice == '0':
        print("Exiting...")
        exit(0)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    startup()
    show_current_account_info()
    show_menu()
    get_choice()