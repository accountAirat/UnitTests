import unittest
from unittest.mock import Mock

from Seminars.seminars.fourth.database.DataProcessor import DataProcessor
from Seminars.seminars.fourth.hotel.BookingService import BookingService
from Seminars.seminars.fourth.message.NotificationService import NotificationService
from Seminars.seminars.fourth.weather.WeatherReporter import WeatherReporter


class TestWeatherReporter(unittest.TestCase):
    """
    // 4.3. Предположим, у вас есть класс WeatherService, который имеет метод getCurrentTemperature(),
    // обращающийся к внешнему API для получения информации о текущей температуре.
    // Вам нужно протестировать другой класс, WeatherReporter, который использует WeatherService.
    // Создайте мок-объект для WeatherService с использованием Mockito.
    """

    def test_generate_report(self):
        # Создаем мок-объект для WeatherService
        mock_weather_service = Mock()
        mock_weather_service.get_current_temperature.return_value = 25

        # Создаем экземпляр WeatherReporter, передавая мок-объект в конструктор
        weather_reporter = WeatherReporter(mock_weather_service)

        # Вызываем метод generate_report
        report = weather_reporter.generate_report()

        # Проверяем, что метод get_current_temperature был вызван
        mock_weather_service.get_current_temperature.assert_called_once()

        # Проверяем, что отчет содержит ожидаемую температуру
        self.assertIn("Текущая температура: 25 градусов.", report)

    """
    // 4.4.
    //Вам необходимо написать тест с использованием моков для сервиса бронирования отелей.
    //Условие: У вас есть класс HotelService с методом public boolean isRoomAvailable(int roomId), который обычно проверяет, доступен ли номер в отеле.
    //Вам необходимо проверить правильность работы класса BookingService, который использует HotelService для бронирования номера, если он доступен.
    """
    def test_book_room(self):
        # Создаем мок-объект для HotelService
        mock_hotel_service = Mock()
        mock_hotel_service.is_room_available.return_value = True

        # Создаем экземпляр BookingService, передавая мок-объект в конструктор
        booking_service = BookingService(mock_hotel_service)

        # Вызываем метод bookRoom
        result = booking_service.book_room(2)

        # Проверяем, что метод is_room_available был вызван
        mock_hotel_service.is_room_available.assert_called_once_with(2)

        # Проверяем, что результат равен ожидаемому значению (True)
        self.assertTrue(result)

    """
     4.5. Вам нужно написать тест с использованием моков для сервиса отправки сообщений.
      Условие: У вас есть класс MessageService с методом public void sendMessage(String message, String recipient),
      который отправляет сообщение получателю.
      Вам необходимо проверить правильность работы класса NotificationService,
      который использует MessageService для отправки уведомлений.
    """
    def test_send_notification(self):
        # Создаем мок-объект для MessageService
        mock_message_service = Mock()

        # Создаем экземпляр NotificationService, передавая мок-объект в конструктор
        notification_service = NotificationService(mock_message_service)

        # Вызываем метод send_notification
        notification_service.send_notification("Привет!", "Анна")

        # Проверяем, что метод sendMessage был вызван
        mock_message_service.send_message.assert_called_once_with("Привет!", "Анна")

    """
    4.6.Вам требуется протестировать класс, который обрабатывает запросы к базе данных.
    Условие: У вас есть класс Database с методом public List<String> query(String sql),
    который выполняет SQL-запрос и возвращает результат.
    Вам необходимо проверить правильность работы класса DataProcessor, который использует
    Database для выполнения запроса и обработки результатов.
    """
    def test_process_data(self):
        # Создаем мок-объект для Database
        mock_database = Mock()
        mock_database.query.return_value = ["Data1", "Data2", "Data3"]

        # Создаем экземпляр DataProcessor, передавая мок-объект в конструктор
        data_processor = DataProcessor(mock_database)

        # Вызываем метод processData
        data = data_processor.process_data("SELECT * FROM table")

        # Проверяем, что метод query был вызван
        mock_database.query.assert_called_once_with("SELECT * FROM table")

        # Проверяем, что результат равен ожидаемому списку
        self.assertEqual(data, ["Data1", "Data2", "Data3"])

    if __name__ == '__main__':
        unittest.main()


if __name__ == '__main__':
    unittest.main()
