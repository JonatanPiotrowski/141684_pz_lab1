from menus.base_menu import BaseMenu
from menus.main_menu import MainMenu
from menus.menu_item import MenuItem


class BorrowBookMenu(BaseMenu):
    def __init__(self, app):
        super().__init__(app)
        self.menu_items = [
            MenuItem("Wypożyczenie książki", lambda: self.app.menu_manager.borrow_one_book()),
            MenuItem("Zwrot książki", lambda: self.app.menu_manager.return_one_book()),
            MenuItem("Powrót", lambda: self.app.menu_manager.switch_menu(MainMenu))
        ]