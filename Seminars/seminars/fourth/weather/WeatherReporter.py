from Seminars.seminars.fourth.weather.WeatherService import WeatherService


class WeatherReporter:
    def __init__(self, weather_service: WeatherService):
        """
        Конструктор класса WeatherReporter.

        :param weather_service: Сервис погоды для использования в отчетах.
        """
        self.weather_service = weather_service

    def generate_report(self) -> str:
        """
        Метод для генерации отчета о погоде.

        :return: Текущая температура в виде строки.
        """
        temperature = self.weather_service.get_current_temperature()
        return f"Текущая температура: {temperature} градусов."
