class Book:
    _id_counter = 1

    def __init__(self, title, author):
        self.id = Book._id_counter
        Book._id_counter += 1
        self.title = title
        self.author = author


    def __repr__(self):
        return f"id: {self.id}, tytuł: {self.title}, autor: {self.author}"