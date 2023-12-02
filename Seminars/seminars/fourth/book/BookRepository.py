from typing import List
from abc import ABC, abstractmethod
from Seminars.seminars.fourth.book.Book import Book


class BookRepository(ABC):
    @abstractmethod
    def find_book_by_id(self, book_id: str) -> Book:
        """
        Метод для поиска книги по идентификатору.

        :param book_id: Идентификатор книги.
        :return: Объект класса Book, соответствующий идентификатору.
        """
        pass  # Реализация метода должна быть добавлена в классах, реализующих интерфейс

    @abstractmethod
    def find_all_books(self) -> List[Book]:
        """
        Метод для получения списка всех книг.

        :return: Список всех книг в репозитории.
        """
        pass  # Реализация метода должна быть добавлена в классах, реализующих интерфейс
