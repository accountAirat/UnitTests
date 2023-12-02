from Seminars.seminars.fourth.message.MessageService import MessageService


class NotificationService:
    def __init__(self, message_service: MessageService):
        """
        Конструктор класса NotificationService.

        :param message_service: Сервис сообщений для использования в уведомлениях.
        """
        self.message_service = message_service

    def send_notification(self, message: str, recipient: str) -> None:
        """
        Метод для отправки уведомления.

        :param message: Текст уведомления.
        :param recipient: Получатель уведомления.
        """
        self.message_service.send_message(message, recipient)
