from models.book import Book
from config.config import current_language as cl

class BooksManager:
    def __init__(self):
        self.books = []

    def add_book(self):
        title = input(f"{cl["add_book_title"]}: ")
        author = input(f"{cl["add_book_author"]}: ")
        new_book = Book(title, author)
        if new_book is not None:
            self.books.append(new_book)
        else:
            print("Próba dodania niepoprawnej książki.")
        print(f"{cl["book_added"]}: {new_book}")

    def delete_book(self):
        print("Usunięto książkę!")

    def modify_book(self):
        print("Zmodyfikowano książkę!")

    def show_all_books(self):
        if self.books:
            for b in self.books:
                print(b)
        else:
            print("Lista książek jest pusta.")