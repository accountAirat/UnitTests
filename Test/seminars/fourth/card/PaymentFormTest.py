import unittest
from unittest.mock import Mock

from Seminars.seminars.fourth.card.PaymentForm import PaymentForm


class PaymentFormTest(unittest.TestCase):

    def test_pay_method(self):
        # Создаем мок-объект для CreditCard
        credit_card_mock = Mock()

        # Задаем поведение мок-объекта: при вызове метода get_card_number() должен возвращаться фиктивный номер карты
        credit_card_mock.get_card_number.return_value = "1234-5678-9012-3456"

        # Создаем объект PaymentForm и передаем ему мок-объект в качестве аргумента
        payment_form = PaymentForm(credit_card_mock)

        # Вызываем метод pay() с некоторой суммой
        payment_form.pay(100.0)

        # Проверяем, что метод charge() был вызван у мок-объекта с ожидаемой суммой
        credit_card_mock.charge.assert_called_once_with(100.0)


if __name__ == '__main__':
    unittest.main()
