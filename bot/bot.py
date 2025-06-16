from config import config
from aiogram import Bot, Dispatcher
from bot.handlers import routers


bot = Bot(token=config.BOT_TOKEN.get_secret_value())
dp = Dispatcher()


async def main():
    for router in routers:
        dp.include_router(router)
    await dp.start_polling(bot)
