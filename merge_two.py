import json

def merge_two(first_dict):
    new_dict = {}

    while True:
        print("Add a new entry:")
        key = input("key: ")

        if key == "exit":
            break

        value = input("value: ")
        new_dict[key] = int(value)

    # Merge dictionaries (new values overwrite old ones if key repeats)
    merged = {**first_dict, **new_dict}

    return json.dumps(merged)
