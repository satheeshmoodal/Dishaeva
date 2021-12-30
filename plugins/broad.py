from pyrogram import Client, filters

from bot.screenshotbot import ScreenShotBot


@Client.on_message(
    filters.private
    & filters.command("broad")
    & filters.reply
)
async def broadcast_(c, m):
    await c.start_broadcast(
        broadcast_message=m.reply_to_message, admin_id=m.from_user.id
    )
