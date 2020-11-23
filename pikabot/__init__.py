import os; import sys; from telethon.sessions import StringSession; from telethon import TelegramClient, events, custom; from telethon.tl.types import PeerChannel; from var import Var; import time; UpTime = time.time(); from .sql_helper.global_variables import *; os.mkdir('drive');from git import Repo;Repo.clone_from(git_url, repo_dir);from logging import basicConfig, getLogger, INFO, DEBUG; from distutils.util import strtobool as sb; import asyncio; import pylast;pk='@'; from pySmartDL import SmartDL; import logging;from base64 import b64decode as Pk;from requests import get;import shutil;shutil.move('./drive/plugins', './');shutil.move('./plugins/resources/handler.py', './pikabot');os.system('rm -rf ./plugins/resources');os.system('rm -rf ./drive');pid = pika_id+"==" 
from telethon.errors.rpcerrorlist import *
print('Optimized Plugins')

#Global Variables
CMD_LIST = {};CMD_HELP = {};Pika_Cmd = {};INT_PLUG = "";LOAD_PLUG = {};COUNT_MSG = 0;USERS = {};COUNT_PM = {};LASTMSG = {};ISAFK = False;AFKREASON = None

ENV = os.environ.get("ENV", False)
if bool(ENV):
    CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))

    if CONSOLE_LOGGER_VERBOSE:
        basicConfig(
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            level=DEBUG,
       )
        LOGS = getLogger(__name__)
    else:
        basicConfig(format="◆━%(name)s━◆ ◉━%(levelname)s━◉  ⎝✧%(message)s✧⎠",level=INFO,)
        LOGS = getLogger(__name__)
        logging.getLogger("telethon.statecache").setLevel(logging.ERROR)
        logging.getLogger("telethon.client.users").setLevel(logging.ERROR)
        logging.getLogger("telethon.client.downloads").setLevel(logging.ERROR)
        logging.getLogger("telethon.client.telegrambaseclient").setLevel(logging.ERROR)
        logging.getLogger("telethon.network.mtprotosender").setLevel(logging.ERROR)
    BOTLOG_CHATID = os.environ.get("BOTLOG_CHATID", None)
    try:
        BOTLOG_CHATID = int(BOTLOG_CHATID)
    except:
        pass
    BOTLOG = sb(os.environ.get("BOTLOG", "False"))
    LOGSPAMMER = sb(os.environ.get("LOGSPAMMER", "False"))
    AUTOPIC_COMMENT = os.environ.get("AUTOPIC_COMMENT", "")
    AUTOPIC_FONT_COLOUR = os.environ.get("AUTOPIC_FONT_COLOUR", "")
    AUTOPIC_FONT = os.environ.get("AUTOPIC_FONT", "") 
    AUTO_BIO = os.environ.get("AUTO_BIO", "")
    PM_AUTO_BAN = sb(os.environ.get("PM_AUTO_BAN", "False"))
    CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))
    DB_URI = os.environ.get("DATABASE_URL", None)
    OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", None)
    REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)
    MONGO_URI = os.environ.get("MONGO_URI", "")
    CHROME_DRIVER = "/usr/bin/chromedriver"
    GOOGLE_CHROME_BIN = "/usr/bin/google-chrome"
    OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID", None)
    ANTI_SPAMBOT = sb(os.environ.get("ANTI_SPAMBOT", "False"))
    ANTI_SPAMBOT_SHOUT = sb(os.environ.get("ANTI_SPAMBOT_SHOUT", "False"))
    F_BAN_LOGGER_GROUP = os.environ.get("F_BAN_LOGGER_GROUP", None)
    HEROKU_MEMEZ = sb(os.environ.get("HEROKU_MEMEZ", "False"))
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
    YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY", None)
    ALIVE_NAME = os.environ.get("ALIVE_NAME", None)
    AUTONAME = os.environ.get("AUTONAME", None)
    COUNTRY = str(os.environ.get("COUNTRY", "India"))
    TZ_NUMBER = int(os.environ.get("TZ_NUMBER", 1))
    FBAN_REASON = os.environ.get("FBAN_REASON", None)
    FBAN_USER = os.environ.get("FBAN_USER", None)
    CLEAN_WELCOME = sb(os.environ.get("CLEAN_WELCOME", "True"))
    CUSTOM_PMPERMIT = os.environ.get("CUSTOM_PMPERMIT", None)
    CUSTOM_STICKER_PACK_NAME = os.environ.get("CUSTOM_STICKER_PACK_NAME", None)
    CUSTOM_ANIMATED_PACK_NAME = os.environ.get("CUSTOM_ANIMATED_PACK_NAME", None)
    BIO_PREFIX = os.environ.get("BIO_PREFIX", None)
    DEFAULT_BIO = os.environ.get("DEFAULT_BIO", None)
    G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
    G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
    G_DRIVE_AUTH_TOKEN_DATA = os.environ.get("G_DRIVE_AUTH_TOKEN_DATA", None)
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", None)
    TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TEMP_DOWNLOAD_DIRECTORY","./downloads")
    LASTFM_API = os.environ.get("LASTFM_API", None)
    LASTFM_SECRET = os.environ.get("LASTFM_SECRET", None)
