class Book:
    def __init__(self, book_id: str, title: str = "", author: str = ""):
        """
        Конструктор класса Book.

        :param book_id: Идентификатор книги.
        :param title: Название книги.
        :param author: Автор книги.
        """
        self.id = book_id
        self.title = title
        self.author = author

    def get_id(self) -> str:
        """
        Метод для получения идентификатора книги.

        :return: Идентификатор книги.
        """
        return self.id

    def set_id(self, book_id: str) -> None:
        """
        Метод для установки идентификатора книги.

        :param book_id: Новый идентификатор книги.
        """
        self.id = book_id

    def get_title(self) -> str:
        """
        Метод для получения названия книги.

        :return: Название книги.
        """
        return self.title

    def set_title(self, title: str) -> None:
        """
        Метод для установки названия книги.

        :param title: Новое название книги.
        """
        self.title = title

    def get_author(self) -> str:
        """
        Метод для получения автора книги.

        :return: Автор книги.
        """
        return self.author

    def set_author(self, author: str) -> None:
        """
        Метод для установки автора книги.

        :param author: Новый автор книги.
        """
        self.author = author
