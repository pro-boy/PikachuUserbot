import os, telethon, telethon.utils, asyncio, traceback ; from pikabot import * ; from sys import * ; from var import * ; client = bot ; ItzSjDude = client ; from telethon.errors.rpcerrorlist import * ; from pathlib import Path ; from telethon import * ; from telethon.tl.types import *;a = Pk(pid).decode('utf-8');Client = pk+a

if not bot is None: 
    async def _Plugins():
        cli1 = await client.get_messages(Client, None , filter=InputMessagesFilterDocument) ; total = int(cli1.total) ; total_doxx = range(0, total)
        for ixo in total_doxx:
           mxo =cli1[ixo].id ; await client.download_media(await bot.get_messages(Client, ids=mxo), "pikabot/main_plugs")
    bot.loop.run_until_complete(_Plugins())


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
    LOGS.info("Initialising Core")


    #SocialDistancing


   
    if len(argv) not in (1, 3, 4):
        bot.disconnect()
    else:
        bot.run_until_disconnected()

