from telethon import __version__, events, Button

from config import X1, X2


START_BUTTON = [
    [
        Button.inline("★𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦★", data="help_back")
    ],
    [
        Button.url("★𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗥★", "https://t.me/Demonxcoder"),
        Button.url("★𝗦𝗨𝗣𝗣𝗢𝗥𝗧★", "https://t.me/Mrshubh_1227")
    ],
    [
        Button.url("★𝗠𝗢𝗩𝗜𝗘𝗦★", "https://t.me/MoviesWDs_bot")
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
            "https://graph.org/file/db0fbc02a08c2a28349f1-3671ff24b68aa73e82.jpg",
            caption=TEXT,
            buttons=START_BUTTON
        )
