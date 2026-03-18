from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.config import settings


def join_verify_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="📢 Join Channel",
                    url=f"https://t.me/{settings.channel_username.replace('@', '')}"
                )
            ],
            [
                InlineKeyboardButton(
                    text="✅ Verify Join",
                    callback_data="verify_join"
                )
            ]
        ]
    )
