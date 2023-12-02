from Seminars.seminars.fourth.card.CreditCard import CreditCard


class PaymentForm:
    def __init__(self, credit_card: CreditCard):
        """
        Конструктор класса PaymentForm.

        :param credit_card: Объект класса CreditCard для выполнения платежа.
        """
        self.credit_card = credit_card

    def pay(self, amount: float) -> None:
        """
        Метод для осуществления платежа с использованием кредитной карты.

        :param amount: Сумма платежа.
        """
        self.credit_card.charge(amount)
