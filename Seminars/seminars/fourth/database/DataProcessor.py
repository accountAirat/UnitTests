from typing import List

from Seminars.seminars.fourth.database.Database import Database


class DataProcessor:
    def __init__(self, database: Database):
        """
        Конструктор класса DataProcessor.

        :param database: Объект класса Database для обработки данных.
        """
        self.database = database

    def process_data(self, sql: str) -> List[str]:
        """
        Метод для обработки данных с использованием SQL-запроса.

        :param sql: SQL-запрос для выполнения.
        :return: Список строк с обработанными данными.
        """
        return self.database.query(sql)
