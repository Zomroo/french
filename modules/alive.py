from pyrogram import Client, filters

app = Client("my_bot")


@app.on_message(filters.command("alive", prefixes="/") & filters.group)
def alive_command_handler(client, message):
    message.reply("I am alive!")


if __name__ == '__main__':
    app.run()
