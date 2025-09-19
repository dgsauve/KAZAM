import subprocess
import json
from account import get_current_account_info, show_current_account_info
from startup import startup
import config

def list_accounts():
    accounts = config.value.get("accounts", [])
    if not accounts:
        print("No accounts found.")
        return

    print("Configured Accounts:")
    for account in accounts:
        print(f"Name: {account['Name']}")


def show_menu():
    print("1. List Accounts")


def get_choice():
    choice = input("Enter your choice: ")
    if choice == '1':
        list_accounts()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    startup()
    show_current_account_info()
    show_menu()
    get_choice()