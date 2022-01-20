from os import path
from pyrogram import Client, filters
from pyrogram import __version__ as pyrover
from pyrogram.types import Message
from time import time
from datetime import datetime
from Yukki import (
    MUSIC_BOT_NAME as bn,
    BOT_USERNAME,
    ASSNAME1,
    ASSID1,
    app,
)

from config import (
    OWNER_NAME as saya,
    BOT_IMG,
    SUPPORT_GROUP,
    SUPPORT_CHANNEL,
    OWNER_USERNAME,
)
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)


@app.on_message(filters.command(["repo", f"repo@{BOT_USERNAME}"]))
async def repo(client, message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await client.send_photo(message.chat.id,
        photo=f"{BOT_IMG}",
        caption=f"""**⚡ Holla {message.from_user.mention()}.**
**Klick button below for {bn} repository 💙**
**Spesial credits for [Team Yukki💚](https://github.com/NotReallyShikhar/YukkiMusicBot)**
**Don't forget to subscribe my [channel 💛]({SUPPORT_CHANNEL})**
**Thanks For Using Me ❤️**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Repo", url=f"https://github.com/fjgaming212/Xbot-Music"
                    ),
                    InlineKeyboardButton(
                        "Deploy", url=f"https://telegram.dog/XTZ_HerokuBot?start=ZmpnYW1pbmcyMTIvWEJvdC1NdXNpYyBtYXN0ZXI"
                    )
                ]
            ]
        )
    )
