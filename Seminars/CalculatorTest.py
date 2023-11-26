import unittest
from Seminars.seminars.first.model.Calculator import Calculator


class CalculatorTest(unittest.TestCase):
    def test_basic_functionality(self):
        self.assertEqual(Calculator.calculation(2, 6, '+'), 8)
        self.assertEqual(Calculator.calculation(2, 2, '-'), 0)
        self.assertEqual(Calculator.calculation(2, 7, '*'), 14)
        self.assertEqual(Calculator.calculation(100, 50, '/'), 2)

    def test_invalid_operator_exception(self):
        with self.assertRaises(ValueError) as context:
            Calculator.calculation(8, 4, '_')
        self.assertEqual(str(context.exception), "Unexpected value operator: _")

    def test_integer_overflow(self):
        result = Calculator.calculation(2_147_483_647, 1, '+')
        self.assertIsInstance(result, int)

    def test_square_root_extraction(self):
        result = Calculator.square_root_extraction(number=169)
        self.assertEqual(result, 13.0)

    def test_square_root_negative_number_exception(self):
        with self.assertRaises(ValueError) as context:
            Calculator.square_root_extraction(number=-1)
        self.assertEqual(str(context.exception), "Cannot calculate square root of a negative number")

    def test_calculating_discount(self):
        result = Calculator.calculating_discount(purchase_amount=100, discount_amount=10)
        self.assertEqual(result, 90.0)


if __name__ == '__main__':
    unittest.main()
