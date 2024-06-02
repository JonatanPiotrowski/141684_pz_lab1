# models/user.py

class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def __str__(self):
        return f"User({self.username}, {self.email})"
