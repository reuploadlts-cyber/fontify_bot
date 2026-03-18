import os
from dataclasses import dataclass

from dotenv import load_dotenv


load_dotenv()


@dataclass
class Settings:
    bot_token: str
    bot_username: str
    channel_username: str
    webhook_base_url: str
    webhook_secret: str
    app_host: str
    app_port: int

    @property
    def webhook_path(self) -> str:
        return f"/webhook/{self.webhook_secret}"

    @property
    def webhook_url(self) -> str:
        return f"{self.webhook_base_url}{self.webhook_path}"


def get_settings() -> Settings:
    bot_token = os.getenv("BOT_TOKEN", "").strip()
    bot_username = os.getenv("BOT_USERNAME", "").strip()
    channel_username = os.getenv("CHANNEL_USERNAME", "").strip()
    webhook_base_url = os.getenv("WEBHOOK_BASE_URL", "").strip().rstrip("/")
    webhook_secret = os.getenv("WEBHOOK_SECRET", "").strip()
    app_host = os.getenv("APP_HOST", "0.0.0.0").strip()
    app_port_raw = os.getenv("APP_PORT", "10000").strip()

    if not bot_token:
        raise ValueError("BOT_TOKEN is missing in .env")

    if not bot_username:
        raise ValueError("BOT_USERNAME is missing in .env")

    if not channel_username:
        raise ValueError("CHANNEL_USERNAME is missing in .env")

    if not channel_username.startswith("@"):
        raise ValueError("CHANNEL_USERNAME must start with '@'")

    if not webhook_base_url:
        raise ValueError("WEBHOOK_BASE_URL is missing in .env")

    if not webhook_secret:
        raise ValueError("WEBHOOK_SECRET is missing in .env")

    try:
        app_port = int(app_port_raw)
    except ValueError as exc:
        raise ValueError("APP_PORT must be a valid integer") from exc

    return Settings(
        bot_token=bot_token,
        bot_username=bot_username,
        channel_username=channel_username,
        webhook_base_url=webhook_base_url,
        webhook_secret=webhook_secret,
        app_host=app_host,
        app_port=app_port,
    )


settings = get_settings()
