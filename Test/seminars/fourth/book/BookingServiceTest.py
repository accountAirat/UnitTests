import unittest
from unittest.mock import Mock

from Seminars.seminars.fourth.book.Book import Book
from Seminars.seminars.fourth.book.BookRepository import BookRepository
from Seminars.seminars.fourth.book.BookService import BookService


class BookServiceTest(unittest.TestCase):

    def test_find_book_by_id(self):
        # Arrange
        repository_mock = Mock(spec=BookRepository)
        book_service = BookService(repository_mock)
        expected_book = Book(book_id="1", title="Test Book", author="Test Author")
        repository_mock.find_book_by_id.return_value = expected_book

        # Act
        result_book = book_service.find_book_by_id("1")

        # Assert
        self.assertEqual(result_book, expected_book)

    def test_find_all_books(self):
        # Arrange
        repository_mock = Mock(spec=BookRepository)
        book_service = BookService(repository_mock)
        expected_books = [Book(book_id="1", title="Test Book1", author="Test Author1"),
                          Book(book_id="2", title="Test Book2", author="Test Author2")]
        repository_mock.find_all_books.return_value = expected_books

        # Act
        result_books = book_service.find_all_books()

        # Assert
        self.assertEqual(result_books, expected_books)


if __name__ == '__main__':
    unittest.main()
