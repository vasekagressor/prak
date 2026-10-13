"""Модуль аутентификации."""
class AuthService:
    def __init__(self):
        self.users = {}

    def register(self, username: str, password: str) -> bool:
        if username in self.users or not password:
            return False
        self.users[username] = password
        return True

    def login(self, username: str, password: str) -> bool:
        return self.users.get(username) == password