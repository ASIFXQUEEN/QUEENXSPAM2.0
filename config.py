import logging

from telethon import TelegramClient

from os import getenv
from OXYBOT.data import OXYGEN


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)


# VALUES REQUIRED FOR XBOTS
API_ID = 27918253
API_HASH = "52464e9f32a2c373b7cac0c821edf3d5"
CMD_HNDLR = getenv("CMD_HNDLR", default=".")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)

BOT_TOKEN = getenv("BOT_TOKEN", default=None)
BOT_TOKEN2 = getenv("BOT_TOKEN2", default=None)


SUDO_USERS = list(map(lambda x: int(x), getenv("SUDO_USERS", default="6132821365").split()))
for x in OXYGEN:
    SUDO_USERS.append(x)
OWNER_ID = int(getenv("OWNER_ID", default="7093899037"))
SUDO_USERS.append(OWNER_ID)


# ------------- CLIENTS -------------

X1 = TelegramClient('X1', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
X2 = TelegramClient('X2', API_ID, API_HASH).start(bot_token=BOT_TOKEN2)