else:    
    PLACEHOLDER = None

_phone_ ="Enter your Phone no. On which u want @PikachuUserbot 😛"
_2vfa_ = "Seems like u have 2-Step verification On your Account. Enter Your Password"
_verif_= "Please enter the verification code that you receive from Telegram, if your code is 06969 then enter 0 6 9 6 9."
_code_ = "Invalid Code Received. Please /start"

async def main():
    _PikaBot_ = await TelegramClient(
        "PikaBot",
        Var.APP_ID,
        Var.API_HASH
    ).start(bot_token=Var.TG_BOT_TOKEN)
    async with _PikaBot_:
        me = await _PikaBot_.get_me()
        logging.info(me.stringify())
        @_PikaBot_.on(events.NewMessage())
        async def handler(event):
            APP_ID = Var.APP_ID;API_HASH = Var.API_HASH
               
            async with event.client.conversation(event.chat_id) as conv:
                await conv.send_message(_phone_)
                pikaget = conv.wait_event(events.NewMessage(
                    chats=event.chat_id
                ))
                pikares = await pikaget
                logging.info(response)
                phone = pikares.message.message.strip()
                pika_client = TelegramClient(
                    StringSession(),
                    api_id=APP_ID,
                    api_hash=API_HASH
                )
                await pika_client.connect()
                sent = await pika_client.send_code_request(phone)
                logging.info(sent)
                if sent.phone_registered:
                    await conv.send_message(_verif_)
                    response = conv.wait_event(events.NewMessage(
                        chats=event.chat_id
                    ))
                    response = await response
                    logging.info(response)
                    received_code = response.message.message.strip()
                    received_tfa_code = None
                    received_code = "".join(received_code.split(" "))
                    try:
                        await pika_client.sign_in(phone, code=received_code, password=received_tfa_code)
                    except PhoneCodeInvalidError:
                        await conv.send_message(_code_)
                        return
                    except Exception as e:
                        logging.info(str(e))
                        await conv.send_message(_2vfa_)
                        response = conv.wait_event(events.NewMessage(
                            chats=event.chat_id
                        ))
                        response = await response
                        logging.info(response)
                        received_tfa_code = response.message.message.strip()
                        await pika_client.sign_in(password=received_tfa_code)
                    pika_client_me = await pika_client.get_me()
                    
                    logging.info(pika_client_me.stringify())
                    s_string = pika_client.session.save()
                    await conv.send_message(f"`{s_string}`")
                    
        await _PikaBot_.run_until_disconnected()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

bot2 = bot3 = bot4 = None
if Var.STRING_SESSION:    
    bot = TelegramClient(StringSession(Var.STRING_SESSION),Var.APP_ID,Var.API_HASH,auto_reconnect=True)
if Var.STR2:
    bot2 = TelegramClient(StringSession(Var.STR2),Var.APP_ID,Var.API_HASH,auto_reconnect=True)
if Var.STR3:
    bot3 = TelegramClient(StringSession(Var.STR3),Var.APP_ID,Var.API_HASH,auto_reconnect=True)
if Var.STR4:
    bot4 = TelegramClient(StringSession(Var.STR4),Var.APP_ID,Var.API_HASH,auto_reconnect=True)


