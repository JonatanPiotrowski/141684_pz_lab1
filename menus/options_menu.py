from menus.base_menu import BaseMenu
from menus.main_menu import MainMenu
from menus.menu_item import MenuItem
from config.config import current_language as cl


class OptionsMenu(BaseMenu):
    def __init__(self, app):
        super().__init__(app)
        self.menu_items = [
            MenuItem(cl["change_language"], lambda: self.app.menu_manager.change_language()),
            MenuItem(cl["previous_option"], lambda: self.app.menu_manager.switch_menu(MainMenu))
        ]