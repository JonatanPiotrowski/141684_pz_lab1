import pytest
from managers.books_manager import BooksManager
from models.book import Book

@pytest.fixture
def books_manager():
    return BooksManager()

def test_add_book(books_manager, mocker):
    mocker.patch('builtins.input', side_effect=['test_title', 'test_author', 'n'])
    books_manager.add_book()
    books = books_manager.database.fetch_all_objects('books')
    assert any(book['title'] == 'test_title' for book in books)

def test_delete_book(books_manager, mocker):
    books_manager.database.add_object('books', ['title', 'author'], ['book_to_delete', 'author'])
    book_id = books_manager.database.fetch_all_objects('books')[0]['id']
    mocker.patch('builtins.input', side_effect=[str(book_id)])
    books_manager.delete_book()
    books = books_manager.database.fetch_all_objects('books')
    assert not any(book['id'] == book_id for book in books)

def test_modify_book(books_manager, mocker):
    books_manager.database.add_object('books', ['title', 'author'], ['book_to_modify', 'author'])
    book_id = books_manager.database.fetch_all_objects('books')[0]['id']
    mocker.patch('builtins.input', side_effect=[str(book_id), 'new_title', 'new_author'])
    books_manager.modify_book()
    book = books_manager.database.fetch_all_objects('books')[0]
    assert book['title'] == 'new_title'
    assert book['author'] == 'new_author'
