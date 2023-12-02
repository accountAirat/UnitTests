class CreditCard:
    def __init__(self, card_number: str, card_holder: str, expiry_date: str, cvv: str):
        """
        Конструктор класса CreditCard.

        :param card_number: Номер кредитной карты.
        :param card_holder: Держатель карты.
        :param expiry_date: Дата окончания срока действия карты.
        :param cvv: Код CVV карты.
        """
        self.card_number = card_number
        self.card_holder = card_holder
        self.expiry_date = expiry_date
        self.cvv = cvv

    def get_card_number(self) -> str:
        """
        Метод для получения номера кредитной карты.

        :return: Номер кредитной карты.
        """
        return self.card_number

    def get_card_holder(self) -> str:
        """
        Метод для получения держателя карты.

        :return: Держатель карты.
        """
        return self.card_holder

    def get_expiry_date(self) -> str:
        """
        Метод для получения даты окончания срока действия карты.

        :return: Дата окончания срока действия карты.
        """
        return self.expiry_date

    def get_cvv(self) -> str:
        """
        Метод для получения кода CVV карты.

        :return: Код CVV карты.
        """
        return self.cvv

    def charge(self, amount: float) -> None:
        """
        Метод для списания средств с карты.

        :param amount: Сумма списания.
        """
        print(f"Charged amount {amount} from the card: {self.card_number}")
