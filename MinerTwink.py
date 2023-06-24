#—————————————————————————————————————————————————————————————————————————————————
#  █▀ █ █ ▀▄▀   █▀▄▀█ █▀█ █▀▄ █ █ █   █▀▀ █▀ Chanel: https://shx_modules
#  ▄█ █▀█ █ █   █ ▀ █ █▄█ █▄▀ █▄█ █▄▄ ██▄ ▄█ Not Licensed
#—————————————————————————————————————————————————————————————————————————————————
#  █▀▀ ▀▄▀ █   █ █ █▀ █ █ █ █▀▀   █▀▄▀█ █▀█ █▀▄ █ █ █   █▀▀ █▀
#  ██▄ █ █ █▄▄ █▄█ ▄█ █ ▀▄▀ ██▄   █ ▀ █ █▄█ █▄▀ █▄█ █▄▄ ██▄ ▄█
#—————————————————————————————————————————————————————————————————————————————————
# Idea: 
# meta developer: @shx_modules
# Thanks: 
#—————————————————————————————————————————————————————————————————————————————————

from .. import loader, utils
import asyncio
from asyncio import sleep

from telethon.tl.types import Message


@loader.tds
class MinerTwink(loader.Module):
    '''Модуль для автоматической передачи найденных кейсов с твинка на основной аккаунт\nDeveloper: @shx_modules'''
    strings = {
        'name': 'MinerTwink 1.0',
        'NickName':'Ник в боте, на который надо передавать найденные кейсы',
        'OnOff':'Включить выключить модуль'
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "NickName", '#',
                lambda: self.strings("NickName"),
                validator=loader.validators.String()
            ),
            loader.ConfigValue(
                "OnOff", False,
                lambda: self.strings("OnOff"),
                validator=loader.validators.Boolean()
            ),
        )


    
   
    async def watcher(self, message):
        NickName = self.config['NickName']
        ooo = self.config['OnOff']
        if ooo == True:
            if message.chat_id == 5522271758 and "✉️ Ты нашел(ла) конверт." in message.raw_text:
                await asyncio.sleep(2)
                await self.client.send_message('@mine_evo_bot', f'Дать {NickName} кт 1')
                return
            elif message.chat_id == 5522271758 and "🧧 Ты нашел(ла) редкий конверт." in message.raw_text:
                await asyncio.sleep(2)
                await self.client.send_message('@mine_evo_bot', f'Дать {NickName} ркт 1')
                return
            elif message.chat_id == 5522271758 and "📦 Ты нашел(ла) Кейс!" in message.raw_text:
                await asyncio.sleep(2)
                await self.client.send_message('@mine_evo_bot', f'Дать {NickName} к 1')
                return
            elif message.chat_id == 5522271758 and "🗳 Ты нашел(ла) Редкий Кейс!" in message.raw_text:
                await asyncio.sleep(2)
                await self.client.send_message('@mine_evo_bot', f'Дать {NickName} рк 1')
                return
            elif message.chat_id == 5522271758 and "🕋 Ты нашел(ла) Мифический Кейс!" in message.raw_text:
                await asyncio.sleep(2)
                await self.client.send_message('@mine_evo_bot', f'Дать {NickName} миф 1')
                return
            elif message.chat_id == 5522271758 and "💎 Ты нашел(ла) Кристальный Кейс!" in message.raw_text:
                await asyncio.sleep(2)
                await self.client.send_message('@mine_evo_bot', f'Дать {NickName} кр 1')
                return
            elif message.chat_id == 5522271758 and "💫" in message.raw_text:
                await asyncio.sleep(2)
                await self.client.send_message('@mine_evo_bot', f'Дать {NickName} зв 1')
                return








    @loader.command()
    async def mts(self, message):
        ''' - Выключить/выключить'''
        self.config['OnOff'] = not self.config['OnOff']
        onoff = self.config['OnOff']
        if onoff == True:
            await utils.answer(message, '<emoji document_id=5204044038126182496>✅</emoji> MinerTwink запущен!')
            return
        if onoff == False:
            await utils.answer(message, '<emoji document_id=5206595394728894920>❌</emoji> MinerTwink остановлен!')
            return

    @loader.command()
    async def setnick(self, message):
        '''[ НикНейм ] - установить никнейм, кому передавать кейсы'''
        args = utils.get_args_raw(message)
        self.config['NickName'] = args
        await utils.answer(message, '<emoji document_id=5204044038126182496>✅</emoji> Ник установлен.\nТеперь буду передавать кейсы на ник <code>args</code>')