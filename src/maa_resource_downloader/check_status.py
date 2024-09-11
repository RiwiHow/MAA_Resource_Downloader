import requests
import json
import os
from plyer import notification

JSON_FILE = "paths.json"

def get_latest_commit():
    url = "https://api.github.com/repos/MaaAssistantArknights/MaaResource/branches/main"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['commit']['sha']
    else:
        raise Exception("Failed to fetch latest commit")

def load_config():
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, "r") as file:
            return json.load(file)
    return {}

def save_config(status):
    with open(JSON_FILE, "w") as file:
        json.dump(status, file, indent = 2)

def check_status():
    latest_commit = get_latest_commit()
    config = load_config()
    if config.get("github_status", {}).get("latest_commit") != latest_commit:
        notification.notify(title = 'MAA gets an update', message = 'Update is downloading.', timeout = 10)

        if "github_status" not in config:
            config['github_status'] = {}
        config['github_status']['latest_commit'] = latest_commit
        save_config(config)
        return True

    return False