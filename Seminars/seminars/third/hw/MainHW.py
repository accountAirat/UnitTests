"""
HW 3.1. Нужно покрыть тестами метод на 100%
Метод проверяет, является ли целое число записанное в переменную n, чётным (true) либо нечётным (false).

HW 3.2. Нужно написать метод который проверяет, попадает ли переданное число в интервал (25;100) и возвращает true, если попадает и false - если нет,
покрыть тестами метод на 100%
"""


class MainHW:
    def even_odd_number(self, n: int) -> bool:
        if n % 2:
            return False
        return True

    def number_in_interval(self, n) -> bool:
        if 25 < n < 100:
            return True
        return False
