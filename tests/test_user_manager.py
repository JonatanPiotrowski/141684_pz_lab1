import pytest
from unittest.mock import patch, MagicMock, call
from models.user import User
from managers.user_manager import UserManager 

@pytest.fixture
def user_manager():
    um = UserManager()
    um.database = MagicMock()
    return um

@pytest.fixture
def mock_user():
    return User(username='testuser', email='test@example.com', password='password123')

def test_add_single_user(user_manager, mock_user):
    with patch('builtins.input', side_effect=['testuser', 'test@example.com', 'password123', 'n']):
        user_manager.add_user()
        user_manager.database.add_object.assert_called_once_with('users', ['username', 'email', 'password'], ['testuser', 'test@example.com', 'password123'])

def test_delete_user(user_manager):
    with patch('builtins.input', side_effect=['1']):
        user_manager.delete_user()
        user_manager.database.delete_object.assert_called_once_with('users', 1)

def test_modify_user(user_manager):
    with patch('builtins.input', side_effect=['1', 'newuser', 'new@example.com', 'newpassword']):
        user_manager.modify_user()
        user_manager.database.update_object.assert_called_once_with('users', 1, ['username', 'email', 'password'], ['newuser', 'new@example.com', 'newpassword'])

def test_fetch_all_users(user_manager):
    mock_users = [User('testuser1', 'test1@example.com', 'password1'), User('testuser2', 'test2@example.com', 'password2')]
    user_manager.database.fetch_all_objects.return_value = mock_users

    with patch('builtins.print') as mock_print:
        user_manager.fetch_all_users()
        calls = [call(mock_users[0]), call(mock_users[1])]
        mock_print.assert_has_calls(calls)

@pytest.mark.parametrize("user_input, expected_calls", [
    (['testuser1', 'test1@example.com', 'password1', 'y', 'testuser2', 'test2@example.com', 'password2', 'n'],
     [(['username', 'email', 'password'], ['testuser1', 'test1@example.com', 'password1']), (['username', 'email', 'password'], ['testuser2', 'test2@example.com', 'password2'])]),
    (['singleuser', 'single@example.com', 'singlepassword', 'n'],
     [(['username', 'email', 'password'], ['singleuser', 'single@example.com', 'singlepassword'])])
])
def test_add_user_param(user_manager, user_input, expected_calls):
    with patch('builtins.input', side_effect=user_input):
        user_manager.add_user()
        for call_args in expected_calls:
            user_manager.database.add_object.assert_any_call('users', *call_args)

@pytest.mark.parametrize("inputs, expected_args", [
    (['1', 'user1', 'user1@example.com', 'password1'], (1, ['username', 'email', 'password'], ['user1', 'user1@example.com', 'password1'])),
    (['2', 'user2', 'user2@example.com', 'password2'], (2, ['username', 'email', 'password'], ['user2', 'user2@example.com', 'password2']))
])
def test_modify_user_param(user_manager, inputs, expected_args):
    with patch('builtins.input', side_effect=inputs):
        user_manager.modify_user()
        user_manager.database.update_object.assert_called_once_with('users', *expected_args)

@pytest.mark.parametrize("user_input, expected_id", [
    ('1', 1),
    ('2', 2)
])
def test_delete_user_param(user_manager, user_input, expected_id):
    with patch('builtins.input', side_effect=[user_input]):
        user_manager.delete_user()
        user_manager.database.delete_object.assert_called_once_with('users', expected_id)
