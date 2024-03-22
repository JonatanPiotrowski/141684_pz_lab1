from menus.base_menu import BaseMenu
from menus.main_menu import MainMenu
from menus.menu_item import MenuItem
from config.config import current_language as cl


class BorrowBookMenu(BaseMenu):
    def __init__(self, app):
        super().__init__(app)
        self.menu_items = [
            MenuItem(cl["borrow_book"], lambda: self.app.menu_manager.borrow_one_book()),
            MenuItem(cl["return_book"], lambda: self.app.menu_manager.return_one_book()),
            MenuItem(cl["previous_option"], lambda: self.app.menu_manager.switch_menu(MainMenu))
        ]