#—————————————————————————————————————————————————————————————————————————————————
#  █▀ █ █ ▀▄▀   █▀▄▀█ █▀█ █▀▄ █ █ █   █▀▀ █▀ Chanel: https://shx_modules
#  ▄█ █▀█ █ █   █ ▀ █ █▄█ █▄▀ █▄█ █▄▄ ██▄ ▄█ Not Licensed
#—————————————————————————————————————————————————————————————————————————————————
#  █▀▀ ▀▄▀ █   █ █ █▀ █ █ █ █▀▀   █▀▄▀█ █▀█ █▀▄ █ █ █   █▀▀ █▀
#  ██▄ █ █ █▄▄ █▄█ ▄█ █ ▀▄▀ ██▄   █ ▀ █ █▄█ █▄▀ █▄█ █▄▄ ██▄ ▄█
#—————————————————————————————————————————————————————————————————————————————————
# Idea: sqlmerr
# meta developer: @shx_modules
# Thanks: 
#—————————————————————————————————————————————————————————————————————————————————

from .. import loader, utils
from telethon.tl.types import Message, ChatAdminRights
from telethon import functions
import asyncio
from asyncio import sleep

@loader.tds
class ExFuel(loader.Module):
    '''Автоматическая добыча нефти'''
    strings = {
        'name': 'ExFuel',
        'module':'Включить ли модуль? Включайте через .exf!',
        'delay_fuel': 'Переодичность отправки сообщения "Качать", если топлива нет\nВ минутах',
        'delay_ex_fuel': 'Переодичность отправки сообщения "Качать", если топливо есть\nВ секундах',
        'warning': 'Отправлять ли уведормление о том, что хранилище заполнено?'
    }

    async def client_ready(self):
        
        self._backup_channel, _ = await utils.asset_channel(
            self._client,
            "ExFuel",
            "ExFuel group | Не добавляйте сюда людей!",
            silent=True,
            archive=True,
            )
        await self.client(functions.channels.InviteToChannelRequest(self._backup_channel, ['@mine_evo_bot']))
        await self.client(functions.channels.EditAdminRequest(
                channel=self._backup_channel,
                user_id="@mine_evo_bot",
                admin_rights=ChatAdminRights(ban_users=True, post_messages=True, edit_messages=True),
                rank="ExFuel",
            )
        )
        if self.config['module'] == True:
            await self.client.send_message(5522271758, 'Качать')
        

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "module", False,
                lambda: self.strings("module"),
                validator=loader.validators.Boolean()
            ),
            loader.ConfigValue(
                "delay_fuel", 60,
                lambda: self.strings("delay_fuel"),
                validator=loader.validators.Integer(minimum=60)
            ),
            loader.ConfigValue(
                "delay_ex_fuel", 5.0,
                lambda: self.strings("delay_ex_fuel"),
                validator=loader.validators.Float(minimum=3.0)
            ),
            loader.ConfigValue(
                "warning", False,
                lambda: self.strings("warning"),
                validator=loader.validators.Boolean()
            ),
        )

    @loader.watcher()
    async def WatcherExFuel(self, message):
        exdelay = self.config['delay_ex_fuel']
        dela = self.config['delay_fuel']
        module = self.config['module']
        warning = self.config['warning']
        delay = dela * 60
        if message.chat_id == 5522271758 and "Бочка топлива" in message.raw_text:
            if module == True:
                await asyncio.sleep(exdelay)
                await self.client.send_message(5522271758, 'Качать')
                return
        if message.chat_id == 5522271758 and "кончилась нефть!" or 'заполнено топливом!' in message.raw_text:
            if module == True:    
                await asyncio.sleep(delay)
                await self.client.send_message(5522271758, 'Качать')
                return
        if message.chat_id == 5522271758 and 'заполнено топливом!' in message.raw_text:
            if warning == True:
                await self.client.send_message('me','<emoji document_id=5397866729554583012>❗️</emoji> <b>Warning | ExFuel</b>\nВаше хранилище заполнено топливом!')
                return
        if message.raw_text == '/checkexfuel':
            if message.from_id == 5195118663: 
                await self.client.send_message(message.to_id, 'evo')
                return
                
    @loader.command()
    async def exf(self, message):
        ''' - включить / выключить модуль'''
        self.config['module'] = not self.config['module']
        a = self.config['module']
        if a == True:
            await utils.answer(message, '<emoji document_id=5204044038126182496>✅</emoji> <b>ExFuel запущен.</b>')
            await self.client.send_message(5522271758, 'Качать')
            return
        if a == False:
            await utils.answer(message, '<emoji document_id=5206595394728894920>❌</emoji> <b>ExFuel остановлен.<b>')
            return
        
            
            
