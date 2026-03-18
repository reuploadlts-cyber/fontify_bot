from aiogram import Router, F
from aiogram.types import Message

from bot.config import settings
from bot.services.join_checker import is_user_joined
from bot.services.text_session import set_user_text
from bot.keyboards.reply import main_menu_keyboard

router = Router()


@router.message(F.text)
async def text_handler(message: Message):
    user_id = message.from_user.id
    text = message.text.strip()

    # Ignore commands
    if text.startswith("/"):
        return

    # Check force join again (security)
    is_joined = await is_user_joined(
        bot=message.bot,
        user_id=user_id,
        channel_username=settings.channel_username
    )

    if not is_joined:
        await message.answer(
            "❌ <b>You must join the channel to use this bot.</b>"
        )
        return

    # Save latest text
    set_user_text(user_id, text)

    reply_text = (
        "✨ <b>Text Received!</b>\n\n"
        f"📝 Your Text:\n<code>{text}</code>\n\n"
        "👇 Now choose what you want to do:"
    )

    await message.answer(
        reply_text,
        reply_markup=main_menu_keyboard()
    )
