from datetime import datetime
from plyer import notification
import json

with open("config.json", "r") as file:
    config = json.load(file)

def annihilation_notification():
    if datetime.now().weekday() == 6 and datetime.now().hour >= 12 and config["annihilation_notification"]:
        notification.notify(title='Annihilation Attention', message='Annihilation is completed or not?', timeout=10)