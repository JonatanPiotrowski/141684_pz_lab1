import pytest
from core.database_manager import DatabaseManager

@pytest.fixture
def db_manager():
    db_manager = DatabaseManager()
    db_manager.initialize_db()
    return db_manager

def test_add_object(db_manager):
    db_manager.add_object('users', ['username', 'email', 'password'], ['test_user', 'test_email', 'test_password'])
    users = db_manager.fetch_all_objects('users')
    assert any(user['username'] == 'test_user' for user in users)

def test_delete_object(db_manager):
    db_manager.add_object('users', ['username', 'email', 'password'], ['user_to_delete', 'email', 'password'])
    user_id = db_manager.fetch_all_objects('users')[0]['id']
    db_manager.delete_object('users', user_id)
    users = db_manager.fetch_all_objects('users')
    assert not any(user['id'] == user_id for user in users)

def test_update_object(db_manager):
    db_manager.add_object('users', ['username', 'email', 'password'], ['user_to_modify', 'email', 'password'])
    user_id = db_manager.fetch_all_objects('users')[0]['id']
    db_manager.update_object('users', user_id, ['username', 'email'], ['new_username', 'new_email'])
    user = db_manager.fetch_all_objects('users')[0]
    assert user['username'] == 'new_username'
    assert user['email'] == 'new_email'
