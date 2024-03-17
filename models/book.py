class Book:
    _id_counter = 1

    def __init__(self, title, author, genre=None, publication_year=None, edition_number=None):
        self.id = Book._id_counter
        Book._id_counter += 1
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_year = publication_year
        self.edition_number = edition_number

    def __repr__(self):
        return f"id: {self.id}, tytuł: {self.title}, autor: {self.author}"