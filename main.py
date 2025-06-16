import logging
import asyncio

from logger import setup_logging
from bot.bot import main

if __name__ == "__main__":
    setup_logging(level=logging.DEBUG)

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Бот остановлен")
    except Exception as e:
        logging.exception(f"Критическая ошибка: {e}")
