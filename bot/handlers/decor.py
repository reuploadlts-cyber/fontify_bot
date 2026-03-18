from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

from bot.services.text_session import get_user_text
from bot.services.decor_engine import apply_decor, apply_wrapper
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

router = Router()


def decor_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="✨ Sparkle", callback_data="decor_sparkle"),
                InlineKeyboardButton(text="🔥 Fire", callback_data="decor_fire"),
            ],
            [
                InlineKeyboardButton(text="💖 Hearts", callback_data="decor_hearts"),
                InlineKeyboardButton(text="🌟 Stars", callback_data="decor_stars"),
            ],
            [
                InlineKeyboardButton(text="👑 Crown", callback_data="decor_crown"),
                InlineKeyboardButton(text="⚡ Lightning", callback_data="decor_lightning"),
            ],
            [
                InlineKeyboardButton(text="🌸 Flowers", callback_data="decor_flowers"),
            ],
            [
                InlineKeyboardButton(text="🔲 Box", callback_data="wrap_box"),
                InlineKeyboardButton(text="🎀 Fancy", callback_data="wrap_fancy"),
            ],
            [
                InlineKeyboardButton(text="⭐ Star Wrap", callback_data="wrap_stars"),
                InlineKeyboardButton(text="❤️ Heart Wrap", callback_data="wrap_hearts"),
            ],
            [
                InlineKeyboardButton(text="⬅️ Back", callback_data="back_menu"),
            ]
        ]
    )


# Open decor menu
@router.message(F.text == "✨ Decor")
async def open_decor(message: Message):
    await message.answer(
        "✨ <b>Decor Styles</b>\n\nChoose a style:",
        reply_markup=decor_keyboard()
    )


# Apply emoji decor
@router.callback_query(F.data.startswith("decor_"))
async def apply_decor_handler(callback: CallbackQuery):
    user_text = get_user_text(callback.from_user.id)

    if not user_text:
        await callback.answer("❌ No text found", show_alert=True)
        return

    style = callback.data.replace("decor_", "")
    result_text = apply_decor(user_text, style)

    await callback.message.answer(
        f"✨ <b>Decorated Text:</b>\n\n<code>{result_text}</code>"
    )

    await callback.answer()


# Apply wrappers
@router.callback_query(F.data.startswith("wrap_"))
async def apply_wrap_handler(callback: CallbackQuery):
    user_text = get_user_text(callback.from_user.id)

    if not user_text:
        await callback.answer("❌ No text found", show_alert=True)
        return

    style = callback.data.replace("wrap_", "")
    result_text = apply_wrapper(user_text, style)

    await callback.message.answer(
        f"🎀 <b>Styled Text:</b>\n\n<code>{result_text}</code>"
    )

    await callback.answer()
