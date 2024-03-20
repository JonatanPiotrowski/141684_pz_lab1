
from menus.base_menu import BaseMenu
from menus.main_menu import MainMenu
from menus.menu_item import MenuItem


class ManageUsersMenu(BaseMenu):
    def __init__(self, app):
        super().__init__(app)
        self.menu_items = [
            MenuItem("Dodaj użytkownika", lambda: self.app.menu_manager.add_user()),
            MenuItem("Usuń użytkownika", lambda: self.app.menu_manager.delete_user()),
            MenuItem("Modyfikuj dane użytkownika", lambda: self.app.menu_manager.modify_user()),
            MenuItem("Wyświetl wszystkich użytkowników", lambda: self.app.menu_manager.show_all_users()),
            MenuItem("Powrót", lambda: self.app.menu_manager.switch_menu(MainMenu))
        ]