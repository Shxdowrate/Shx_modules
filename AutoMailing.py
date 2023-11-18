#—————————————————————————————————————————————————————————————————————————————————
#  █▀ █ █ ▀▄▀   █▀▄▀█ █▀█ █▀▄ █ █ █   █▀▀ █▀ Channel: https://t.me/mescr_m
#  ▄█ █▀█ █ █   █ ▀ █ █▄█ █▄▀ █▄█ █▄▄ ██▄ ▄█ Not Licensed
#—————————————————————————————————————————————————————————————————————————————————
# Idea:
# meta developer: @mescr_m
# Thanks: 
#—————————————————————————————————————————————————————————————————————————————————
# склемру привет :)

from .. import utils, loader
import asyncio
from asyncio import sleep
import inspect

__version__ = (1, 1, 0)

class AutoMailing(loader.Module):
    '''Модуль для автоматической рассылки постов с одного канала в несколько других.\nDeveloper: @mescr_m'''
    strings = {
        'name':'Auto-mailing',
        'channel_out':'Канал из которого будут перессылаться посты',
        'channel_in':'Каналы, куда будут перессылаться посты'
    }

    async def client_ready(self):
        a = self.get('am_sleep')
        if a is None:
            self.set('am_sleep', 2)
        a = self.get('am_status')
        if a is None:
            self.set('am_status', False)

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "channel_out", 1234,
                lambda: self.strings("channel_out"),
                validator=loader.validators.Integer()
            ),
            loader.ConfigValue(
                "channel_in", [1234],
                lambda: self.strings("channel_in"),
                validator=loader.validators.Series()
            ),
        )

    @loader.watcher()
    async def watcher(self, message):
        am_status = self.get('am_status')
        if am_status == True:
            channel_out = self.config['channel_out']
            channel_in = self.config['channel_in']
            sleep = self.get('am_sleep')
            if message:
                if message.from_id == channel_out:
                    for channel in channel_in:
                        channel = int(channel)
                        if message.media:
                            await self.client.send_message(channel, file=message.media)
                            await asyncio.sleep(sleep)
                            
                        elif message.file:
                            await self.client.send_file(channel, message.file)
                            await asyncio.sleep(sleep)
                            
                        elif message.sticker:
                            await self.client.send_file(channel, message.sticker)
                            await asyncio.sleep(sleep)
                            
                        else:
                            await self.client.send_message(channel, message.text)
                            await asyncio.sleep(sleep)
                            



    
    @loader.command(alias = 'amss')
    async def automailingswitchstatus(self, message):
        ''' - включить/отключить модуль'''
        a = self.get('am_status')
        if a == False:
            self.set('am_status', True)
            await utils.answer(message, f'<emoji document_id=5332533929020761310>✅</emoji> | Auto-mailing включен.')
            return
        elif a == True:
            self.set('am_status', False)
            await utils.answer(message, f'<emoji document_id=5332533929020761310>✅</emoji> | Auto-mailing отключен.')

    @loader.command(alias = 'sams')
    async def setautomailingsleep(self, message):
        '''[ Время в секундах:int ] - установить задержку между отправкой постов в каналы'''
        args = utils.get_args_raw(message)
        error_cmd = f'<code>{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}</code>'
        sleep = self.get('am_sleep')
        if not args:
            await utils.answer(message, f'Ваша текущая задержка: <code>{sleep}</code>')
            return
        else:
            if args.isdigit():
                tsleep = int(args)
                if tsleep >= 2:
                    self.set('am_sleep', tsleep)
                    await utils.answer(message, f'<emoji document_id=5332533929020761310>✅</emoji> | Ваша задержка была изменена на <code>{tsleep}</code>')
                    return
                else:
                    await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error</b> | <code>{error_cmd}</code>\nЗадержка не может быть меньше двух секунд.')
                    return
            else:
                await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error</b> | <code>{error_cmd}</code>\nЗадержкой может стать только целочисленное значение.')
                return
