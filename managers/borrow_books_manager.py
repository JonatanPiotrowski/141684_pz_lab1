from models.user import User
from models.book import Book
from managers.user_manager import UserManager
from managers.books_manager import BooksManager

class BorrowBooksManager:
    def __init__(self, user_manager: UserManager, books_manager: BooksManager):
        self.user_manager = user_manager
        self.books_manager = books_manager
        self.borrowed_books = {}

    def borrow_book(self, book_id, user_id):
        user = next((user for user in self.user_manager.users if user.id == user_id), None)
        book = next((book for book in self.books_manager.books if book.id == book_id), None)

        if not user or not book:
            print("Nieprawidłowe ID książki lub użytkownika.")
            return False

        if book_id in self.borrowed_books:
            print("Książka jest już wypożyczona.")
            return False

        self.borrowed_books[book_id] = user_id
        print(f"Książka {book_id} została wypożyczona przez użytkownika {user_id}.")
        return True

    def return_book(self, book_id):
        if book_id not in self.borrowed_books:
            print("Ta książka nie była wypożyczona.")
            return False

        del self.borrowed_books[book_id]
        print(f"Książka {book_id} została zwrócona.")
        return True

    def interact_borrow_book(self):
        try:
            book_id = int(input("Podaj ID książki do wypożyczenia: "))
            user_id = int(input("Podaj ID użytkownika: "))
            if self.borrow_book(book_id, user_id):
                print("Wypożyczono książkę.")
            else:
                print("Nie udało się wypożyczyć książki.")
        except ValueError:
            print

    def interact_return_book(self):
        book_id = int(input("Podaj ID książki do zwrotu: "))
        if self.return_book(book_id):
            print("Zwrócono książkę.")
        else:
            print("Nie udało się zwrócić książki.")