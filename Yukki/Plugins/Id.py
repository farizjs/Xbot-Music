# Thanks levina <Veez>
# Fix by Fariz <Xbot>
# If you want to copy this repo also copy the file in line 9
# <Yukki.Utilities.get_file_id>
# Dont remove credits ⚠️
# © Xbot-Music

from pyrogram import Client, filters
from pyrogram.types import Message

from Yukki import BOT_USERNAME, app
from Yukki.Utilities.get_file_id import get_file_id


@app.on_message(filters.command(["id", f"id@{BOT_USERNAME}"]))
async def showid(_, message: Message):
    chat_type = message.chat.type

    if chat_type == "private":
        user_id = message.chat.id
        await message.reply_text(f"<code>{user_id}</code>")

    elif chat_type in ["group", "supergroup"]:
        _id = ""
        _id += "<b>Chat ID</b>: " f"<code>{message.chat.id}</code>\n"
        if message.reply_to_message:
            _id += (
                "<b>Replied User ID</b>: "
                f"<code>{message.reply_to_message.from_user.id}</code>\n"
            )
            file_info = get_file_id(message.reply_to_message)
        else:
            _id += "<b>User ID</b>: " f"<code>{message.from_user.id}</code>\n"
            file_info = get_file_id(message)
        if file_info:
            _id += (
                f"<b>{file_info.message_type}</b>: "
                f"<code>{file_info.file_id}</code>\n"
            )
        await message.reply_text(_id)
