from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

from bot.services.text_session import get_user_text
from bot.services.combo_engine import combo_style

router = Router()


def combo_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="🔥 Bold Fire", callback_data="combo_bold_fire"),
                InlineKeyboardButton(text="✨ Italic Sparkle", callback_data="combo_italic_sparkle"),
            ],
            [
                InlineKeyboardButton(text="👑 Double Crown", callback_data="combo_double_crown"),
                InlineKeyboardButton(text="🌸 Fancy Flowers", callback_data="combo_fancy1_flowers"),
            ],
            [
                InlineKeyboardButton(text="🎀 Mono Fancy", callback_data="combo_mono_fancy"),
                InlineKeyboardButton(text="💖 SmallCaps Hearts", callback_data="combo_smallcaps_hearts"),
            ],
            [
                InlineKeyboardButton(text="⭐ Fancy Wrap", callback_data="combo_fancy3_wrap"),
            ],
            [
                InlineKeyboardButton(text="⬅️ Back", callback_data="back_menu"),
            ]
        ]
    )


# Open combo menu
@router.message(F.text == "🔥 Combo Styles")
async def open_combo(message: Message):
    await message.answer(
        "🔥 <b>Combo Styles</b>\n\nSelect a ready-made style:",
        reply_markup=combo_keyboard()
    )


# Handle combo clicks
@router.callback_query(F.data.startswith("combo_"))
async def combo_handler(callback: CallbackQuery):
    user_text = get_user_text(callback.from_user.id)

    if not user_text:
        await callback.answer("❌ No text found", show_alert=True)
        return

    data = callback.data

    # Mapping combos
    combos = {
        "combo_bold_fire": ("bold", "fire", None),
        "combo_italic_sparkle": ("italic", "sparkle", None),
        "combo_double_crown": ("double", "crown", None),
        "combo_fancy1_flowers": ("fancy1", "flowers", None),
        "combo_mono_fancy": ("mono", None, "fancy"),
        "combo_smallcaps_hearts": ("smallcaps", "hearts", None),
        "combo_fancy3_wrap": ("fancy3", None, "fancy"),
    }

    font, decor, wrapper = combos.get(data, (None, None, None))

    if not font:
        await callback.answer("❌ Invalid style", show_alert=True)
        return

    result = combo_style(user_text, font, decor, wrapper)

    await callback.message.answer(
        f"🔥 <b>Combo Styled Text:</b>\n\n<code>{result}</code>"
    )

    await callback.answer()
