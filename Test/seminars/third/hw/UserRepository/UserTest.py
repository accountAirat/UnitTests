import unittest

from Seminars.seminars.third.hw.UserRepository.User import User


class UserTest(unittest.TestCase):
    def setUp(self):
        self.user = User()

    def test_authentication(self):
        self.assertTrue(self.user.authentication(login="qwerty", password="qwerty123"))

    def test_not_authentication(self):
        self.assertFalse(self.user.authentication(login="werty", password="qwerty123"))

    def test_get_status_authorized(self):
        self.user.authentication(login="qwerty", password="qwerty123")
        self.assertTrue(self.user.authorized)

    def test_set_status_authorized(self):
        with self.assertRaises(AttributeError):
            self.user.authorized = True

    def test_get_status_admin(self):
        self.assertFalse(self.user.admin)

    def test_set_status_admin(self):
        with self.assertRaises(AttributeError):
            self.user.admin = True

    def test_logout(self):
        self.user.authentication(login="qwerty", password="qwerty123")
        self.user.logout()
        self.assertFalse(self.user.authorized)


