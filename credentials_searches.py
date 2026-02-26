import json
import os

def credentials_search():
    if not os.path.isfile("logs.json"):
        return  # File does not exist, do nothing

    try:
        with open("logs.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return  # Invalid JSON or empty file, do nothing

    found = {}

    # Recursive function to search nested dictionaries
    def search_dict(d):
        for key, value in d.items():
            if key in ("password", "secret"):
                found[key] = value
            elif isinstance(value, dict):
                search_dict(value)

    if isinstance(data, dict):
        search_dict(data)
    
    if found:
        with open("credentials.json", "w", encoding="utf-8") as f_out:
            json.dump(found, f_out, indent=2)
