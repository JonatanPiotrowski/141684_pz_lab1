from menus.base_menu import BaseMenu
from menus.menu_item import MenuItem
from config.config import current_language as cl


class MainMenu(BaseMenu):
    def __init__(self, app):
        super().__init__(app)
        self.menu_items = [
            MenuItem(cl["book_rental"], lambda: self.app.menu_manager.borrow_book()),
            MenuItem(cl["manage_clients"], lambda: self.app.menu_manager.manage_users()),
            MenuItem(cl["manage_books"], lambda: self.app.menu_manager.manage_books()),
            # Opcja zmiany języka nie działa, dodam w następnych laboratoriach
            # MenuItem(cl["options_menu"], lambda: self.app.menu_manager.manage_options()),
            MenuItem(cl["exit_program"], lambda: self.app.core.exit_program())
        ]