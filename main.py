from pyrogram import Client
import config
from modules import rank

if __name__ == '__main__':
    app = Client("my_bot", api_id=config.API_ID, api_hash=config.API_HASH, bot_token=config.BOT_TOKEN)

    # Add message handlers from the rank module
    app.add_handler(rank.handle_message)
    app.add_handler(rank.handle_me_command)

    try:
        app.run()
    except ApiIdInvalid:
        print("Invalid API ID. Please set the correct API ID in the config.py file.")
    except ApiHashInvalid:
        print("Invalid API hash. Please set the correct API hash in the config.py file.")
