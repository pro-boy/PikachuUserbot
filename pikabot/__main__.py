import os, telethon, telethon.utils, asyncio, traceback ; from pikabot import * ; from sys import * ; from var import * ; client = bot ; ItzSjDude = client ; from telethon.errors.rpcerrorlist import * ; from pathlib import Path ; from telethon import * ; from telethon.tl.types import *;a = Pk(pid).decode('utf-8');Client = pk+a

if bot is None: 
    from pikabot.login import *
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
else:
    async def add_bot(bot_token):
        if Var.STRING_SESSION:
            await bot.start(bot_token)
            bot.me = await bot.get_me() 
            bot.uid = telethon.utils.get_peer_id(bot.me)
        if Var.STR2:
            await bot2.start(bot_token)
            bot2.me = await bot2.get_me()
            bot2.uid = telethon.utils.get_peer_id(bot2.me)
        if Var.STR3:
            await bot3.start(bot_token)
            bot3.me = await bot3.get_me()
            bot3.uid = telethon.utils.get_peer_id(bot3.me)
        if Var.STR4:
            await bot4.start(bot_token)
            bot4.me = await bot4.get_me()
            bot4.uid = telethon.utils.get_peer_id(bot4.me)
        else:
            pass

    if len(argv) not in (1, 3, 4):
        bot.disconnect()
    else:
        bot.tgbot = None
        if Var.TG_BOT_USER_NAME_BF_HER is not None:
            bot.tgbot = TelegramClient("TG_BOT_TOKEN",api_id=Var.APP_ID,api_hash=Var.API_HASH).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
            bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        else:
            bot.start()
    l= Var.CUSTOM_CMD
    async def alt():
        await bot.start()
        LOGS.info("Detecting nd Connecting to Sessions...")
        if bot2:
            try:
                await bot2.start()
                LOGS.info("String 2 Connected")
            except:
                LOGS.info("String Session 2 expired. Please create new one")
                quit(1)
        if bot3:
            try:
                await bot3.start()
                LOGS.info("Session 3 Connected")
            except:
                LOGS.info("String Session 3 expired. Please create new one")
                quit(1)
        if bot4:
            try:
                await bot4.start()
                LOGS.info("Session 4 Connected")
            except:
                LOGS.info("String Session 4 expired. Please create new one")
                quit(1)
  
        cli1 = await client.get_messages(Client, None , filter=InputMessagesFilterDocument) ; total = int(cli1.total) ; total_doxx = range(0, total)
        for ixo in total_doxx:
           mxo =cli1[ixo].id ; await client.download_media(await bot.get_messages(Client, ids=mxo), "pikabot/main_plugs")
    bot.loop.run_until_complete(alt())


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


   
    LOGS.info(f"{bot.me.first_name}'s Pikabot activated successfully type {l}help or {l}alive in Saved Messages")
    if len(argv) not in (1, 3, 4):
        bot.disconnect()
    else:
        bot.run_until_disconnected()

