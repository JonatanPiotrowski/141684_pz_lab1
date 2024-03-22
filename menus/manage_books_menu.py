from menus.base_menu import BaseMenu
from menus.main_menu import MainMenu
from menus.menu_item import MenuItem
from config.config import current_language as cl


class ManageBooksMenu(BaseMenu):
    def __init__(self, app):
        super().__init__(app)
        self.menu_items = [
            MenuItem(cl["add_book"], lambda: self.app.menu_manager.add_book()),
            MenuItem(cl["del_book"], lambda: self.app.menu_manager.delete_book()),
            MenuItem(cl["modify_book"], lambda: self.app.menu_manager.modify_book()),
            MenuItem(cl["show_all_books"], lambda: self.app.menu_manager.show_all_books()),
            MenuItem(cl["previous_option"], lambda: self.app.menu_manager.switch_menu(MainMenu))
        ]