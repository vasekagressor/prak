"""Настройка логирования."""
import logging
import os

def setup_logging():
    """Настройка логирования для всего приложения (вывод в консоль и файл)."""
    log_dir = "logs"
    # Автоматически создаем папку logs, если её нет
    os.makedirs(log_dir, exist_ok=True)

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(os.path.join(log_dir, "app.log"), encoding="utf-8"),
            logging.StreamHandler() # Вывод в терминал
        ]
    )