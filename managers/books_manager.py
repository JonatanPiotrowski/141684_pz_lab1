from models.book import Book
from config.config import current_language as cl
from core.database_manager import DatabaseManager

class BooksManager:
    def __init__(self):
        self.database = DatabaseManager
        self.database.initialize_db()

    def add_book(self):
        book_or_books = self.collect_books()
        if isinstance(book_or_books, list):
            for book in book_or_books:
                self.database.add_object('books', ['title', 'author', 'published_date', 'isbn'], [book.title, book.author, book.published_date, book.isbn])
            print(f"{cl['books_added_total']}: {len(book_or_books)}")
        else:
            book = book_or_books
            self.database.add_object('books', ['title', 'author'], [book.title, book.author])
            print(f"{cl['book_added']}: {book}")

    def collect_books(self):
        books_to_add = []
        add_more = True

        while add_more:
            title = input(f"{cl['add_book_title']}: ")
            author = input(f"{cl['add_book_author']}: ")

            new_book = Book(title, author)

            if isinstance(new_book, Book):
                books_to_add.append(new_book)
                print(f"{cl['book_added']}: {title}")

            add_another = input(f"{cl['add_another_book']} (y/n): ").lower()
            add_more = add_another == 'y'

        return books_to_add[0] if len(books_to_add) == 1 else books_to_add

    def delete_book(self):
        try:
            del_book_id = int(input(f"{cl['del_book_id']}: "))
            self.database.delete_object('books', del_book_id)
            print(f"{cl['book_deleted']}: {del_book_id}")
        except ValueError:
            print(f"{cl['invalid_input']}")

    def modify_book(self):
        try:
            book_id = int(input(f"{cl['modify_book_id']}: "))
            new_title = input(f"{cl['modify_new_title']}: ")
            new_author = input(f"{cl['modify_new_author']}: ")
            self.database.update_object('books', book_id, ['title', 'author'], [new_title, new_author])
            print(f"{cl['book_modified']}: {book_id}")
        except ValueError:
            print(f"{cl['invalid_input']}")

    def fetch_all_books(self):
        books = self.database.fetch_all_objects('books')
        for book in books:
            print(book)
