import requests
import json
import os
from plyer import notification

JSON_FILE = "config.json"


def get_latest_commit():
    url = "https://api.github.com/repos/MaaAssistantArknights/MaaResource/branches/main"
    response = None

    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()['commit']['sha']
        else:
            notification.notify(
                title="Fetch Error",
                # type: ignore
                message=f"Failed to fetch latest commit. Status code: {response.status_code}", timeout=10)

    except requests.exceptions.ConnectionError:
        notification.notify(
            title="Network Error",
            message="Please check your network connection", timeout=10)  # type: ignore
        return None
    except Exception as e:
        notification.notify(
            title="Error", message=str(e), timeout=10)  # type: ignore
        return None


def load_config():
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, "r") as file:
            return json.load(file)
    return {}


def save_config(status):
    with open(JSON_FILE, "w") as file:
        json.dump(status, file, indent=2)


def check_status():
    latest_commit = get_latest_commit()
    config = load_config()
    if config.get("latest_commit") != latest_commit:
        notification.notify(title='MAA gets an update',
                            message='Update is downloading.', timeout=10)  # type: ignore

        if "latest_commit" not in config:
            config["latest_commit"] = {}

        config['latest_commit'] = latest_commit
        save_config(config)
        return True

    return False
