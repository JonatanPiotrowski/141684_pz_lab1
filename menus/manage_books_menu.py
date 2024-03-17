from menus.base_menu import BaseMenu
from menus.main_menu import MainMenu
from menus.menu_item import MenuItem


class ManageBooksMenu(BaseMenu):
    def __init__(self, app):
        super().__init__(app)
        self.menu_items = [
            MenuItem("Dodaj książkę do bazy", lambda: self.app.menu_manager.add_book()),
            MenuItem("Usuń książkę", lambda: self.app.menu_manager.delete_book()),
            MenuItem("Modyfikuj książkę", lambda: self.app.menu_manager.modify_book()),
            MenuItem("Pokaż listę wszystkich książek", lambda: self.app.menu_manager.show_all_books()),
            MenuItem("Powrót", lambda: self.app.menu_manager.switch_menu(MainMenu))
        ]