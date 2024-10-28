from datetime import datetime
from plyer import notification
import json

JSON_FILE = "config.json"

def save_config(status):
    with open(JSON_FILE, "w") as file:
        json.dump(status, file, indent = 2)

with open("config.json", "r") as file:
    config = json.load(file)

def annihilation_notification():
    if "annihilation_flag" not in config:
        config["annihilation_flag"] = False
        save_config(config)

    if datetime.now().weekday() == 6 and datetime.now().hour >= 12 and config["annihilation_notification"] and config["annihilation_flag"]:
        notification.notify(title='Annihilation Attention', message='Annihilation is completed or not?', timeout=10)
        config["annihilation_flag"] = False
        save_config(config)

    if datetime.now().weekday() != 6:
        config["annihilation_flag"] = True
        save_config(config)

