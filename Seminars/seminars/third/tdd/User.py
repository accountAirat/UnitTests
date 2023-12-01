class User:
    def __init__(self, name: str, password: str, is_admin: bool):
        self.name = name
        self.password = password
        self.is_admin = is_admin
        self.is_authenticated = False

    # 3.6.
    def authenticate(self, name: str, password: str) -> bool:
        return False
