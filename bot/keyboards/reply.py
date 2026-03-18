from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_menu_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="🎨 Fonts"),
                KeyboardButton(text="✨ Decor"),
            ],
            [
                KeyboardButton(text="🔥 Combo Styles"),
            ]
        ],
        resize_keyboard=True
    )
