from pyrogram import Client
import config
from modules import rank
from modules.rank import handle_me_command

if __name__ == '__main__':
    try:
        rank.app.add_handler(handle_me_command)
        rank.app.run()

    except ApiIdInvalid:
        print("Invalid API ID. Please set the correct API ID in the config.py file.")
    except ApiHashInvalid:
        print("Invalid API hash. Please set the correct API hash in the config.py file.")
