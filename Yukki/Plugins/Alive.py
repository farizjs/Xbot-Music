"""
MIT License
Copyright (C) 2021 KennedyXMusic
This file is part of https://github.com/KennedyProject/KennedyXMusic
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

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
    OWNER_ID,
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


@app.on_message(filters.command(["alive", f"alive@{BOT_USERNAME}"]))
async def alive(client, message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await client.send_photo(message.chat.id,
        photo=f"{BOT_IMG}",
        caption=f"""**⚡ Holla {message.from_user.mention()}, I'm {bn}.**
⚡ **I'm Working Properly**
⚡ **Bot : 6.0 LATEST**
⚡ **My Master : [{saya}](tg://openmessage?user_id={OWNER_ID})**
⚡ **Uptime : `{uptime}`**
⚡ **Pyrogram Version : `{pyrover}`**
⚡ **Please join my group and channel**
**Thanks For Using Me ❤️**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Support", url=f"{SUPPORT_GROUP}"
                    ),
                    InlineKeyboardButton(
                        "Updates", url=f"{SUPPORT_CHANNEL}"
                    )
                ]
            ]
        )
    )
