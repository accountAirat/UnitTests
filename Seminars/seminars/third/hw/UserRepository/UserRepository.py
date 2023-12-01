from typing import List

from Seminars.seminars.third.hw.UserRepository.User import User


class UserRepository:
    def __init__(self):
        self.repository: List[User] = list()

    def add_user(self, user: User):
        if user.authorized:
            self.repository.append(user)

    def log_out_all(self):
        for i in self.repository:
            if not i.admin:
                i.logout()
