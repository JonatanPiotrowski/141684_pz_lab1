from models.user import User
from models.book import Book
from managers.user_manager import UserManager
from managers.books_manager import BooksManager
from config.config import current_language as cl

class BorrowBooksManager:
    def __init__(self, user_manager: UserManager, books_manager: BooksManager):
        self.user_manager = user_manager
        self.books_manager = books_manager
        self.borrowed_books = {}

    def borrow_book(self, book_id, user_id):
        user = next((user for user in self.user_manager.users if user.id == user_id), None)
        book = next((book for book in self.books_manager.books if book.id == book_id), None)

        if not user or not book:
            print(cl["invalid_book_or_user_id"])
            return False

        if book_id in self.borrowed_books:
            print(cl["book_already_borrowed"])
            return False

        self.borrowed_books[book_id] = user_id
        print(cl["book_borrowed"].format(book_id=book_id, user_id=user_id))
        return True

    def return_book(self, book_id):
        if book_id not in self.borrowed_books:
            print(cl["book_not_borrowed"])
            return False

        del self.borrowed_books[book_id]
        print(cl["book_returned"].format(book_id=book_id))
        return True

    def interact_borrow_book(self):
        try:
            book_id = int(input(cl["enter_book_id_to_borrow"]))
            user_id = int(input(cl["enter_user_id"]))
            if self.borrow_book(book_id, user_id):
                print(cl["book_successfully_borrowed"])
            else:
                print(cl["book_borrow_failed"])
        except ValueError:
            print(cl["invalid_input"])

    def interact_return_book(self):
        try:
            book_id = int(input(cl["enter_book_id_to_return"]))
            if self.return_book(book_id):
                print(cl["book_successfully_returned"])
            else:
                print(cl["book_return_failed"])
        except ValueError:
            print(cl["invalid_input"])
