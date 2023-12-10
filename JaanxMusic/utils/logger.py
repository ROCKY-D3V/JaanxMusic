from pyrogram.enums import ParseMode

from JaanxMusic import app
from JaanxMusic.utils.database import is_on_off
from config import LOGGER_ID


async def play_logs(message, streamtype):
    if await is_on_off(2):
        logger_text = f"""
<b>{app.mention} ᴘʟᴀʏ ʟᴏɢ</b>

<b>¢нαт ι∂ :</b> <code>{message.chat.id}</code>
<b>¢нαт иαмє :</b> {message.chat.title}
<b>¢нαт υѕєяиαмє :</b> @{message.chat.username}

<b>υѕєя ι∂ :</b> <code>{message.from_user.id}</code>
<b>иαмє :</b> {message.from_user.mention}
<b>υѕєяиαмє :</b> @{message.from_user.username}

<b>qυєяу :</b> {message.text.split(None, 1)[1]}
<b>ѕтяєαмтуρє :</b> {streamtype}"""
        if message.chat.id != LOGGER_ID:
            try:
                await app.send_message(
                    chat_id=LOGGER_ID,
                    text=logger_text,
                    parse_mode=ParseMode.HTML,
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
