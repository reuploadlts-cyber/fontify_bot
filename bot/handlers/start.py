from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from bot.keyboards.inline import join_verify_keyboard
from bot.config import settings

router = Router()


@router.message(CommandStart())
async def start_handler(message: Message):
    text = (
        "✨ <b>Welcome to Fontify Bot</b> ✨\n\n"
        "🎨 Convert your text into stylish fonts & cool designs!\n\n"
        "🚀 Before using the bot, please join our channel.\n\n"
        "👇 Click the button below and then press <b>Verify</b>."
    )

    await message.answer(
        text=text,
        reply_markup=join_verify_keyboard(settings.channel_username)
    )
