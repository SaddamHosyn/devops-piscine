import json

def get_recipes(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data
