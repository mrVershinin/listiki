from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr


class Settings(BaseSettings):
    BOT_TOKEN: SecretStr
    ID_ADMINS: list[int]
    WEBHOOK_URL: str
    HOST: str
    PORT: int
    SSL_CERTFILE: str
    SSL_KEYFILE: str
    WORKERS: int

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding='utf-8',
        extra='ignore'
    )


config = Settings()  # type: ignore
