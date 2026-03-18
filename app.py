from contextlib import asynccontextmanager

from aiogram.types import Update
from fastapi import FastAPI, HTTPException, Request

from bot.config import settings
from bot.loader import bot, dp


@asynccontextmanager
async def lifespan(app: FastAPI):
    webhook_info = await bot.get_webhook_info()

    if webhook_info.url != settings.webhook_url:
        await bot.set_webhook(
            url=settings.webhook_url,
            secret_token=settings.webhook_secret,
            drop_pending_updates=True,
        )

    yield

    await bot.delete_webhook()
    await bot.session.close()


app = FastAPI(title="FontifyBot", lifespan=lifespan)


@app.get("/")
async def root():
    return {
        "ok": True,
        "message": "FontifyBot is running.",
        "bot_username": settings.bot_username,
        "channel_username": settings.channel_username,
    }


@app.get("/health")
async def health():
    return {"status": "healthy"}


@app.post(settings.webhook_path)
async def telegram_webhook(request: Request):
    secret_token = request.headers.get("X-Telegram-Bot-Api-Secret-Token")
    if secret_token != settings.webhook_secret:
        raise HTTPException(status_code=403, detail="Invalid secret token")

    data = await request.json()
    update = Update.model_validate(data)
    await dp.feed_update(bot, update)

    return {"ok": True}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app:app",
        host=settings.app_host,
        port=settings.app_port,
        reload=True,
    )
