import json

def load_language_resources(language_code):
    file_path = f"config/resources_{language_code}.json"
    with open(file_path, 'r') as file:
        return json.load(file)

current_language = load_language_resources("en")