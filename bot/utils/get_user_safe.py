from pydantic import BaseModel, ConfigDict


class TelegramUser(BaseModel):
    id: int = 0
    first_name: str = "Аноним"
    last_name: str | None = None
    username: str | None = None
    is_bot: bool = False
    
    model_config = ConfigDict(from_attributes=True)


def get_user_safe(event) -> TelegramUser:
    user = (
        getattr(event, 'from_user', None)
        or getattr(event, 'user', None)
    )
    
    if user is None:
        return TelegramUser()
    
    return TelegramUser.model_validate(user, from_attributes=True)
