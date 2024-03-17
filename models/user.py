from config.config import current_language

class User:
    _id_counter = 1

    def __init__(self, first_name, last_name, address=None, phone=None, email=None):
        self.id = User._id_counter
        User._id_counter += 1
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.phone = phone
        self.email = email

    def __repr__(self):
        return f"({self.id}, {self.first_name}, {self.last_name})"