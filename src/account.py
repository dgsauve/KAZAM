import subprocess
import json

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

    print("Current Azure Account Information:")
    print(f"Subscription: {account_info['name']}")
    print(f"Account Type: {account_info['user']['type']}")