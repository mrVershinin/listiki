from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Union
from aiogram.types import (
    Message, InlineQuery, CallbackQuery, ChatMemberUpdated,
    PreCheckoutQuery, ShippingQuery, PollAnswer
)


class TelegramUser(BaseModel):
    # Основные поля
    id: int = 0
    first_name: str = "Аноним"
    last_name: Optional[str] = None
    username: Optional[str] = None
    is_bot: bool = False
    language_code: Optional[str] = "ru"

    # Взаимодействие с ботом
    registered_at: datetime
    last_seen: datetime
    current_state: str = "start"
    locale: str = "ru"
    is_blocked: bool = False

    # Премиум/функциональные поля
    is_premium: bool = False

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"


def get_user_safe(
    event: Union[
        Message, InlineQuery, CallbackQuery,
        ChatMemberUpdated, PreCheckoutQuery,
        ShippingQuery, PollAnswer
    ]
) -> TelegramUser:
    user = (
        event.user if isinstance(event, PollAnswer)
        else event.from_user if hasattr(event, 'from_user')
        else None
    )
    return TelegramUser.model_validate(user.__dict__ if user else {})
