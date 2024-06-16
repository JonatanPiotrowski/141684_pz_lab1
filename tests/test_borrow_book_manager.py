import pytest
from unittest.mock import Mock

from managers.user_manager import UserManager
from managers.books_manager import BooksManager
from config.config import current_language as cl
from core.database_manager import DatabaseManager
from managers.borrow_books_manager import BorrowBooksManager

mock_users = [(1, 'Alice'), (2, 'Bob')]
mock_books = [(1, 'Book A'), (2, 'Book B')]
mock_borrow_records = [(1, 1, 1), (2, 2, 2)]

@pytest.fixture
def mock_db_manager():
    db_manager = Mock(spec=DatabaseManager)
    db_manager.fetch_all_objects.side_effect = lambda table: {
        'users': mock_users,
        'books': mock_books,
        'borrow_records': mock_borrow_records
    }[table]
    db_manager.initialize_db = Mock()
    db_manager.add_object = Mock()
    db_manager.delete_object = Mock()
    return db_manager

@pytest.fixture
def borrow_books_manager(mock_db_manager):
    user_manager = Mock(spec=UserManager)
    books_manager = Mock(spec=BooksManager)
    manager = BorrowBooksManager(user_manager, books_manager)
    manager.database = mock_db_manager  
    return manager

def test_borrow_book_success(borrow_books_manager, mock_db_manager):
    mock_db_manager.fetch_all_objects.side_effect = lambda table: {
        'users': mock_users,
        'books': mock_books,
        'borrow_records': []
    }[table]

    result = borrow_books_manager.borrow_book(1, 1)
    print(f"Test borrow_book_success result: {result}")  
    assert result is True
    mock_db_manager.add_object.assert_called_once_with('borrow_records', ['user_id', 'book_id', 'borrow_date'], [1, 1, '2024-01-01'])

def test_borrow_book_invalid_user_or_book(borrow_books_manager, mock_db_manager):
    mock_db_manager.fetch_all_objects.side_effect = lambda table: {
        'users': [],
        'books': mock_books,
        'borrow_records': []
    }[table]

    result = borrow_books_manager.borrow_book(1, 1)
    print(f"Test borrow_book_invalid_user_or_book result: {result}")
    assert result is False
    mock_db_manager.add_object.assert_not_called()

def test_borrow_book_already_borrowed(borrow_books_manager, mock_db_manager):
    result = borrow_books_manager.borrow_book(1, 1)
    print(f"Test borrow_book_already_borrowed result: {result}")
    assert result is False
    mock_db_manager.add_object.assert_not_called()

def test_return_book_success(borrow_books_manager, mock_db_manager):
    result = borrow_books_manager.return_book(1)
    print(f"Test return_book_success result: {result}")
    assert result is True
    mock_db_manager.delete_object.assert_called_once_with('borrow_records', 1)

def test_return_book_not_borrowed(borrow_books_manager, mock_db_manager):
    mock_db_manager.fetch_all_objects.side_effect = lambda table: {
        'users': mock_users,
        'books': mock_books,
        'borrow_records': []
    }[table]

    result = borrow_books_manager.return_book(1)
    print(f"Test return_book_not_borrowed result: {result}") 
    assert result is False
    mock_db_manager.delete_object.assert_not_called()

@pytest.mark.parametrize("book_id, user_id, expected", [
    (1, 1, True),
    (1, 3, False),  
    (3, 1, False),  
    (2, 2, False)  
])
def test_borrow_book_parametrized(borrow_books_manager, mock_db_manager, book_id, user_id, expected):
    mock_db_manager.fetch_all_objects.side_effect = lambda table: {
        'users': mock_users,
        'books': mock_books,
        'borrow_records': [(2, 2, 2)] if book_id != 1 or user_id != 1 else []
    }[table]

    result = borrow_books_manager.borrow_book(book_id, user_id)
    print(f"Test test_borrow_book_parametrized result: {result}, expected: {expected}") 
    assert result is expected

@pytest.mark.parametrize("book_id, expected", [
    (1, True),
    (3, False) 
])
def test_return_book_parametrized(borrow_books_manager, mock_db_manager, book_id, expected):
    mock_db_manager.fetch_all_objects.side_effect = lambda table: {
        'users': mock_users,
        'books': mock_books,
        'borrow_records': [(1, 1, 1), (2, 2, 2)]
    }[table]

    result = borrow_books_manager.return_book(book_id)
    print(f"Test test_return_book_parametrized result: {result}, expected: {expected}")
    assert result is expected
