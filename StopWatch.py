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

from .. import utils, loader
from ..inline.types import InlineCall
import asyncio 
from asyncio import sleep
import inspect

__version__ = (1, 0, 0)

class StopWatch(loader.Module):
    '''Старый добрый секундомер\nDeveloper: @shx_modules'''
    strings = {
        'name': 'StopWatch',
    }

    async def client_ready(self):
        self.set('fact_status', False)
        if self.get('format') == None:
            self.set('format', 'секунды')

    @loader.command(alias = 'swreset')
    async def stopwatchreset(self, message):
        '''- перезагрузка модуля'''
        self.set('fact_status', False)
        self.set('status', False)
        self.set('seconds',0)
        await utils.answer(message, f'<emoji document_id=5332533929020761310>✅</emoji> StopWatch перезагружен.')

    @loader.command(alias = 'sw')
    async def stopwatch(self, message):
        '''- запустить секундомер'''
        error_cmd = f'{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}'
        if message.is_private:
            
            if self.get('fact_status') == False:
                self.set('seconds', 0)
                format = self.get('format')


                await self.inline.form(
                    text = '🚀 <b>StopWatch v1.0</b>\n\n',
                    message=message,
                    reply_markup=[
                        [
                            {
                                "text": "▶ Старт",
                                "callback": self.start,
                            },
                            
                        ],
                        [
                            {
                                "text": "🔄 Сброс",
                                "callback": self.reset,
                            },
                        ],
                        [
                            {
                                'text':f'📄 Формат: {format}',
                                'callback': self.format,
                            }
                        ],
                        [
                            {
                                "text": "🗑️ Остановить секундомер",
                                "callback": self.stop_full,
                            },
                        ],
                            
                    ],
                )
            else:
                await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error</b> | <code>{error_cmd}</code>\nУ вас уже запущен секундомер, остановите его или используйте {utils.escape_html(self.get_prefix())}stopwatchreset')
                return
        else:
            await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error</b> | <code>{error_cmd}</code>\nК сожалению, StopWatch может работать только в личных сообщениях... Возможно, будет исправлено.')
            return
        
    async def start(self, call: InlineCall):
        await call.answer(f'▶ Запущено')
        self.set('status', True)
        self.set('fact_status', True)
        while True:
            await asyncio.sleep(1)
            seconds = self.get('seconds')
            if self.get('status') == True:
                seconds += 1
                self.set('seconds', seconds)
                format = self.get('format')
                if format == 'полный':
                    if seconds < 60:
                        txt = f'🚀 <b>StopWatch v1.0</b>\n\n{seconds}сек.'
                    if seconds >= 60:
                        m = int(seconds/60)
                        s = seconds%60
                        txt = f'🚀 <b>StopWatch v1.0</b>\n\n{m}мин. {s}сек. '
                    if seconds >= 3600:
                        h = int(seconds/3600)
                        m1 = int(seconds - 3600)
                        m = m1/60
                        s = m1%60
                        txt = f'🚀 <b>StopWatch v1.0</b>\n\n{h}ч. {m}мин. {s}сек.'
                else:
                    txt = f'🚀 <b>StopWatch v1.0</b>\n\n{seconds}сек.'
                await call.edit(
                    text=txt,
                    reply_markup=[
                        [
                            {
                                'text': '⏸ Стоп',
                                'callback': self.stop,
                            }
                        ],
                        [
                            {
                                "text": "🔄 Сброс",
                                "callback": self.reset,
                            },
                        ],
                        [
                            {
                                'text':f'📄 Формат: {format}',
                                'callback': self.format,
                            }
                        ],
                        [
                            {
                                "text": "🗑️ Остановить секундомер",
                                "callback": self.stop_full,
                            },
                        ],
                    ]
                )
            else:
                break
                    

    async def stop(self, call: InlineCall):
        await call.answer(f'⏸ Остановлено')
        self.set('status', False)
        seconds = self.get('seconds')
        format = self.get('format')
        if format == 'полный':
            if seconds < 60:
                txt = f'🚀 <b>StopWatch v1.0</b>\n\n{seconds}сек.'
            if seconds >= 60:
                m = int(seconds/60)
                s = seconds%60
                txt = f'🚀 <b>StopWatch v1.0</b>\n\n{m}мин. {s}сек. '
            if seconds >= 3600:
                h = int(seconds/3600)
                m1 = int(seconds - 3600)
                m = m1/60
                s = m1%60
                txt = f'🚀 <b>StopWatch v1.0</b>\n\n{h}ч. {m}мин. {s}сек.'
        else:
            txt = f'🚀 <b>StopWatch v1.0</b>\n\n{seconds}сек.'
        await call.edit(
            text=txt,
            reply_markup=[
                [
                    {
                        "text": "▶ Старт",
                        "callback": self.start,
                    },
                    
                ],
                [
                    {
                        "text": "🔄 Сброс",
                        "callback": self.reset,
                    },
                ],
                [
                    {
                        'text':f'📄 Формат: {format}',
                        'callback': self.format,
                    }
                ],
                [
                    {
                        "text": "🗑️ Остановить секундомер",
                        "callback": self.stop_full,
                    },
                ],
            ]
        )

    async def reset(self, call: InlineCall):
        await call.answer('🔄 Сброшено')
        self.set('seconds', 0)
        self.set('status', False)
        seconds = self.get('seconds')
        format = self.get('format')
        if format == 'полный':
            if seconds < 60:
                txt = f'🚀 <b>StopWatch v1.0</b>\n\n{seconds}сек.'
            if seconds >= 60:
                m = int(seconds/60)
                s = seconds%60
                txt = f'🚀 <b>StopWatch v1.0</b>\n\n{m}мин. {s}сек. '
            if seconds >= 3600:
                h = int(seconds/3600)
                m1 = int(seconds - 3600)
                m = m1/60
                s = m1%60
                txt = f'🚀 <b>StopWatch v1.0</b>\n\n{h}ч. {m}мин. {s}сек.'
        else:
            txt = f'🚀 <b>StopWatch v1.0</b>\n\n{seconds}сек.'
        await call.edit(
            text=txt,
            reply_markup=[
                [
                    {
                        "text": "▶ Старт",
                        "callback": self.start,
                    },
                ],
                [
                    {
                        "text": "🔄 Сброс",
                        "callback": self.reset,
                    },
                ],
                [
                    {
                        'text':f'📄 Формат: {format}',
                        'callback': self.format,
                    }
                ],
                [
                    {
                        "text": "🗑️ Остановить секундомер",
                        "callback": self.stop_full,
                    },
                ],
            ]
        )

    async def stop_full(self, call: InlineCall):
        self.set('seconds', 0)
        self.set('status', False)
        self.set('fact_status', False)
        await call.edit(
            text=f'🗑️ StopWatch остановлен.',
            
        )

    async def format(self, call: InlineCall):
        
        if self.get('format') == 'секунды':
            await call.answer('📄 Новый формат: полный')
            self.set('format', 'полный')
        else:
            self.set('format', 'секунды')
            await call.answer('📄 Новый формат: секунды')
        
