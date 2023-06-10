#—————————————————————————————————————————————————————————————————————————————————
#  █▀ █ █ ▀▄▀   █▀▄▀█ █▀█ █▀▄ █ █ █   █▀▀ █▀ Chanel: https://shx_modules
#  ▄█ █▀█ █ █   █ ▀ █ █▄█ █▄▀ █▄█ █▄▄ ██▄ ▄█ Not Licensed
#—————————————————————————————————————————————————————————————————————————————————
#  █▀▀ ▀▄▀ █   █ █ █▀ █ █ █ █▀▀   █▀▄▀█ █▀█ █▀▄ █ █ █   █▀▀ █▀
#  ██▄ █ █ █▄▄ █▄█ ▄█ █ ▀▄▀ ██▄   █ ▀ █ █▄█ █▄▀ █▄█ █▄▄ ██▄ ▄█
#—————————————————————————————————————————————————————————————————————————————————
# Idea:
# meta developer: @shx_modules
# Thanks: GPT
#—————————————————————————————————————————————————————————————————————————————————


import asyncio
import re

from telethon.tl.types import Message, ChatAdminRights
from telethon import functions

import logging

from asyncio import sleep

from .. import loader, utils


logger = logging.getLogger(__name__)

@loader.tds
class EVOQ(loader.Module):
    """Модуль для управления аккаунтом t.me/mine_evo_bot\nDeveloper: @Shx_modules"""
    strings = {
        "name": "EVOQ"
    }

    async def client_ready(self):
        self._backup_channel, _ = await utils.asset_channel(
            self._client,
            "EVOQasst",
            "Группа для работы модуля EVOQ от @Shx_modules\nНе добавляйте сюда других людей или ботов!",
            silent=True,
            archive=True,
            _folder="hikka",
        )

        await self.client(functions.channels.InviteToChannelRequest(self._backup_channel, ['@mine_evo_bot']))
        await self.client(functions.channels.EditAdminRequest(
                channel=self._backup_channel,
                user_id="@mine_evo_bot",
                admin_rights=ChatAdminRights(ban_users=True, post_messages=True, edit_messages=True),
                rank="EVOQ",
            )
        )


    

    @loader.command()
    async def evo(self, message: Message):
        """[ Запрос ] - отправить запрос\nПример: .evo проф"""
        args = utils.get_args_raw(message)
        await utils.answer(message, 'Выполняется...')
        async with self._client.conversation(self._backup_channel) as conv:
            await conv.send_message(f'{args}')
            response = await conv.get_response()
        links_regex = re.compile(r'.(https?://\S+).')
        response.text = links_regex.sub('', response.text)
        links = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', response.text)
        for link in links:
            response.text = response.text.replace(link, '')
        await utils.answer(message, response.text)