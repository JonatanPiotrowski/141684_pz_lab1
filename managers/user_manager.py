from config.config import current_language as cl
from models.user import User
from core.database_manager import DatabaseManager

class UserManager:
    def __init__(self):
        self.database = DatabaseManager
        self.database.initialize_db()

    def add_user(self):
        user_or_users = self.collect_users()
        if isinstance(user_or_users, list):
            for user in user_or_users:
                self.database.add_object('users', ['username', 'email', 'password'], [user.username, user.email, user.password])
            print(f"{cl['users_added_total']}: {len(user_or_users)}")
        else:
            user = user_or_users
            self.database.add_object('users', ['username', 'email', 'password'], [user.username, user.email, user.password])
            print(f"{cl['user_added']}: {user}")

    def collect_users(self):
        users_to_add = []
        add_more = True

        while add_more:
            username = input(f"{cl['add_name']}: ")
            email = input(f"{cl['add_email']}: ")
            password = input(f"{cl['add_password']}: ")
            new_user = User(username, email, password)

            if isinstance(new_user, User):
                users_to_add.append(new_user)
                print(f"{cl['user_added']}: {new_user}")

            add_another = input(f"{cl['add_another_user']} (y/n): ").lower()
            add_more = add_another == 'y'

        return users_to_add[0] if len(users_to_add) == 1 else users_to_add

    def delete_user(self):
        try:
            del_user_id = int(input(f"{cl['del_user_id']}: "))
            self.database.delete_object('users', del_user_id)
            print(f"{cl['user_deleted']}: {del_user_id}")
        except ValueError:
            print(f"{cl['invalid_input']}")

    def modify_user(self):
        try:
            user_id = int(input(f"{cl['modify_user_id']}: "))
            new_username = input(f"{cl['modify_new_username']}: ")
            new_email = input(f"{cl['modify_new_email']}: ")
            new_password = input(f"{cl['modify_new_password']}: ")
            self.database.update_object('users', user_id, ['username', 'email', 'password'], [new_username, new_email, new_password])
            print(f"{cl['user_modified']}: {user_id}")
        except ValueError:
            print(f"{cl['invalid_input']}")

    def fetch_all_users(self):
        users = self.database.fetch_all_objects('users')
        for user in users:
            print(user)
