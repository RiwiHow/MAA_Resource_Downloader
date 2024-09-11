import json

def read_path(file_path: str) -> dict:
    with open(file_path, "r") as file:
        paths = json.load(file)

    return paths