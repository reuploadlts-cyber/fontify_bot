from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def join_verify_keyboard(channel_username: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="📢 Join Channel",
                    url=f"https://t.me/{channel_username.replace('@', '')}"
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


def fonts_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="𝗕𝗼𝗹𝗱", callback_data="font_bold"),
                InlineKeyboardButton(text="𝘐𝘵𝘢𝘭𝘪𝘤", callback_data="font_italic"),
            ],
            [
                InlineKeyboardButton(text="𝙼𝚘𝚗𝚘", callback_data="font_mono"),
                InlineKeyboardButton(text="𝔻𝕠𝕦𝕓𝕝𝕖", callback_data="font_double"),
            ],
            [
                InlineKeyboardButton(text="Sᴍᴀʟʟ Cᴀᴘs", callback_data="font_smallcaps"),
            ],
            [
                InlineKeyboardButton(text="Fancy 1", callback_data="font_fancy1"),
                InlineKeyboardButton(text="Fancy 2", callback_data="font_fancy2"),
            ],
            [
                InlineKeyboardButton(text="Fancy 3", callback_data="font_fancy3"),
            ],
            [
                InlineKeyboardButton(text="⬅️ Back", callback_data="back_menu"),
            ]
        ]
    )
