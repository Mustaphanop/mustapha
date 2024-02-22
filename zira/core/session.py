import sys

from telethon.network.connection.tcpabridged import ConnectionTcpAbridged
from telethon.errors import AccessTokenExpiredError, AccessTokenInvalidError
from ..Config import Config
from .bothseesion import bothseesion
from .client import ZedUserBotClient
from .logger import logging

LOGS = logging.getLogger("𝙎𝙤𝙪𝙧𝙘𝙚 𝙋𝙧𝙤")
__version__ = "2.10.6"

loop = None

if Config.STRING_SESSION:
    session = bothseesion(Config.STRING_SESSION, LOGS)
else:
    session = "mustapha"

try:
    zedub = ZedUserBotClient(
        session=session,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        loop=loop,
        app_version=__version__,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
except Exception as e:
    print(
        f"STRING_SESSION CODE WRONG MAKE A NEW SESSION - {e}\n كود سيشن تيليثـون غير صالح .. قم باستخـراج كود جديد ؟!"
    )
    sys.exit()


try:
    zedub.tgbot = tgbot = ZedUserBotClient(
        session="ZedTgbot",
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        loop=loop,
        app_version=__version__,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    ).start(bot_token=Config.TG_BOT_TOKEN)
except AccessTokenExpiredError:
    LOGS.error("توكن البوت غير صالح قم باستبداله بتوكن جديد من بوت فاذر")
except AccessTokenInvalidError:
    LOGS.error("توكن البوت غير صحيح قم باستبداله بتوكن جديد من بوت فاذر")
