from core.app_core import AppCore
from managers.user_manager import UserManager
from managers.borrow_books_manager import BorrowBooksManager
from managers.books_manager import BooksManager
from core.menu_manager import MenuManager


class App:
    def __init__(self):
        self.core = AppCore()
        self.user_manager = UserManager()
        self.borrow_book_manager = BorrowBooksManager()
        self.books_manager = BooksManager()
        self.menu_manager = MenuManager(self)

    def run(self):
        self.menu_manager.run()


if __name__ == "__main__":
    app = App()
    app.run()
