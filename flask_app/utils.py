import json


def load_file():
    with open("data/candidates.json", "r", encoding="utf-8") as file:
        src = json.load(file)

    return src