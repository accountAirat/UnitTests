class SomeService:
    """
    3.1. Метод возвращает Fizz для чисел кратных 3, Buzz для кратных 5, и FizzBuzz для кратных 3 и 5 одновременно
    """

    def fizz_buzz(self, i: int) -> str:
        if i % 3 == 0 and i % 5 == 0:
            return "FizzBuzz"
        elif i % 3 == 0:
            return "Fizz"
        elif i % 5 == 0:
            return "Buzz"
        else:
            return str(i)

    """
    3.2. Метод возвращает true для массивов, которые начинаются или заканчиваются 6,
    и false - если 6 нет ни в начале ни в конце массива
    """

    def first_last_6(self, nums: list[int]) -> bool:
        if nums[0] == 6 or nums[-1] == 6:
            return True
        return False

    """
    3.3. Метод подсчета скидки
    """

    def calculating_discount(self, purchase_amount: float, discount_amount: int) -> float:
        return purchase_amount

    """
    3.4. Метод принимает на вход 3 числа (int a, b, c). Нужно вернуть их сумму. Однако, если одно из значений равно 13,
    то оно не учитывается в сумме. Так, например, если b равно 13, то считается сумма только a и c.
    """

    def sum_without_13(self, a: int, b: int, c: int) -> int:
        # Проверка наличия числа 13 и исключение его из суммы
        if a == 13:
            return b + c
        elif b == 13:
            return a + c
        elif c == 13:
            return a + b
        else:
            return a + b + c
