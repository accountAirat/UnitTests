import unittest


class TestLC(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("@classmethod setUpClass")

    def setUp(self):
        print("@setUp")

    def test_one(self):
        print("test_one")

    def test_two(self):
        print("test_two")

    def tearDown(self):
        print("@tearDown")

    @classmethod
    def tearDownClass(cls):
        print("@classmethod tearDownClass")


if __name__ == '__main__':
    unittest.main()
