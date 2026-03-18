from aiogram import Bot
from aiogram.exceptions import TelegramBadRequest


async def is_user_joined(bot: Bot, user_id: int, channel_username: str) -> bool:
    try:
        member = await bot.get_chat_member(
            chat_id=channel_username,
            user_id=user_id
        )

        if member.status in ["member", "administrator", "creator"]:
            return True

        return False

    except TelegramBadRequest:
        return False
