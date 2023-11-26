import math


class Calculator:
    def calculation(self, first_operand: int, second_operand: int, operator: str) -> int:
        result: int
        match operator:
            case '+':
                result = first_operand + second_operand
            case '-':
                result = first_operand - second_operand
            case '*':
                result = first_operand * second_operand
            case '/':
                if second_operand != 0:
                    result = first_operand / second_operand
                else:
                    raise ArithmeticError("Division by zero is not possible")
            case _:
                raise ValueError("Unexpected value operator: " + operator)
        return result

    def square_root_extraction(self, number: float) -> float:
        if number == 0:
            raise ArithmeticError("Невозможно извлечь корень из 0")
        if number < 0:
            raise ArithmeticError("Из отрицательных чисел невозможно извлечь корень")
        return math.sqrt(number)

    def calculating_discount(self, purchase_amount: float, discount_amount: int) -> float:
        if not isinstance(purchase_amount, float | int):
            raise ArithmeticError('purchase_amount должно быть вещественное числом')
        if purchase_amount < 0:
            raise ArithmeticError('purchase_amount не может быть отрицательным числом')

        if not isinstance(discount_amount, int):
            raise ArithmeticError('discount_amount должно быть целым числом')
        if discount_amount < 0:
            raise ArithmeticError('discount_amount не может быть отрицательным числом')

        return purchase_amount - (purchase_amount / 100 * discount_amount)
