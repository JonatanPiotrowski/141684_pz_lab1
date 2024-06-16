import pytest
from unittest.mock import patch, MagicMock
from models.book import Book
from core.database_manager import DatabaseManager
from managers.books_manager import BooksManager

@pytest.fixture
def books_manager():
    with patch.object(DatabaseManager, 'initialize_db') as mock_db_init:
        manager = BooksManager()
        mock_db_init.assert_called_once()
    return manager

def test_add_single_book(books_manager):
    with patch('builtins.input', side_effect=['Test Title', 'Test Author', 'n']):
        with patch.object(DatabaseManager, 'add_object') as mock_add:
            books_manager.add_book()
            mock_add.assert_called_once_with('books', ['title', 'author'], ['Test Title', 'Test Author'])

def test_add_multiple_books(books_manager):
    with patch('builtins.input', side_effect=['Test Title 1', 'Test Author 1', 'y', 'Test Title 2', 'Test Author 2', 'n']):
        with patch.object(DatabaseManager, 'add_object') as mock_add:
            books_manager.add_book()
            assert mock_add.call_count == 2

def test_delete_book(books_manager):
    with patch('builtins.input', side_effect=['1']):
        with patch.object(DatabaseManager, 'delete_object') as mock_delete:
            books_manager.delete_book()
            mock_delete.assert_called_once_with('books', 1)

def test_modify_book(books_manager):
    with patch('builtins.input', side_effect=['1', 'New Title', 'New Author']):
        with patch.object(DatabaseManager, 'update_object') as mock_update:
            books_manager.modify_book()
            mock_update.assert_called_once_with('books', 1, ['title', 'author'], ['New Title', 'New Author'])

def test_fetch_all_books(books_manager):
    with patch.object(DatabaseManager, 'fetch_all_objects', return_value=[{'title': 'Test Title', 'author': 'Test Author'}]):
        with patch('builtins.print') as mock_print:
            books_manager.fetch_all_books()
            mock_print.assert_called_with({'title': 'Test Title', 'author': 'Test Author'})

@pytest.mark.parametrize("input_values, expected_calls", [
    (['Title 1', 'Author 1', 'n'], 1),
    (['Title 1', 'Author 1', 'y', 'Title 2', 'Author 2', 'n'], 2),
])
def test_add_book_param(books_manager, input_values, expected_calls):
    with patch('builtins.input', side_effect=input_values):
        with patch.object(DatabaseManager, 'add_object') as mock_add:
            books_manager.add_book()
            assert mock_add.call_count == expected_calls

@pytest.mark.parametrize("input_value, expected_id", [
    ('1', 1),
    ('5', 5),
])
def test_delete_book_param(books_manager, input_value, expected_id):
    with patch('builtins.input', side_effect=[input_value]):
        with patch.object(DatabaseManager, 'delete_object') as mock_delete:
            books_manager.delete_book()
            mock_delete.assert_called_once_with('books', expected_id)

@pytest.mark.parametrize("input_values, expected_params", [
    (['1', 'Updated Title 1', 'Updated Author 1'], [1, ['title', 'author'], ['Updated Title 1', 'Updated Author 1']]),
    (['2', 'Updated Title 2', 'Updated Author 2'], [2, ['title', 'author'], ['Updated Title 2', 'Updated Author 2']]),
])
def test_modify_book_param(books_manager, input_values, expected_params):
    with patch('builtins.input', side_effect=input_values):
        with patch.object(DatabaseManager, 'update_object') as mock_update:
            books_manager.modify_book()
            mock_update.assert_called_once_with('books', *expected_params)
