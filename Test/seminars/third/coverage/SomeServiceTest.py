import unittest
from parameterized import parameterized

from Seminars.seminars.third.coverage.SomeService import SomeService


class SomeServiceTest(unittest.TestCase):
    # 3.1.
    def setUp(self):
        self.some_service = SomeService()

    def test_multiple_three_returns_fizz(self):
        self.assertEqual(self.some_service.fizz_buzz(3), 'Fizz')

    def test_multiple_five_returns_fizz(self):
        self.assertEqual(self.some_service.fizz_buzz(5), 'Buzz')

    def test_multiple_fifteen_returns_fizz(self):
        self.assertEqual(self.some_service.fizz_buzz(15), 'FizzBuzz')

    def test_multiple_eight_returns_fizz(self):
        self.assertEqual(self.some_service.fizz_buzz(8), '8')

    def test_list_first_6(self):
        self.assertTrue(self.some_service.first_last_6([6, 5, 3]))

    def test_list_last_6(self):
        self.assertTrue(self.some_service.first_last_6([4, 5, 6]))

    def test_list_not_first_or_last_6(self):
        self.assertFalse(self.some_service.first_last_6([7, 5, 3]))
