from typing import List


class UserRepository:
    def __init__(self):
        # Тут можно хранить аутентифицированных пользователей
        self.data = []

    def add_user(self, user):
        # ..
        pass

    def find_by_name(self, username: str) -> bool:
        for user in self.data:
            if user.name == username:
                return True
        return False
