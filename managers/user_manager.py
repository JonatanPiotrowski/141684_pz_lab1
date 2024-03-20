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
        try:
            del_user_id = int(input(f"{cl['del_user_id']}: "))
            user_to_delete = next((user for user in self.users if user.id == del_user_id), None)
            if user_to_delete:
                self.users.remove(user_to_delete)
                print(f"{cl['user_deleted']}: {user_to_delete}")
            else:
                print(f"{cl['user_not_found']}")
        except ValueError:
            print(f"{cl['invalid_input']}")

    def modify_user(self):
        search_query = input(f"{cl['modify_user_search']}: ")
        try:
            search_id = int(search_query)
            users_found = [user for user in self.users if user.id == search_id]
        except ValueError:
            users_found = [user for user in self.users if search_query.lower() in user.last_name.lower()]

        if not users_found:
            print(f"{cl['user_not_found']}")
            return

        if len(users_found) > 1:
            print(f"{cl['multiple_users_found']}")
            for i, user in enumerate(users_found, start=1):
                print(f"{i}. {user}")
            user_choice = int(input(f"{cl['choose_user_to_modify']}: ")) - 1
            user_to_modify = users_found[user_choice]
        else:
            user_to_modify = users_found[0]

        modify_choice = input(f"{cl['modify_user_choice']}: ").lower()
        if modify_choice == cl['first_name']:
            new_first_name = input(f"{cl['add_name']}: ")
            user_to_modify.first_name = new_first_name
        elif modify_choice == cl['last_name']:
            new_last_name = input(f"{cl['add_surname']}: ")
            user_to_modify.last_name = new_last_name
        else:
            print(f"{cl['invalid_input']}")
            return

        print(f"{cl['user_modified']}: {user_to_modify}")

    def show_all_users(self):
        if self.users:
            for u in self.users:
                print(u)
        else:
            print(f"{cl["empty_users_list"]}")