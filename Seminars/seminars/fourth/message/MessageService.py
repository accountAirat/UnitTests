class MessageService:
    def send_message(self, message: str, recipient: str) -> None:
        """
        Метод для отправки сообщения получателю.

        :param message: Текст сообщения.
        :param recipient: Получатель сообщения.
        """
        # Здесь код, который отправляет сообщение получателю.
        print(f"Отправка сообщения \"{message}\" получателю {recipient}")
