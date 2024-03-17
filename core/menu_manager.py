from menus.borrow_book_menu import BorrowBookMenu
from menus.main_menu import MainMenu
from menus.manage_books_menu import ManageBooksMenu
from menus.manage_users_menu import ManageUsersMenu

class MenuManager:
    def __init__(self, app):
        self.app = app
        self.current_menu = MainMenu(self.app)

    def run(self):
        while self.app.core.is_running:
            self.current_menu.run()

    def switch_menu(self, new_menu):
        self.current_menu = new_menu(self.app)

    def borrow_book(self):
        self.switch_menu(BorrowBookMenu)

    def manage_users(self):
        self.switch_menu(ManageUsersMenu)

    def manage_books(self):
        self.switch_menu(ManageBooksMenu)

    def add_user(self):
        self.app.user_manager.add_user()

    def delete_user(self):
        self.app.user_manager.delete_user()

    def modify_user(self):
        self.app.user_manager.modify_user()

    def borrow_one_book(self):
        self.app.borrow_book_manager.borrow_book()

    def return_one_book(self):
        self.app.borrow_book_manager.return_book()

    def add_book(self):
        self.app.books_manager.add_book()

    def delete_book(self):
        self.app.books_manager.delete_book()

    def modify_book(self):
        self.app.books_manager.modify_book()

    def show_all_books(self):
        self.app.books_manager.show_all_books()

    #dodaj obsługę menu opcji
    def manage_options(self):
        pass
