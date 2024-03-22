
from menus.base_menu import BaseMenu
from menus.main_menu import MainMenu
from menus.menu_item import MenuItem
from config.config import current_language as cl


class ManageUsersMenu(BaseMenu):
    def __init__(self, app):
        super().__init__(app)
        self.menu_items = [
            MenuItem(cl["add_user"], lambda: self.app.menu_manager.add_user()),
            MenuItem(cl["delete_user"], lambda: self.app.menu_manager.delete_user()),
            MenuItem(cl["modify_user"], lambda: self.app.menu_manager.modify_user()),
            MenuItem(cl["show_all_users"], lambda: self.app.menu_manager.show_all_users()),
            MenuItem(cl["previous_option"], lambda: self.app.menu_manager.switch_menu(MainMenu))
        ]