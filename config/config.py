import json

def load_language_resources(language_code):
    file_path = f"config/resources_{language_code}.json"
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Language file for {language_code} not found.")
        return None

current_language = load_language_resources("pl")

def change_language():
    print("Available languages: en, pl")
    chosen_language = input("Choose language (en/pl): ")

    new_language_resources = load_language_resources(chosen_language)
    if new_language_resources is not None:
        global current_language
        current_language = new_language_resources
        print(current_language["language_change_success"])
    else:
        print("This language is not supported.")


