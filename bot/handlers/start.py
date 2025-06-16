import logging
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from bot.utils.get_user_safe import get_user_safe


logger = logging.getLogger(__name__)
router = Router()


@router.message(CommandStart())
async def answer_start(msg: Message):
    user = get_user_safe(msg)
    await msg.answer(
        f'Привет, {user.first_name}!'
    )

    logger.debug(
        f"Пользователь {user.username or user.id} "
        "запустил бота /start"
    )
