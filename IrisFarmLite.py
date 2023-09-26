#—————————————————————————————————————————————————————————————————————————————————
#  █▀ █ █ ▀▄▀   █▀▄▀█ █▀█ █▀▄ █ █ █   █▀▀ █▀ Channel: https://t.me/shx_modules
#  ▄█ █▀█ █ █   █ ▀ █ █▄█ █▄▀ █▄█ █▄▄ ██▄ ▄█ Not Licensed
#—————————————————————————————————————————————————————————————————————————————————
# Idea:
# meta developer: @shx_modules
# Thanks: 
#—————————————————————————————————————————————————————————————————————————————————

version = (1, 0, 0)

from .. import utils, loader
import inspect
import asyncio
from asyncio import sleep
import re

class IrisFarmLite(loader.Module):
    '''Модуль для фарма койнов в Iris\nDeveloper: @shx_modules'''
    strings = {
        'name':'IrisFarmLite',
    }

    async def client_ready(self):
        if self.get('status') == None:
            self.set('status', False)
        if self.get('farm') == None:
            self.set('farm', 0)

        if self.get('status') == True:
            await self.farm()

    @loader.command()
    async def farmstart(self, message):
        '''- начать фарм'''
        status = self.get('status')
        error_cmd = f'{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}'
        if status == True:
            await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error</b> | <code>{error_cmd}</code>\nФарм уже запущен.')
            return
        else:
            self.set('status', True)
            await utils.answer(message, f'<emoji document_id=5332533929020761310>✅</emoji> | Фарм запущен.')
            await self.farm()
                
    @loader.command()
    async def farmstats(self, message):
        '''- получить кол-во нафармленных коинов'''
        farm = self.get('farm')
        text = f'<emoji document_id=5188208446461188962>💯</emoji> | Бот нафармил: {farm} коинов.'
        await utils.answer(message, text)
        
    @loader.watcher(chat_id = 5443619563)
    async def watcher(self, message):
        if 'ЗАЧЁТ!' in message.raw_text:
            if self.get('status') == True:
                farm = self.get('farm')
                text = message.raw_text
                match = re.search(r'\+(\d+)', text)
                if match:
                    num = match.group(1)
                    num = int(num)
                    farm += num
                    self.set('farm', farm)
        
    @loader.command()
    async def farmstop(self, message):
        '''- остановить фарм'''
        status = self.get('status')
        error_cmd = f'{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}'
        if status == False:
            await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error</b> | <code>{error_cmd}</code>\nФарм уже остановлен.')
            return
        else:
            self.set('status', False)
            await utils.answer(message, f'<emoji document_id=5332533929020761310>✅</emoji> | Фарм остановлен. <b>Не запускайте фарм снова в течении 4 часов или перезагрузите юзербот.</b>')

    async def farm(self):
        status = self.get('status')
        while True:
            status = self.get('status')
            if status == True:
                await self.client.send_message(5443619563, 'Фарма')
                await asyncio.sleep(14520)
            else:
                break