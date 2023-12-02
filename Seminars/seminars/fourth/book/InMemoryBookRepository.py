from typing import List

from Seminars.seminars.fourth.book.Book import Book
from Seminars.seminars.fourth.book.BookRepository import BookRepository


class InMemoryBookRepository(BookRepository):
    def __init__(self):
        """
        Конструктор класса InMemoryBookRepository.

        Здесь создается некоторое фиктивное хранилище книг для демонстрационных целей.
        """
        self.books = {
            "1": Book("1", "Book1", "Author1"),
            "2": Book("2", "Book2", "Author2"),
        }

    def find_by_id(self, book_id: str) -> Book:
        """
        Метод для поиска книги по идентификатору.

        :param book_id: Идентификатор книги.
        :return: Объект класса Book, соответствующий идентификатору.
        """
        return self.books.get(book_id)

    def find_all(self) -> List[Book]:
        """
        Метод для получения списка всех книг.

        :return: Список всех книг в репозитории.
        """
        return list(self.books.values())
