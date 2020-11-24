import asyncio,logging,os,sys,heroku3
from telethon import TelegramClient, events, custom
from telethon.sessions import StringSession
from telethon.errors.rpcerrorlist import *
from pikabot import LOGS as logging
from var import Var 

Heroku = heroku3.from_key(Var.HEROKU_API_KEY)
app = Heroku.app(Var.HEROKU_APP_NAME)


def get_client(_Pika_):
    global a
    if _Pika_=="STRING_SESSION":
       a ="**MAINCLIENT**"
    elif _Pika_=="STR2":
      a ="**MULTICLIENT1**"
    elif _Pika_=="STR3":
      a ="**MULTICLIENT2**"
    elif _Pika_=="STR4":
      a ="**MULTICLIENT3**"
    return a
      
_phone_ ="**Login Assistent** For {}\n\nEnter your Phone no. On which u want @PikachuUserbot 😛\nIf Indian No. **+91xxxxxxxxxx** else use **Country Code**"
_2vfa_ = "**Login Assistent** For {}\n\nSeems like u have **2-Step verification** On your Account. Enter Your Password"
_verif_= "**Login Assistent** For {}\n\nPlease enter the verification code that you receive from Telegram\n**if your code is** 06969 **then enter** 0 6 9 6 9."
_code_ = "**Login Assistent** For {}\n\n**Invalid Code Received**. Please /start"
_logged_ = "Login Assistent** For {}\n\n **LOGGED IN** Successfully wait for 2Mins n then Do .pika**"
async def pika_login(_PiKa_):
    _PikaBot_ = await TelegramClient(
        "PikaBot",
        Var.APP_ID,
        Var.API_HASH
    ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
    _cn_=get_client_(_PiKa_)
    async with _PikaBot_:
        me = await _PikaBot_.get_me()
        logging.info(me.first_name)
        @_PikaBot_.on(events.NewMessage())
        async def handler(event):
            APP_ID = Var.APP_ID;API_HASH = Var.API_HASH
            Config=app.config()  
            async with event.client.conversation(event.chat_id) as conv:
                await conv.send_message(_phone_.format(_cn_))
                pikaget = conv.wait_event(events.NewMessage(
                    chats=event.chat_id
                ))
                pikares = await pikaget
                logging.info(pikares)
                phone = pikares.message.message.strip()
                pika_client = TelegramClient(
                    StringSession(),
                    api_id=APP_ID,
                    api_hash=API_HASH
                )
                await pika_client.connect()
                sent = await pika_client.send_code_request(phone)
                logging.info(sent)
                await conv.send_message(_verif_.format(_cn_))
                response = conv.wait_event(events.NewMessage(
                    chats=event.chat_id
                ))
                response = await response
                logging.info(response)
                r_code = response.message.message.strip()
                _2vfa_code_ = None
                r_code = "".join(r_code.split(" "))
                try:
                    await pika_client.sign_in(phone, code=r_code, password=_2vfa_code_)
                except PhoneCodeInvalidError:
                    await conv.send_message(_code_.format(_cn_))
                    return
                except Exception as e:
                    logging.info(str(e))
                    await conv.send_message(_2vfa_.format(_cn_))
                    response = conv.wait_event(events.NewMessage(
                        chats=event.chat_id
                    ))
                    response = await response
                    logging.info(response)
                    _2vfa_code_ = response.message.message.strip()
                    await pika_client.sign_in(password=_2vfa_code_)
                    pika_client_me = await pika_client.get_me()
                    logging.info(pika_client_me.stringify())
                    s_string = pika_client.session.save()
                    await conv.send_message(_logged_.format(_cn_))
                    Config[_PiKa_] = s_string
        await _PikaBot_.run_until_disconnected()
