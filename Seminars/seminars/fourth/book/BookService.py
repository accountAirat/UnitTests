from typing import List

from Seminars.seminars.fourth.book.Book import Book
from Seminars.seminars.fourth.book.BookRepository import BookRepository


class BookService:
    def __init__(self, book_repository: BookRepository):
        """
        Конструктор класса BookService.

        :param book_repository: Репозиторий книг для использования в сервисе.
        """
        self.book_repository = book_repository

    def find_book_by_id(self, book_id: str) -> Book:
        """
        Метод для поиска книги по идентификатору.

        :param book_id: Идентификатор книги.
        :return: Объект класса Book, соответствующий идентификатору.
        """
        return self.book_repository.find_book_by_id(book_id)

    def find_all_books(self) -> List[Book]:
        """
        Метод для получения списка всех книг.

        :return: Список всех книг в репозитории.
        """
        return self.book_repository.find_all_books()
