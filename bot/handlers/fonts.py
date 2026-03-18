from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

from bot.keyboards.inline import fonts_keyboard
from bot.services.text_session import get_user_text
from bot.services.font_engine import convert_text

router = Router()


# When user clicks "Fonts"
@router.message(F.text == "🎨 Fonts")
async def open_fonts_menu(message: Message):
    text = (
        "🎨 <b>Font Styles</b>\n\n"
        "Select any style below:"
    )

    await message.answer(
        text=text,
        reply_markup=fonts_keyboard()
    )


# Handle font selection
@router.callback_query(F.data.startswith("font_"))
async def apply_font_handler(callback: CallbackQuery):
    user_id = callback.from_user.id

    style = callback.data.replace("font_", "")
    user_text = get_user_text(user_id)

    if not user_text:
        await callback.answer("❌ No text found", show_alert=True)
        return

    styled_text = convert_text(user_text, style)

    result = (
        "✨ <b>Here is your styled text:</b>\n\n"
        f"<code>{styled_text}</code>"
    )

    await callback.message.answer(result)

    await callback.answer()


# Back button
@router.callback_query(F.data == "back_menu")
async def back_menu_handler(callback: CallbackQuery):
    await callback.message.delete()
    await callback.answer()
