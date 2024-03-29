class HotelService:
    def is_room_available(self, room_id: int) -> bool:
        """
        Метод, который проверяет, доступен ли номер.

        В реальной ситуации здесь мы бы сделали запрос к базе данных или другому сервису,
        чтобы проверить доступность комнаты. Но для простоты этого примера,
        давайте просто симулируем это поведение: предположим, что комнаты с четными номерами
        доступны, а с нечетными - нет.

        :param room_id: Идентификатор номера, который нужно проверить на доступность.
        :return: True, если номер доступен, иначе False.
        """
        return room_id % 2 == 0
