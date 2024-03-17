from datetime import datetime

class BorrowRecord:
    def __init__(self, user, book, borrow_date=None):
        self.user = user
        self.book = book
        self.borrow_date = borrow_date if borrow_date else datetime.now()

    def __repr__(self):
        return f"BorrowRecord(User: {self.user.first_name} {self.user.last_name}, Book: {self.book.title}, Date: {self.borrow_date})"