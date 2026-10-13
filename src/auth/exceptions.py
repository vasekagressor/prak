"""Пользовательские исключения модуля аутентификации."""

class AuthError(Exception):
    """Базовое исключение модуля аутентификации."""
    pass

class ValidationError(AuthError):
    """Ошибка валидации данных (пустые поля, короткий пароль)."""
    pass

class UserExistsError(AuthError):
    """Ошибка: пользователь уже зарегистрирован в системе."""
    pass

class InvalidCredentialsError(AuthError):
    """Ошибка: неверное имя пользователя или пароль."""
    pass