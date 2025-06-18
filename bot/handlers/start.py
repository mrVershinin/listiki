import logging
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message


logger = logging.getLogger(__name__)

router = Router()


@router.message(CommandStart())
async def cmd_start(msg: Message):
    await msg.reply(
        f"Привет!\nТвой ID {user.id}"
        f"Имя: {msg.from_user.first_name or "Имя скрыто"}\n"
        f"Фамилия: {msg.from_user.last_name or "Фамилия скрыта"}"
    )

    logger.debug(
        f"Пользователь {msg.from_user.username or msg.from_user.id} "
        "запустил бота /start"
    )
