#To Check whether Your Telegram Bots are Active or Not (pyrogram)
#Idea from github.com/odysseusmax/bug-free-broccoli 🌝
#You need a user session for it

import time
from datetime import datetime
import pytz #Install it using `pip(3) install pytz`
import pyrogram

@pyrogram.Client.on_message(pyrogram.filters.command(["checkstatus"]) # Reply on /checkstatus command
async def check_status(client, message):
    first_msg = "<b>Bots Status...</b>\n\n"
    msg = await message.reply_text(first_msg, parse_mode="html")
    bots = ["@ArchiveHEXbot","@PsychicRobot"] #List of your bots

    for bot in bots:
        checking = f"<b>⭕️ {bot} Status : ♻️</b>\n\n"
        first_msg += checking
        await msg.edit_text(first_msg,parse_mode="html")
        send = await client.send_message(bot, '/start')
        time.sleep(8) #You can change it if you need to increase Checking time.
        bot_msg = await client.get_history(bot, 1)

        if send.message_id == bot_msg[0].message_id:
           nice = f"<b>⭕️ {bot} Status : ❌</b>\n\n"
        else:
           nice = f"<b>⭕️ {bot} Status : ✅</b>\n\n"

        first_msg = first_msg.replace(checking, nice)
        await msg.edit_text(first_msg,parse_mode="html")
        await client.read_history(bot)

    tz = pytz.timezone('Asia/Kolkata')
    time_now  = datetime.utcnow().astimezone(tz=tz).strftime("%I:%M %p - %d %B %Y")
    first_msg += f"<code>[Updated on : {time_now} IST]</code>"
    await msg.edit_text(first_msg,parse_mode="html")
