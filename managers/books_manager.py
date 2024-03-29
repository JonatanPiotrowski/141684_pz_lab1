from models.book import Book
from config.config import current_language as cl

class BooksManager:
    def __init__(self):
        self.books = []

    def add_book(self):
        book_or_books = self.collect_books()
        if isinstance(book_or_books, list):
            self.books.extend(book_or_books) 
            print(f"{cl['books_added_total']}: {len(book_or_books)}")
        else:
            self.books.append(book_or_books) 
            print(f"{cl['book_added']}: {book_or_books}")

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
        search_query = input(f"{cl["modify_book_search"]}: ")
        try:
            search_id = int(search_query)
            books_found = [book for book in self.books if book.id == search_id]
        except ValueError:
            books_found = [book for book in self.books if search_query.lower() in book.title.lower() or search_query.lower() in book.author.lower()]

        if not books_found:
            print(f"{cl["book_not_found"]}")
            return

        if len(books_found) > 1:
            print(f"{cl['multiple_books_found']}")
            for i, book in enumerate(books_found, start=1):
                print(f"{i}. {book}")
            book_choice = int(input(f"{cl['choose_book_to_modify']}: ")) - 1
            book_to_modify = books_found[book_choice]
        else:
            book_to_modify = books_found[0]

        modify_choice = input(f"{cl["modify_book_choice"]}: ").lower()
        if modify_choice == cl["title"]:
            new_title = input(f"{cl["add_book_title"]}: ")
            book_to_modify.title = new_title
        elif modify_choice == cl["author"]:
            new_author = input(f"{cl["add_book_author"]}: ")
            book_to_modify.author = new_author
        else:
            print(f"{cl["invalid_input"]}")
            return

        print(f"{cl["book_modified"]}: {book_to_modify}")


    def show_all_books(self):
        if self.books:
            for b in self.books:
                print(b)
        else:
            print(f"{cl["empty_book_list"]}")