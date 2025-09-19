import subprocess
import json
import config
import keyring

"""
Account information
"""
def get_account_name_from_config(app_id):
    """
    Retrieves the account name from the config based on ApplicationId.
    """
    accounts = config.value.get("accounts", [])
    for account in accounts:
        if account["ApplicationId"] == app_id:
            return account["Name"]
    
    return None


def get_current_account_info():
    """
    Uses the Azure CLI to retrieve current account information.

    Returns:
        dict or None: Parsed JSON account info, or None on failure.
    """
    result = subprocess.run(['az.cmd', 'account', 'show'], capture_output=True, text=True)
    if result.returncode != 0:
        print("Error retrieving account information:", result.stderr)
        return None
    
    return json.loads(result.stdout)


def show_current_account_info():
    """
    Displays current Azure subscription and account type.
    """
    account_info = get_current_account_info()
    if account_info is None:
        print("Unable to fetch Azure account info.")
        return

    # Resolve the account name from config if possible
    name = get_account_name_from_config(account_info['user']['name'])
    if name is None:
        name = account_info['user']['name']

    print("Current Azure Account Information:")
    print(f"Subscription: {name}")
    print(f"Account Type: {account_info['user']['type']}")


def list_accounts():
    accounts = config.value.get("accounts", [])
    if not accounts:
        print("No accounts found.")
        return

    print("Configured Accounts:")
    for account in accounts:
        print(f"Name: {account['Name']}")


"""
Account management functions
"""
def add_account():
    """
    Adds a new account to the configuration.
    """
    name = input("Enter account name: ")
    app_id = input("Enter Application ID: ")
    tenant_id = input("Enter Tenant ID: ")
    secret = input("Enter Secret (stored in keyring): ")
    new_account = {
        "Name": name,
        "ApplicationId": app_id,
        "TenantId": tenant_id
    }

    # Store secret in keyring
    store_secret_in_keyring(name, secret)

    accounts = config.value.get("accounts", [])
    accounts.append(new_account)
    config.value["accounts"] = accounts
    config.save_config()
    
    print(f"Account '{name}' added.")


def show_account_details_by_name():
    """
    Shows account details by name.
    """
    list_accounts()
    name = input("\nEnter account name to view details: ")
    print()
    accounts = config.value.get("accounts", [])
    for account in accounts:
        if account["Name"] == name:
            print(f"Details for account '{name}':")
            print(f"  Application ID: {account['ApplicationId']}")
            print(f"  Tenant ID: {account['TenantId']}")
            secret = get_secret_from_keyring(name)
            if secret:
                print(f"  Secret: {secret}")
            else:
                print("  Secret: Not found in keyring.")
            return
    
    print(f"No account found with the name '{name}'.")


def remove_account():
    """
    Removes an account and it's secret from the configuration and keyring.
    """
    list_accounts()
    name = input("\nEnter account name to remove: ")
    accounts = config.value.get("accounts", [])
    for i, account in enumerate(accounts):
        if account["Name"] == name:
            keyring.delete_password("azure_accounts", name)
            del accounts[i]
            config.value["accounts"] = accounts
            config.save_config()
            print(f"Account '{name}' removed.")
            return
    
    print(f"No account found with the name '{name}'.")


"""
Keyring management functions
"""
def store_secret_in_keyring(account_name, secret):
    """
    Stores the secret in the system keyring.
    """
    keyring.set_password("azure_accounts", account_name, secret)
    print(f"Secret for account '{account_name}' stored in keyring.")


def get_secret_from_keyring(account_name):
    """
    Retrieves the secret from the system keyring.
    """
    return keyring.get_password("azure_accounts", account_name)


