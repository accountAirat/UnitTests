from Seminars.seminars.first.model.Calculator import Calculator
from assertpy import assert_that


def main():
    test_valid_input()
    test_negative_purchase_amount()
    test_negative_discount_amount()
    test_non_float_purchase_amount()
    test_non_integer_discount_amount()
    print('Ok')


def test_valid_input():
    # Проверка корректных входных данных
    instance = Calculator()
    result = instance.calculating_discount(100.0, 10)
    assert_that(result).is_equal_to(90.0)


def test_negative_purchase_amount():
    # Проверка, что функция вызывает исключение при отрицательном purchase_amount
    instance = Calculator()
    assert_that(instance.calculating_discount).raises(ArithmeticError).when_called_with(-50.0, 10)


def test_negative_discount_amount():
    # Проверка, что функция вызывает исключение при отрицательном discount_amount
    instance = Calculator()
    assert_that(instance.calculating_discount).raises(ArithmeticError).when_called_with(100.0, -10)


def test_non_float_purchase_amount():
    # Проверка, что функция вызывает исключение при неверном типе purchase_amount
    instance = Calculator()
    assert_that(instance.calculating_discount).raises(ArithmeticError).when_called_with("100.0", 10)


def test_non_integer_discount_amount():
    # Проверка, что функция вызывает исключение при неверном типе discount_amount
    instance = Calculator()
    assert_that(instance.calculating_discount).raises(ArithmeticError).when_called_with(100.0, 10.5)


if __name__ == '__main__':
    main()
