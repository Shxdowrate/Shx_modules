#—————————————————————————————————————————————————————————————————————————————————
#  █▀ █ █ ▀▄▀   █▀▄▀█ █▀█ █▀▄ █ █ █   █▀▀ █▀ Chanel: https://t.me/mescr_m
#  ▄█ █▀█ █ █   █ ▀ █ █▄█ █▄▀ █▄█ █▄▄ ██▄ ▄█ Not Licensed
#—————————————————————————————————————————————————————————————————————————————————
#  █▀▀ ▀▄▀ █   █ █ █▀ █ █ █ █▀▀   █▀▄▀█ █▀█ █▀▄ █ █ █   █▀▀ █▀
#  ██▄ █ █ █▄▄ █▄█ ▄█ █ ▀▄▀ ██▄   █ ▀ █ █▄█ █▄▀ █▄█ █▄▄ ██▄ ▄█
#—————————————————————————————————————————————————————————————————————————————————
# Idea: 
# meta developer: @mescr_m
# Thanks: 
#—————————————————————————————————————————————————————————————————————————————————

from .. import utils, loader
from ..inline.types import InlineCall

__version__ = (1, 0, 0)

class DualMessage(loader.Module):
    '''Модуль для дублирования ваших сообщений\nDeveloper: @mescr_m'''

    strings = {
        'name': 'DualMessage'
    }

    @loader.watcher(no_commands = True, no_media = True, no_inline = True, out = True)
    async def watcher(self, message):
        if message:
            status = self.get('m_status')
            if status == True:
                reply = await message.get_reply_message()
                if reply != None:
                    ds = self.get('d_status')
                    await reply.reply(message.text)
                    if ds == True:
                        await message.delete()
                        return
                else:
                    ds = self.get('d_status')
                    await self.client.send_message(message.chat_id, message.text)
                    if ds == True:
                        await message.delete()

    async def client_ready(self):
        a = self.get('m_status')
        if a == None:
            self.set('m_status', False)
        a = self.get('d_status')
        if a == None:
            self.set('d_status', False)
        a = 1
        


    @loader.command()
    async def dualmsettings(self, message):
        '''- открыть настройки модуля'''
        status = self.get('m_status')
        ds = self.get('d_status')
        if status == True:
            statustxt = 'включен'
            statusbutton = '⚡ Отключить'
        else:
            statustxt = 'отключен'
            statusbutton = '⚡ Включить'
        if ds == True:
            dstxt = 'включено'
            dsbutton = '🗑️ Отключить удаление сообщения'
        else:
            dstxt = 'отключено'
            dsbutton = '🗑️ Включить удаление сообщения'
        await self.inline.form(
            text = f'Настройки модуля <b>DualMessage</b>\n\n<b>⚡ Статус:</b> {statustxt}\n🗑️ <b>Удаление сообщения: </b>{dstxt}',
            message=message,
            reply_markup=[
                [
                    {
                        "text": statusbutton,
                        "callback": self.status,
                    },
                ],
                [
                    
                    {
                        "text": dsbutton,
                        "callback": self.delete_message,
                    },
                ],
            ],
        )


    async def status(self, call: InlineCall):
        status = self.get('m_status')
        ds = self.get('d_status')
        if status == False:
            self.set('m_status', True)
        else:
            self.set('m_status', False)
        status = self.get('m_status')
        ds = self.get('d_status')
        if status == True:
            statustxt = 'включен'
            statusbutton = '⚡ Отключить'
        else:
            statustxt = 'отключен'
            statusbutton = '⚡ Включить'
        if ds == True:
            dstxt = 'включено'
            dsbutton = '🗑️ Отключить удаление сообщения'
        else:
            dstxt = 'отключено'
            dsbutton = '🗑️ Включить удаление сообщения'
        await call.edit(
            text=f'Настройки модуля <b>DualMessage</b>\n\n<b>⚡ Статус:</b> {statustxt}\n🗑️ <b>Удаление сообщения: </b>{dstxt}',
            reply_markup=[
                [
                    {
                        "text": statusbutton,
                        "callback": self.status,
                    },
                ],
                [
                    
                    {
                        "text": dsbutton,
                        "callback": self.delete_message,
                    },
                ],
            ],
        )

    async def delete_message(self, call: InlineCall):
        status = self.get('m_status')
        ds = self.get('d_status')
        if ds == False:
            self.set('d_status', True)
        else:
            self.set('d_status', False)
        status = self.get('m_status')
        ds = self.get('d_status')
        if status == True:
            statustxt = 'включен'
            statusbutton = '⚡ Отключить'
        else:
            statustxt = 'отключен'
            statusbutton = '⚡ Включить'
        if ds == True:
            dstxt = 'включено'
            dsbutton = '🗑️ Отключить удаление сообщения'
        else:
            dstxt = 'отключено'
            dsbutton = '🗑️ Включить удаление сообщения'
        await call.edit(
            text=f'Настройки модуля <b>DualMessage</b>\n\n<b>⚡ Статус:</b> {statustxt}\n🗑️ <b>Удаление сообщения: </b>{dstxt}',
            reply_markup=[
                [
                    {
                        "text": statusbutton,
                        "callback": self.status,
                    },
                ],
                [
                    
                    {
                        "text": dsbutton,
                        "callback": self.delete_message,
                    },
                ],
            ],
        )
