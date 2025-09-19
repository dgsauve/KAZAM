import subprocess
import json
import config

def startup():
    """
    Startup routine to ensure Azure CLI is installed and user is logged in.
    """
    try:
        subprocess.run(['az.cmd', '--version'], check=True, capture_output=True)
    except subprocess.CalledProcessError:
        print("Azure CLI is not installed. Please install it from https://aka.ms/azcli.")
        return

    try:
        subprocess.run(['az.cmd', 'account', 'show'], check=True, capture_output=True)
    except subprocess.CalledProcessError:
        print("You are not logged in to Azure CLI. Please run 'az login' to log in.")
        return
    
    try:
        config.value = json.load(open('config.json'))
    except FileNotFoundError:
        print("Configuration file not found.")
        # with open('config.json', 'w') as f:
            # json.dump({"accounts": []}, f)