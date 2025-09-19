import json

value = None

def save_config():
    global value
    with open('config.json', 'w') as f:
        json.dump(value, f, indent=4)