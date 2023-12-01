import unittest

from Seminars.seminars.third.hw.UserRepository.User import User
from Seminars.seminars.third.hw.UserRepository.UserRepository import UserRepository


class UserRepositoryTest(unittest.TestCase):
    def setUp(self):
        self.repository = UserRepository()
        for i in range(10):
            user = User(login=f"qwerty{i}", password=f"qwerty123{i}", admin=False if i % 3 else True)
            user.authentication(login=f"qwerty{i}", password=f"qwerty123{i}")
            self.repository.add_user(user)

    def test_add_authorized_user(self):
        self.assertEqual(len(self.repository.repository), 10)

    def test_log_out(self):
        self.repository.log_out_all()
        for i in range(10):
            self.assertEqual(self.repository.repository[i].authorized, False if i % 3 else True)
