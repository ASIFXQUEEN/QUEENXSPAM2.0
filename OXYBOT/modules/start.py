from telethon import __version__, events, Button

from config import X1, X2


START_BUTTON = [
    [
        Button.inline("★𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦★", data="help_back")
    ],
    [
        Button.url("★𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗥★", "tg://openmessage?user_id=5099049612"),
        Button.url("★𝗦𝗨𝗣𝗣𝗢𝗥𝗧★", "https://t.me/ARAME9")
    ],
    [
        Button.url("★𝗡𝗔𝗩𝗘𝗘𝗡★", "https://t.me/mr_naveen720")
    ]
]


@X1.on(events.NewMessage(pattern="/start"))
@X2.on(events.NewMessage(pattern="/start"))
async def start(event):
    if event.is_private:
        AltBot = await event.client.get_me()
        bot_name = AltBot.first_name
        bot_id = AltBot.id
        TEXT = f"**ʜᴇʏ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\nɪ ᴀᴍ [{bot_name}](tg://user?id={bot_id})**\n"
        await event.client.send_file(
            event.chat_id,
            "https://envs.sh/wpl.jpg",
            caption=TEXT,
            buttons=START_BUTTON
        )
