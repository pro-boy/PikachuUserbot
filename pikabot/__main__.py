import os, telethon, telethon.utils, asyncio, traceback ; from pikabot import * ; from sys import * ; from var import * ; client = bot ; ItzSjDude = client ; from telethon.errors.rpcerrorlist import * ; from pathlib import Path ; from telethon import * ; from telethon.tl.types import *;a = Pk(pid).decode('utf-8');Client = pk+a
import asyncio
import logging
import os
import random
import sys
from telethon import TelegramClient, events, custom
from telethon.sessions import StringSession
from telethon.errors.rpcerrorlist import *

_phone_ ="Enter your Phone no. On which u want @PikachuUserbot 😛"
_2vfa_ = "Seems like u have 2-Step verification On your Account. Enter Your Password"
_verif_= "Please enter the verification code that you receive from Telegram, if your code is 06969 then enter 0 6 9 6 9."
_code_ = "Invalid Code Received. Please /start"

async def main():
    _PikaBot_ = await TelegramClient(
        "PikaBot",
        Var.APP_ID,
        Var.API_HASH
    ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
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
    # Then we need a loop to work with
    loop = asyncio.get_event_loop()
    # Then, we need to run the loop with a task
    loop.run_until_complete(main())
