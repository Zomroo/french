from pyrogram import Client
import config
from modules import alive
from modules import rank

if __name__ == '__main__':
    try:
        alive.app.start()
        rank.app.start()
    except KeyboardInterrupt:
        print('\nExiting...')
    finally:
        if alive.app.is_running:
            alive.app.stop()
        if rank.app.is_running:
            rank.app.stop()
