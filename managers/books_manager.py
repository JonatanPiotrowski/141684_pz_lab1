from models.book import Book

class BooksManager:
    def __init__(self):
        self.books = []

    def add_book(self):
        title = input("Podaj tytuł książki: ")
        author = input("Podaj autora książki: ")
        new_book = Book(title, author)
        if new_book is not None:
            self.books.append(new_book)
        else:
            print("Próba dodania niepoprawnej książki.")
        print(f"Dodano nową książkę: {new_book}")

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