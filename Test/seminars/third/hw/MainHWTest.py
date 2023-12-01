import unittest

from parameterized import parameterized

from Seminars.seminars.third.hw.MainHW import MainHW


class MainHWtest(unittest.TestCase):
    def setUp(self):
        self.main_hw = MainHW()

    def test_even_number(self):
        self.assertTrue(self.main_hw.even_odd_number(2))

    def test_odd_number(self):
        self.assertFalse(self.main_hw.even_odd_number(1))

    @parameterized.expand([1, 101])
    def test_number_not_in_interval(self, n):
        self.assertFalse(self.main_hw.number_in_interval(n))

    def test_number_in_interval(self):
        self.assertTrue(self.main_hw.number_in_interval(80))
