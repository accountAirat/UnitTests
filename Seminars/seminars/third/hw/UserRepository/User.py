class User:
    def __init__(self, login="qwerty", password="qwerty123", admin=False):
        self._login = login
        self._password = password
        self._authorized = False
        self._admin = admin

    def authentication(self, login, password):
        if login == self._login and password == self._password:
            self._authorized = True
            return True
        return False

    @property
    def authorized(self):
        return self._authorized

    @authorized.setter
    def authorized(self, *args):
        raise AttributeError()

    @property
    def admin(self):
        return self._admin

    @admin.setter
    def admin(self, *args):
        raise AttributeError()

    def logout(self):
        self._authorized = False
