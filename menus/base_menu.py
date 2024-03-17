class BaseMenu:
    def __init__(self, app):
        self.app = app
        self.menu_items = []

    def display(self):
        for i, item in enumerate(self.menu_items, start=1):
            print(f"{i}. {item.name}")

    def run(self):
        self.display()
        choice = int(input("Wybierz opcję: ")) - 1
        if 0 <= choice < len(self.menu_items):
            self.menu_items[choice].execute()
        else:
            print("Nieznana opcja, spróbuj ponownie.")
