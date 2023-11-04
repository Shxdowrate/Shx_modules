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
import asyncio
from asyncio import sleep
import inspect

__version__ = (1, 1, ' Medium Update')

class EvDC(loader.Module):
    '''Модуль для автоматического фарма ежедневных бонусов в боте @good_biznesbot\nDeveloper: @shx_modules'''

    strings = {
        'name':'EvDC',
        'sleep':'Раз в сколько пробовать получать ежедневный бонус?\nУказывайте в часах.',
        'autostart':'Запускать ли модуль автоматически после загрузки юзербота?'
    }

    # Конфиг
    def __init__(self):  
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "sleep", 3,
                lambda: self.strings("sleep"),
                validator=loader.validators.Integer(minimum = 1)
            ),
            loader.ConfigValue(
                "autostart", False,
                lambda: self.strings("autostart"),
                validator=loader.validators.Boolean()
            ),
        )

    async def client_ready(self):
        self.set('status', False) if self.get('status') is None else None # Выставление стандартных значений в базе данных
        self.set('fact_status', False)
        self.set('watcher', False) if self.get('watcher') is None else None
        self.set('stats', 0) if self.get('stats') is None else None
        self.set('group', 0) if self.get('group') is None else None
        if self.config['autostart'] == True: # АвтоЗапуск
            if self.get('status') == True:
                await self.evdcs()
        else:
            self.set('fact_status', False)
            self.set('status', False)

    # Основная функция
    async def evdcs(self): 
        while True:
            if self.get('status') == True:
                self.set('fact_status', True)
                self.set('watcher', True)
                await self.client.send_message(self.get('group'), f'Я')
                await asyncio.sleep(10)
                self.set('watcher', False)
                await asyncio.sleep(self.config['sleep'] * 3600)
            else:
                self.set('fact_status', False)
                break

    # Наблюдатель
    @loader.watcher()
    async def watcher(self, message):
        if self.get('status') == True:
            if self.get('watcher') == True:
                if message.chat_id == self.get('group'):
                    if 'Ранг:' in message.raw_text and  'Уровень:' in message.raw_text: 
                        if 'Ежедневная отметка' in str(message):
                            a = self.get('stats')
                            a += 1
                            self.set('stats', a)
                            await message.click(-1)
                    
    # Включение/выключение модуля
    @loader.command(alias = 'evdc')
    async def everydaycatcher(self, message):
        '''- включить / отключить модуль'''
        if self.get('group') != 0:
            if self.get('status') == True:
                self.set('status', False)
                await utils.answer(message, f'<emoji document_id=5325872701032635449>✅</emoji> <b>EvDC отключен.</b>')
                return
            else:
                self.set('status', True)
                txt = f'<emoji document_id=5325872701032635449>✅</emoji> <b>EvDC включен.</b>'
                if self.get('fact_status') == False:
                    txt += f'\n<emoji document_id=5327790373865530387>🔗</emoji> Цикл перезапущен.'
                await utils.answer(message, txt)
                if self.get('fact_status') == False:
                    await self.evdcs()
        else:
            await utils.answer(message, f'<emoji document_id=5980953710157632545>🚫</emoji> <b>Error</b> // <code>{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}</code>'
                '\n\n<emoji document_id=5818973781707722673>🗣</emoji> <b><u>Суть ошибки:</u></b>\nУ вас не установлена группа для работы модуля EvDC.'
                f'\n\n<emoji document_id=5821302890932736039>🗣</emoji> <b><u>Способы исправления:</u></b>\nУстановите группу для работы модуля EvDC при помощи команды <code>{utils.escape_html(self.get_prefix())}evdcg</code>')
            return
        
    
            
    # Вывод статистики модуля
    @loader.command(alias = 'evdcs')
    async def everydaycatcherstatistics(self, message):
        '''- посмотреть статистику модуля\n"reset" в аргументы, чтобы сбросить'''
        if utils.get_args_raw(message).lower() == 'reset':
            self.set('stats', 0)
            await utils.answer(message, f'<emoji document_id=5307958727448469562>✅</emoji> Статистика EvDC сброшена.')
            return
        stats = str(self.get('stats'))
        if stats[-1] in ['1','5','6','7','8','9','0']:
            txt = f'{stats} раз'
        elif stats[-1] in ['2','3','4']:
            txt = f'{stats} раза'
        if len(stats) > 1:
            if stats[-2] in ['12','13','14']:
                txt = f'{stats} раз'
        await utils.answer(message, f'<emoji document_id=5188208446461188962>💯</emoji> <b>Ежедный бонус был получен:</b> <code>{txt}</code>.')

    # Установка группы для модуля
    @loader.command(alias = 'evdcg')
    async def everydaycatchergroup(self, message):
        '''- установить группу для модуля'''
        if '-' in str(message.chat_id):
            if message.chat_id != self.get('group'):
                self.set('group', message.chat_id)
                await utils.answer(message, f'<emoji document_id=5325872701032635449>✅</emoji> | Группа {message.chat.title} (<code>{message.chat_id}</code>) установлена, как чат для EvDC.')
                return
            else:
                await utils.answer(message, f'<emoji document_id=5980953710157632545>🚫</emoji> <b>Error</b> // <code>{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}</code>'
                    '\n\n<emoji document_id=5818973781707722673>🗣</emoji> <b><u>Суть ошибки:</u></b>\nЭта группа уже установлена, как чат для EvDC.'
                    '\n\n<emoji document_id=5821302890932736039>🗣</emoji> <b><u>Способы исправления:</u></b>\nНапишите команду в другом чате, где есть Бизнесс Бот.')
                return
        else:
            await utils.answer(message, f'<emoji document_id=5980953710157632545>🚫</emoji> <b>Error</b> // <code>{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}</code>'
                '\n\n<emoji document_id=5818973781707722673>🗣</emoji> <b><u>Суть ошибки:</u></b>\nЭтот чат не является группой.'
                '\n\n<emoji document_id=5821302890932736039>🗣</emoji> <b><u>Способы исправления:</u></b>\nНапишите команду в другом чате, где есть Бизнесс Бот.')
            return
