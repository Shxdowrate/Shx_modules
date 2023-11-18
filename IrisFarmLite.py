#—————————————————————————————————————————————————————————————————————————————————
#  █▀ █ █ ▀▄▀   █▀▄▀█ █▀█ █▀▄ █ █ █   █▀▀ █▀ Channel: https://t.me/mescr_m
#  ▄█ █▀█ █ █   █ ▀ █ █▄█ █▄▀ █▄█ █▄▄ ██▄ ▄█ Not Licensed
#—————————————————————————————————————————————————————————————————————————————————
# Idea:
# meta developer: @mescr_m
# Thanks: 
#—————————————————————————————————————————————————————————————————————————————————

__version__  = (1, 1, 0)

from .. import utils, loader
import inspect
import asyncio
from asyncio import sleep
import re
from ..inline.types import InlineCall

class IrisFarmLite(loader.Module):
    '''Модуль для фарма койнов в Iris\nDeveloper: @mescr_m'''
    strings = {
        'name':'IrisFarmLite',
    }

    async def client_ready(self):
        if self.get('status') == None:
            self.set('status', False)
        if self.get('farm') == None:
            self.set('farm', 0)
        if self.get('sd_status') == None:
            self.set('sd_status', False)
        if self.get('ss') == None:
            self.set('ss', False)
        

        if self.get('status') == True:
            await self.farm()

    @loader.command()
    async def farmstart(self, message):
        '''- начать фарм'''
        status = self.get('status')
        error_cmd = f'{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}'
        sd_status = self.get('sd_status')
        if status == True:
            await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error</b> | <code>{error_cmd}</code>\nФарм уже запущен.')
            return
        else:
            if sd_status == False:
                self.set('status', True)
                await utils.answer(message, f'<emoji document_id=5332533929020761310>✅</emoji> | Фарм запущен.')
                await self.farm()
                return
            else:
                await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error</b> | <code>{error_cmd}</code>\nДождитесь завершения цикла, а после запустите фарм снова.')
                return
                
    @loader.command()
    async def farmstats(self, message):
        '''- получить кол-во нафармленных коинов'''
        farm = self.get('farm')
        txt = f'<emoji document_id=5188208446461188962>💯</emoji> | Бот нафармил: {farm} коинов.'
        await self.inline.form(
            text = txt,
            message=message,
            reply_markup=[
                    [
                        {
                            "text": "💼 Мешок",
                            "callback": self.bag,
                        },
                    ],
                    [
                        {
                            "text": "🗑️ Сброс статистики",
                            "callback": self.reset,
                        },
                    ],
                    
            ],
        )

    async def bag(self, call: InlineCall):
        farm = self.get('farm')
        await self.client.send_message(5443619563, 'Мешок')
        self.set('ss', True)
        txt = f'<emoji document_id=5188208446461188962>💯</emoji> | Бот нафармил: {farm} коинов.\n⏳ | Подождите...'
        await call.edit(
            text=txt,
        )
        await asyncio.sleep(5)
        bag = self.get('bag')
        if bag is None:
            bag = '[ error ] No bag.'
        txt = f'<emoji document_id=5188208446461188962>💯</emoji> | Бот нафармил: {farm} коинов.\n💼 Мешок:\n\n{bag}'
        await call.edit(
            text=txt
        )

    async def reset(self, call: InlineCall):
        await call.edit(
            text='<b>Вы уверены, что хотите сбросить статистику IrisFarmLite?</b>',
            reply_markup=[
                [
                    {
                        "text": "✔️ Да",
                        "callback": self.reset_yes,
                    },
                    {
                        "text": "❌ Нет",
                        "callback": self.reset_no,
                    },
                ]
            ]
        )
    
    async def reset_yes(self, call: InlineCall):
        self.set('farm', 0)
        await call.edit(
            text='🗑️ | <b>Статистика IrisFarmLite сброшена.</b>',
        )

    async def reset_no(self, call: InlineCall):
        
        await call.edit(
            text='🗑️ | <b>Действие отменено.</b>',
        )

        
        
    
        
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

        if '💰 В мешке' in message.raw_text:
            if self.get('ss') == True:
                bag = message.raw_text
                self.set('bag', bag)
                self.set('ss', False)
            
        
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
            await utils.answer(message, f'<emoji document_id=5332533929020761310>✅</emoji> | Фарм остановлен.')

    async def farm(self):
        status = self.get('status')
        while True:
            self.set('sd_status', True)
            status = self.get('status')
            if status == True:
                await self.client.send_message(5443619563, 'Фарма')
                await asyncio.sleep(14520)
            else:
                self.set('sd_status', False)
                break
                
