from Seminars.seminars.fourth.hotel.HotelService import HotelService


class BookingService:
    def __init__(self, hotel_service: HotelService):
        """
        Конструктор класса BookingService.

        :param hotel_service: Сервис отеля, предоставляющий информацию о номерах.
        """
        self.hotel_service = hotel_service

    def book_room(self, room_id: int) -> bool:
        """
        Метод для бронирования номера.

        :param room_id: Идентификатор номера для бронирования.
        :return: True, если номер успешно забронирован, иначе False.
        """
        if self.hotel_service.is_room_available(room_id):
            # Код, который бронирует номер.
            # Логика бронирования комнаты
            # В реальном приложении здесь бы было больше кода
            return True  # Номер забронирован
        else:
            return False  # Номер не доступен
