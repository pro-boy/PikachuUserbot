import os, telethon, telethon.utils, asyncio, traceback ; from sys import * ;from pikabot import * ;from var import * ; client = bot ; ItzSjDude = client ; from telethon.errors.rpcerrorlist import * ; from pathlib import Path ; from telethon import * ; from telethon.tl.types import *;a = Pk(pid).decode('utf-8');Client = pk+a

if bot is None: 
    from pikabot.login import *
    _Pika_Loop_ = asyncio.get_event_loop()
    _Pika_Loop_.run_until_complete(pika_login("STRING_SESSION"))
else:
    l= Var.CUSTOM_CMD
    from pikabot import LOGS as pikalog
    async def connecting_clients():
        if bot: 
            try: 
                 await bot.start()
                 pikalog.info("_MAINCLIENT_: Connected 🔥")
            except:
                 pikalog.info("**MAINCLIENT**: Session incorrect/expired.Started Login Assistent, Do /start at {}'s PM".format(BF_BOTNAME))
                 await pika_login("STRING_SESSION")
        if bot2:
            try:
                await bot2.start()
                pikalog.info("_MULTICLIENT1_: Connected 🔥")
            except:
                pikalog.info("_MULTICLIENT1_: Session incorrect/expired.Started Login Assistent, Do /start at {}'s PM".format(BF_BOTNAME))
                await pika_login("STR2")
        if bot3:
            try:
                await bot3.start()
                pikalog.info("_MULTICLIENT2_: Connected 🔥")
            except:
                pikalog.info("_MULTICLIENT2_: Session incorrect/expired.Started Login Assistent, Do /start at {}'s PM".format(BF_BOTNAME))
                await pika_login("STR3")
        if bot4:
            try:
                await bot4.start()
                pikalog.info("_MULTICLIENT3_: Connected 🔥")
            except:
                pikalog.info("_MULTICLIENT3_: Session incorrect/expired.Started Login Assistent, Do /start at {}'s PM".format(BF_BOTNAME))
                await pika_login("STR4")

        cli1 = await client.get_messages(Client, None , filter=InputMessagesFilterDocument) ; total = int(cli1.total) ; total_doxx = range(0, total)
        for ixo in total_doxx:
           mxo =cli1[ixo].id ; await client.download_media(await bot.get_messages(Client, ids=mxo), "pikabot/main_plugs")
    bot.loop.run_until_complete(connecting_clients())

    #SocialDistancing


    from pikabot.utils import load_module
    import glob
    path = 'plugins/*.py'
    files = glob.glob(path)
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            load_module(shortname.replace(".py", ""))


    #SocialDistancing


    import pikabot._core


    #SocialDistancing


   
    if len(argv) not in (1, 3, 4):
        bot.disconnect()
    else:
        bot.run_until_disconnected()

