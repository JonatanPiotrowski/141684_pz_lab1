from config.config import current_language as cl
from models.user import User

class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self):
        user_or_users = self.collect_users()
        if isinstance(user_or_users, list):
            self.users.extend(user_or_users)
            print(f"{cl["users_added_total"]}: {len(user_or_users)}")
        else:
            self.users.append(user_or_users)
            print(f"{cl["user_added"]}: {user_or_users}")

    def collect_users(self):
        users_to_add = []
        add_more = True

        while add_more:
            name = input(f"{cl["add_name"]}: ")
            surname = input(f"{cl["add_surname"]}: ")
            new_user = User(name, surname)

            if isinstance(new_user, User):
                users_to_add.append(new_user)
                print(f"{cl['user_added']}: {new_user}")

            add_another = input(f"{cl['add_another_user']} (y/n): ").lower()
            add_more = add_another == 'y'

        return users_to_add[0] if len(users_to_add) == 1 else users_to_add

    def delete_user(self):
        print("Usunięto użytkownika")

    def modify_user(self):
        print("Zmodyfikowano użytkownika")
