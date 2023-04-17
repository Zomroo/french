import config
from pyrogram import Client

app = Client(
    session_name=config.SESSION_NAME,
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    workers=config.WORKERS,
    workdir=config.WORKDIR
)
