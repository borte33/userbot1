# Copyright (C) 2020 by UsergeTeam@Github, < https://github.com/UsergeTeam >.
#
# This file is part of < https://github.com/UsergeTeam/Userge > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/uaudith/Userge/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram.errors import ChatSendMediaForbidden
from pyrogram.errors.exceptions import FileIdInvalid, FileReferenceEmpty
from pyrogram.errors.exceptions.bad_request_400 import BadRequest, ChannelInvalid, MediaEmpty


@Client.on_message(filters.command(['yasiyorum'], ['!','.','/']) & filters.me)
async def alive(message: Message):
    await message.delete()
    output = f"""
**Yaşıyorum usta..**

**💥 version** : `{get_version()}`
**__Python__**: `{versions.__python_version__}`
**__Pyrogram__**: `{versions.__pyro_version__}`"""
    if Config.HEROKU_APP:
        output += f"\n• **dyno-saver**: `{_parse_arg(Config.RUN_DYNO_SAVER)}`"
    output += f"""

   
"""
    try:
        await _send_alive(message, output)
    except (FileIdInvalid, FileReferenceEmpty, BadRequest):
        await _refresh_id()
        await _send_alive(message, output)


def _parse_arg(arg: bool) -> str:
    return "enabled" if arg else "disabled"


async def _send_alive(message: Message, text: str) -> None:
    except (MediaEmpty, ChatSendMediaForbidden):
        await message.client.send_message(chat_id=message.chat.id,
                                          text=text,
                                          disable_web_page_preview=True)


