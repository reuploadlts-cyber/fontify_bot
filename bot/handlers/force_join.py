from aiogram import Router, F
from aiogram.types import CallbackQuery

from bot.config import settings
from bot.keyboards.inline import join_verify_keyboard
from bot.services.join_checker import is_user_joined

router = Router()


@router.callback_query(F.data == "verify_join")
async def verify_join_handler(callback: CallbackQuery):
    user_id = callback.from_user.id

    is_joined = await is_user_joined(
        bot=callback.bot,
        user_id=user_id,
        channel_username=settings.channel_username
    )

    if not is_joined:
        text = (
            "❌ <b>You haven't joined the channel yet!</b>\n\n"
            "📢 Please join our channel first, then click <b>Verify</b> again."
        )

        await callback.message.edit_text(
            text=text,
            reply_markup=join_verify_keyboard()
        )

        await callback.answer("Join required ❌", show_alert=True)
        return

    text = (
        "✅ <b>Verification Successful!</b>\n\n"
        "🎉 Now you can use the bot.\n\n"
        "✍️ Send me any text and I will convert it into stylish fonts."
    )

    await callback.message.edit_text(text=text)

    await callback.answer("Verified ✅")
