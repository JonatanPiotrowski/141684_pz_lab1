from core.app_core import AppCore
from managers.user_manager import UserManager
from managers.borrow_books_manager import BorrowBooksManager
from managers.books_manager import BooksManager
from core.menu_manager import MenuManager
from config.config import current_language as cl


class App:
    def __init__(self):
        self.core = AppCore()
        self.user_manager = UserManager()
        self.books_manager = BooksManager()
        self.borrow_books_manager = BorrowBooksManager(self.user_manager, self.books_manager)
        self.menu_manager = MenuManager(self)
        print(cl["welcome_message"])

    def run(self):
        self.menu_manager.run()


if __name__ == "__main__":
    app = App()
    app.run()
