import json

def parse_config():
    with open("settings.json", "r") as config_file:
        return json.load(config_file)
