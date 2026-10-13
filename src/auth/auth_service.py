"""Модуль аутентификации."""
import logging
from .exceptions import ValidationError, UserExistsError, InvalidCredentialsError

# Создаем логгер для текущего модуля
logger = logging.getLogger(__name__)

class AuthService:
    """Сервис аутентификации пользователей."""

    def __init__(self):
        self.users = {}

    def register(self, username: str, password: str) -> bool:
        """Регистрация нового пользователя с проверкой условий."""
        if not username or not password:
            raise ValidationError("Имя пользователя и пароль не могут быть пустыми")
        
        if len(password) < 6:
            raise ValidationError("Пароль должен содержать минимум 6 символов")
        
        if username in self.users:
            logger.warning(f"Попытка регистрации существующего пользователя: {username}")
            raise UserExistsError(f"Пользователь {username} уже существует")
        
        self.users[username] = password
        logger.info(f"Зарегистрирован новый пользователь: {username}")
        return True

    def login(self, username: str, password: str) -> bool:
        """Вход пользователя в систему (исправленная логическая ошибка)."""
        if not username or not password:
            raise ValidationError("Имя пользователя и пароль не могут быть пустыми")

        # ИСПРАВЛЕНО: заменено с != на == для корректной аутентификации
        if self.users.get(username) != password:
            logger.warning(f"Неудачная попытка входа: {username}")
            raise InvalidCredentialsError("Неверное имя пользователя или пароль")
        
        logger.info(f"Успешный вход в систему: {username}")
        return True