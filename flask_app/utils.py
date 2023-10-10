import json
import os
from pathlib import Path

def load_file():
    with open("data/candidates.json", "r", encoding="utf-8") as file:
        src = json.load(file)

    return src

def get_candidate(candidate_id):
    candidates = load_file()
    for candidate in candidates:
        if candidate["id"] == candidate_id:
            return candidate
    return "Нет такого кандидата"

def get_candidates_by_name(candidate_name):
    candidates = load_file()
    flag = False
    candidates_list = []
    for candidate in candidates:
        if candidate_name in candidate["name"]:
            flag = True
            candidates_list.append(candidate)
    if flag == False:
        return "Нет такого кандидата с таким именем"
    return candidates_list

def get_candidates_by_skill(skill_name):
    candidates = load_file()
    flag = False
    candidates_list = []
    for candidate in candidates:
        if skill_name.lower() in candidate["skills"].lower().split(", "):
            flag = True
            candidates_list.append(candidate)
    if flag == False:
        return "Ничего не найдено \n"
    return candidates_list


def get_template():
    path = Path(__file__).parent.joinpath("templates")
    files = os.listdir(path)
    files_list = []
    for file in files:
        if file == "index.html":
            pass
        else:
            files_list.append(file.split(".")[0])
    return files_list
