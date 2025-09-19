import subprocess
import json
import config

def get_account_name_from_config(app_id):
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