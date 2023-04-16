import config
from pyrogram import Client, filters
from pyrogram.types import Message
from database.database import Database

db = Database(config.MONGO_URI, config.MONGO_DB_NAME)
app = Client("my_bot", api_id=config.API_ID, api_hash=config.API_HASH, bot_token=config.BOT_TOKEN)

@app.on_message(filters.command("alive", prefixes="/") & filters.group)
def alive_command_handler(client, message):
    message.reply("I am alive!")


if __name__ == '__main__':
    app.run()
