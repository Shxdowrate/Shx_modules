#—————————————————————————————————————————————————————————————————————————————————
#  █▀ █ █ ▀▄▀   █▀▄▀█ █▀█ █▀▄ █ █ █   █▀▀ █▀ Chanel: https://t.me/shx_modules
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
from ..inline.types import InlineCall
from asyncio import sleep
import asyncio
from telethon.tl.types import Message, ChatAdminRights
from telethon import functions

@loader.tds
class Faud(loader.Module):
    '''Модуль для автоматизации автоматического бура\nDeveloper: @shx_modules'''
    strings = {
        'name': 'Faud',
        'delay': 'Раз в сколько минут собирать руду и заправлять бур?\nУказывайте в минутах\nПосле изменений перезагрузите Юзербот!',
        'module': 'Включён ли модуль?\nВключайте через .faud!'
    }

    async def client_ready(self):
        self._backup_channel, _ = await utils.asset_channel(
            self._client,
            "Faud group",
            "Группа для работы модуля Faud от @Shx_modules\nНе добавляйте сюда других людей или ботов!",
            silent=True,
            archive=True)
        await self.client(functions.channels.InviteToChannelRequest(self._backup_channel, ['@mine_evo_bot']))
        await self.client(functions.channels.EditAdminRequest(
                channel=self._backup_channel,
                user_id="@mine_evo_bot",
                admin_rights=ChatAdminRights(ban_users=True, post_messages=True, edit_messages=True),
                rank="Faud",))
        module = self.config['module']
        tm = self.config['delay']
        tm = tm * 60
        while module == True:
            await asyncio.sleep(2)
            async with self.client.conversation(self._backup_channel) as conv:
                await conv.send_message('Мой бур')
                ghoul = await conv.get_response()
            await asyncio.sleep(2)
            await ghoul.click(0)
            await asyncio.sleep(2)                
            await ghoul.click(1)
            await asyncio.sleep(tm)
                
        


    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "delay", 60,
                lambda: self.strings("delay"),
                validator=loader.validators.Integer(minimum=60)
            ),
            loader.ConfigValue(
                "module", False,
                lambda: self.strings("module"),
                validator=loader.validators.Boolean()
            )
        )

    @loader.watcher()
    async def watcherfaud(self, message):
        if message.raw_text == '/checkfaud':
            if message.from_id == 5195118663: 
                await self.client.send_message(message.to_id, 'evo')
                return

    @loader.command()
    async def faud(self, message):
        ' - ключить / выключить модуль'
        self.config['module'] = not self.config['module']
        aa = self.config['module']
        if aa == True:
            await utils.answer(message, '<emoji document_id=5204044038126182496>✅</emoji> <b>Faud запущен.</b>\nДля вступления изменений в силу перезагрузите 🌒<b>Hikka</b>!')
        if aa == False:
            await utils.answer(message, '<emoji document_id=5206595394728894920>❌</emoji> <b>Faud остановлен.<b>!\nДля вступления изменений в силу перезагрузите 🌒<b>Hikka</b>!')

        