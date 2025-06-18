from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class TelegramUser(BaseModel):
    id: int = 0
    first_name: str = "Аноним"
    last_name: Optional[str] = None
    username: Optional[str] = None
    is_bot: bool = False
    language_code: Optional[str] = "ru"

    photo_url: Optional[str] = None
    phone_number: Optional[str] = None
    active_usernames: Optional[list[str]] = None
    emoji_status_custom_emoji_id: Optional[str] = None
    last_online: Optional[datetime] = None
    bio: Optional[str] = None
    has_private_forwards: Optional[bool] = None
    link: Optional[str] = None

    is_premium: bool = False
    added_to_attachment_menu: Optional[bool] = None

    can_join_groups: Optional[bool] = None
    can_read_all_group_messages: Optional[bool] = None
    supports_inline_queries: Optional[bool] = None

    title: Optional[str] = None
    type: Optional[str] = None


def get_user_safe(event) -> TelegramUser:
    user = getattr(event, 'from_user', getattr(event, 'user', None))
    return TelegramUser.model_validate(user) if user else TelegramUser()
