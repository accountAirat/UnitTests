import unittest
from unittest.mock import Mock


class MainTest(unittest.TestCase):
    """
    4.0. Проверка работы Mockito
    """

    def test_simple(self):
        # Создаем мок
        mockedList = Mock()

        # Используем мок
        mockedList.add("one")
        mockedList.clear()

        # Проверяем, что методы были вызваны
        assert mockedList.add("one")
        assert mockedList.clear()

    """
    4.1. Создать мок-объект Iterator, настроить поведение так,
    чтобы за два вызова next() Iterator вернул два слова  “Hello World”,
    и проверить это поведение с помощью утверждений
    """

    def test_iterator_will_return_hello_world(self):
        # Arrange
        iterator_mock = Mock()
        iterator_mock.next.side_effect = ["Hello", "World"]

        # Act & Assert
        assert "Hello" == iterator_mock.next()
        assert "World" == iterator_mock.next()


if __name__ == '__main__':
    unittest.main()
