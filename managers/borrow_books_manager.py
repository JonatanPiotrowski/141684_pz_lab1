from models.user import User
from models.book import Book
from managers.user_manager import UserManager
from managers.books_manager import BooksManager
from config.config import current_language as cl
from core.database_manager import DatabaseManager

class BorrowBooksManager:
    def __init__(self, user_manager: UserManager, books_manager: BooksManager):
        self.user_manager = user_manager
        self.books_manager = books_manager
        self.database = DatabaseManager
        self.database.initialize_db()

    def borrow_book(self, book_id, user_id):
        user = self.database.fetch_all_objects('users')
        user = next((u for u in user if u[0] == user_id), None)
        book = self.database.fetch_all_objects('books')
        book = next((b for b in book if b[0] == book_id), None)

        print(f"Debug: user={user}, book={book}")  

        if not user or not book:
            print(cl["invalid_book_or_user_id"])
            return False

        borrowed_books = self.database.fetch_all_objects('borrow_records')
        print(f"Debug: borrowed_books={borrowed_books}") 
        if any(record[1] == user_id and record[2] == book_id for record in borrowed_books):
            print(cl["book_already_borrowed"])
            return False

        self.database.add_object('borrow_records', ['user_id', 'book_id', 'borrow_date'], [user_id, book_id, '2024-01-01'])
        print(cl["book_borrowed"].format(book_id=book_id, user_id=user_id))
        return True

    def return_book(self, book_id):
        borrowed_books = self.database.fetch_all_objects('borrow_records')
        borrow_record = next((record for record in borrowed_books if record[2] == book_id), None)

        if not borrow_record:
            print(cl["book_not_borrowed"])
            return False

        self.database.delete_object('borrow_records', borrow_record[0])
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
