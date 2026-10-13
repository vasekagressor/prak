"""Главный модуль приложения."""
import logging
from src.logger_config import setup_logging
from src.auth.auth_service import AuthService
from src.auth.exceptions import AuthError

# Инициализируем конфигурацию логов
setup_logging()

def main():
    auth = AuthService()
    try:
        # Имитируем последовательность действий
        auth.register("ivan", "123456")
        auth.login("ivan", "123456")
        auth.login("ivan", "wrong_pass") # Это вызовет исключение
    except AuthError as e:
        logging.error(f"Контролируемая ошибка аутентификации: {e}")
    except Exception as e:
        logging.critical(f"Непредвиденная критическая ошибка системы: {e}")
    finally:
        logging.info("Завершение работы приложения")

if __name__ == "__main__":
    main()