from config.config import current_language as cl

class BaseMenu:
    def __init__(self, app):
        self.app = app
        self.menu_items = []

    def display(self):
        for i, item in enumerate(self.menu_items, start=1):
            print(f"{i}. {item.name}")

    def run(self):
        self.display()
        try:
            choice = int(input(f"{cl["choose_option"]}: ")) - 1
            self.menu_items[choice].execute()
        except IndexError:
            print(f"{cl["invalid_input"]}")
