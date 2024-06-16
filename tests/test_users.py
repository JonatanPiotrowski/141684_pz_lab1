import pytest
from managers.user_manager import UserManager
from models.user import User

@pytest.fixture
def user_manager():
    return UserManager()

def test_add_user(user_manager, mocker):
    mocker.patch('builtins.input', side_effect=['test_user', 'test_email', 'test_password', 'n'])
    user_manager.add_user()
    users = user_manager.database.fetch_all_objects('users')
    assert any(user['username'] == 'test_user' for user in users)

def test_delete_user(user_manager, mocker):
    user_manager.database.add_object('users', ['username', 'email', 'password'], ['user_to_delete', 'email', 'password'])
    user_id = user_manager.database.fetch_all_objects('users')[0]['id']
    mocker.patch('builtins.input', side_effect=[str(user_id)])
    user_manager.delete_user()
    users = user_manager.database.fetch_all_objects('users')
    assert not any(user['id'] == user_id for user in users)

def test_modify_user(user_manager, mocker):
    user_manager.database.add_object('users', ['username', 'email', 'password'], ['user_to_modify', 'email', 'password'])
    user_id = user_manager.database.fetch_all_objects('users')[0]['id']
    mocker.patch('builtins.input', side_effect=[str(user_id), 'new_username', 'new_email'])
    user_manager.modify_user()
    user = user_manager.database.fetch_all_objects('users')[0]
    assert user['username'] == 'new_username'
    assert user['email'] == 'new_email'
