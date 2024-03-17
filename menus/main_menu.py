from menus.base_menu import BaseMenu
from menus.menu_item import MenuItem
from config.config import current_language as cl


class MainMenu(BaseMenu):
    def __init__(self, app):
        super().__init__(app)
        self.menu_items = [
            MenuItem("Wypożyczalnia książek", lambda: self.app.menu_manager.borrow_book()),
            MenuItem("Zarządzaj bazą klientów", lambda: self.app.menu_manager.manage_users()),
            MenuItem("Zarządzaj bazą książek", lambda: self.app.menu_manager.manage_books()),
            MenuItem(f"{cl["options_menu"]}", lambda: self.app.menu_manager.manage_options()),
            MenuItem("Wyjście z programu", lambda: self.app.core.exit_program())
        ]