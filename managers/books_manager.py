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
            print(f"{cl["add_book_err"]}")
        print(f"{cl["book_added"]}: {new_book}")

    def delete_book(self):
        try:
            del_book_id = int(input(f"{cl["del_book_id"]}: "))
            book_to_delete = next((book for book in self.books if book.id == del_book_id), None)
            if book_to_delete:
                self.books.remove(book_to_delete)
                print(f"{cl["book_deleted"]}: {book_to_delete}")
            else:
                print(f"{cl["book_not_found"]}")
        except ValueError:
            print(f"{cl["invalid_input"]}")


    def modify_book(self):
        print("Zmodyfikowano książkę!")

    def show_all_books(self):
        if self.books:
            for b in self.books:
                print(b)
        else:
            print(f"{cl["empty_book_list"]}")