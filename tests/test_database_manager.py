import pytest
import sqlite3
import os
import tempfile
from core.database_manager import DatabaseManager 

@pytest.fixture(scope='function')
def setup_db():
    temp_db = tempfile.NamedTemporaryFile(delete=False)
    test_db = temp_db.name
    temp_db.close()

    try:
        DatabaseManager.initialize_db(test_db)
        yield test_db

    finally:
        if os.path.exists(test_db):
            try:
                os.remove(test_db)
            except PermissionError:
                pass

def test_initialize_db(setup_db):
    connection = sqlite3.connect(setup_db)
    cursor = connection.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
    assert cursor.fetchone() is not None

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='books'")
    assert cursor.fetchone() is not None

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='borrow_records'")
    assert cursor.fetchone() is not None

    connection.close()

def test_add_object(setup_db):
    DatabaseManager.add_object('users', ['username', 'email', 'password'], ['testuser', 'testuser@example.com', 'password'], setup_db)

    connection = sqlite3.connect(setup_db)
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM users WHERE username = ?', ('testuser',))
    user = cursor.fetchone()

    assert user is not None
    assert user[1] == 'testuser'
    assert user[2] == 'testuser@example.com'

    connection.close()

def test_delete_object(setup_db):
    DatabaseManager.add_object('users', ['username', 'email', 'password'], ['testuser', 'testuser@example.com', 'password'], setup_db)
    connection = sqlite3.connect(setup_db)
    cursor = connection.cursor()
    cursor.execute('SELECT id FROM users WHERE username = ?', ('testuser',))
    user_id = cursor.fetchone()[0]
    connection.close()

    DatabaseManager.delete_object('users', user_id, setup_db)

    connection = sqlite3.connect(setup_db)
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
    user = cursor.fetchone()

    assert user is None

    connection.close()

def test_update_object(setup_db):
    DatabaseManager.add_object('users', ['username', 'email', 'password'], ['testuser', 'testuser@example.com', 'password'], setup_db)

    connection = sqlite3.connect(setup_db)
    cursor = connection.cursor()
    cursor.execute('SELECT id FROM users WHERE username = ?', ('testuser',))
    user_id = cursor.fetchone()[0]
    connection.close()

    DatabaseManager.update_object('users', user_id, ['email'], ['newemail@example.com'], setup_db)

    connection = sqlite3.connect(setup_db)
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
    user = cursor.fetchone()

    assert user is not None
    assert user[2] == 'newemail@example.com'

    connection.close()

def test_fetch_all_objects(setup_db):
    DatabaseManager.add_object('users', ['username', 'email', 'password'], ['testuser1', 'testuser1@example.com', 'password'], setup_db)
    DatabaseManager.add_object('users', ['username', 'email', 'password'], ['testuser2', 'testuser2@example.com', 'password'], setup_db)

    users = DatabaseManager.fetch_all_objects('users', setup_db)

    assert len(users) == 2
    assert users[0][1] == 'testuser1'
    assert users[1][1] == 'testuser2'


@pytest.mark.parametrize("username, email, password", [
    ("paramuser1", "paramuser1@example.com", "password1"),
    ("paramuser2", "paramuser2@example.com", "password2"),
    ("paramuser3", "paramuser3@example.com", "password3")
])
def test_add_object_parametrized(setup_db, username, email, password):
    DatabaseManager.add_object('users', ['username', 'email', 'password'], [username, email, password], setup_db)

    connection = sqlite3.connect(setup_db)
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()

    assert user is not None
    assert user[1] == username
    assert user[2] == email

    connection.close()

@pytest.mark.parametrize("username, email, password", [
    ("fetchuser1", "fetchuser1@example.com", "password1"),
    ("fetchuser2", "fetchuser2@example.com", "password2"),
    ("fetchuser3", "fetchuser3@example.com", "password3")
])
def test_fetch_all_objects_parametrized(setup_db, username, email, password):
    DatabaseManager.add_object('users', ['username', 'email', 'password'], [username, email, password], setup_db)

    users = DatabaseManager.fetch_all_objects('users', setup_db)

    found_user = False
    for user in users:
        if user[1] == username and user[2] == email:
            found_user = True
            break

    assert found_user
