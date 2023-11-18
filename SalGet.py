#—————————————————————————————————————————————————————————————————————————————————
#  █▀ █ █ ▀▄▀   █▀▄▀█ █▀█ █▀▄ █ █ █   █▀▀ █▀ Chanel: https://t.me/mescr_m
#  ▄█ █▀█ █ █   █ ▀ █ █▄█ █▄▀ █▄█ █▄▄ ██▄ ▄█ Not Licensed
#—————————————————————————————————————————————————————————————————————————————————
# Idea:
# meta developer: @mescr_m
# Thanks: 
#—————————————————————————————————————————————————————————————————————————————————

from .. import utils, loader
import asyncio
import inspect

__version__ = (1, 0, 0)

class SalGet(loader.Module):
    '''Модуля для автоматической выплаты зарплаты работникам ваших бизнессов в боте @good_biznesbot\nDeveloper: @mescr_m'''

    strings = {
        'name': 'SalGet',
        'sleep': 'Раз в сколько минут выдавать зарплату?',
        'autostart': 'Запускать ли модуль автоматически после загрузки юзербота?',
        'resget': 'Собирать ли ресурсы с бизнессов?',
        # Строки для вотчера
        'str_c_res': '\n<emoji document_id=5818711397860642669>✅</emoji> Ресурсы собраны.',
        'str_d_res': '\n<emoji document_id=5818665600624365278>❌</emoji> Собирать нечего.',
        'str_c_sal': '\n<emoji document_id=5818711397860642669>✅</emoji> Зарплата выдана.',
        'str_d_sal': '\n<emoji document_id=5818665600624365278>❌</emoji> Платить некому.'
    }

    # Конфиг
    def __init__(self):  
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "sleep", 300,
                lambda: self.strings("sleep"),
                validator=loader.validators.Integer(minimum = 10)
            ),
            loader.ConfigValue(
                "resget", False,
                lambda: self.strings("resget"),
                validator=loader.validators.Boolean()
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
                await self.salget()
        else:
            self.set('fact_status', False)
            self.set('status', False)

    # Основная функция
    async def salget(self): 
        while True:
            await asyncio.sleep(0.5)
            if self.get('status') == True:
                self.set('fact_status', True)
                self.set('watcher', True)
                await self.client.send_message(self.get('group'), f'Я')
                await asyncio.sleep(10)
                self.set('watcher', False)
                await asyncio.sleep(self.config['sleep'] * 60)
            else:
                self.set('fact_status', False)
                break

    # Осн. наблюдатель
    @loader.watcher()
    async def watcher(self, message):
        if self.get('status') == True:
            if self.get('watcher') == True:
                if message.chat_id == self.get('group'):
                    if 'Ранг:' in message.raw_text and  'Уровень:' in message.raw_text:
                        await message.click(1) if 'Корпорация' in str(message) else await message.click(0)
                        await asyncio.sleep(0.5)
                        txt = '<emoji document_id=5188377234380954537>🌘</emoji> <b>SalGet is working...</b>'
                        urp = await message.reply(txt)
                        await asyncio.sleep(1)
                        urf = await urp.get_reply_message()
                        if self.config['resget'] == True:
                            if 'Собрать ресурсы' in str(urf):
                                await urf.click(1)
                                txt += self.strings['str_c_res']
                                await urp.edit(txt)
                                await asyncio.sleep(1)
                            else:
                                txt += self.strings['str_d_res']
                                await urp.edit(txt)
                                await asyncio.sleep(1)
                        if 'Заплатить' in str(urf):
                            txt += self.strings['str_c_sal']
                            await urp.edit(txt)
                            await urf.click(0)
                            return
                        else:
                            txt += self.strings['str_d_sal']
                            await urp.edit(txt)
                            return
                            
    # Подсчет, сколько раз поработали на вас                   
    @loader.watcher(chat_id = 6052095251)
    async def workstats(self, message):
        if 'поработал на' in message.raw_text:
            if message.from_id == 6052095251:
                a = self.get('stats')
                a += 1
                self.set('stats', a)

    # Включение/выключение модуля
    @loader.command(alias = 'sgs')
    async def salgetstatus(self, message):
        '''- включить / отключить модуль'''
        if self.get('group') != 0:
            if self.get('status') == True:
                self.set('status', False)
                await utils.answer(message, f'<emoji document_id=5325872701032635449>✅</emoji> <b>SalGet отключен.</b>')
                return
            else:
                self.set('status', True)
                txt = f'<emoji document_id=5325872701032635449>✅</emoji> <b>SalGet включен.</b>'
                if self.get('fact_status') == False:
                    txt += f'\n<emoji document_id=5327790373865530387>🔗</emoji> Цикл перезапущен.'
                await utils.answer(message, txt)
                if self.get('fact_status') == False:
                    await self.salget()
        else:
            await utils.answer(message, f'<emoji document_id=5980953710157632545>🚫</emoji> <b>Error</b> // <code>{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}</code>'
                '\n\n<emoji document_id=5818973781707722673>🗣</emoji> <b><u>Суть ошибки:</u></b>\nУ вас не установлена группа для работы модуля SalGet.'
                f'\n\n<emoji document_id=5821302890932736039>🗣</emoji> <b><u>Способы исправления:</u></b>\nУстановите группу для работы модуля SalGet при помощи команды <code>{utils.escape_html(self.get_prefix())}sgg</code>')
            return
        
    # Вывод статистики модуля
    @loader.command(alias = 'sgst')
    async def salgetstatistic(self, message):
        '''- посмотреть, сколько раз на вас поработали\n"reset" в аргументы, чтобы сбросить"'''
        if utils.get_args_raw(message).lower() == 'reset':
            self.set('stats', 0)
            await utils.answer(message, f'<emoji document_id=5307958727448469562>✅</emoji> Статистика SalGet сброшена.')
            return
        stats = str(self.get('stats'))
        if stats[-1] in ['1','5','6','7','8','9','0']:
            txt = f'{stats} раз'
        elif stats[-1] in ['2','3','4']:
            txt = f'{stats} раза'
        if len(stats) > 1:
            if stats[-2] in ['12','13','14']:
                txt = f'{stats} раз'
        await utils.answer(message, f'<emoji document_id=5188208446461188962>💯</emoji> <b>На вас поработали:</b> <code>{txt}</code>.')

    # Установка группы для модуля
    @loader.command(alias = 'sgg')
    async def salgetgroup(self, message):
        '''- установить группу для модуля'''
        if '-' in str(message.chat_id):
            if message.chat_id != self.get('group'):
                self.set('group', message.chat_id)
                await utils.answer(message, f'<emoji document_id=5325872701032635449>✅</emoji> | Группа {message.chat.title} (<code>{message.chat_id}</code>) установлена, как чат для SalGet.')
                return
            else:
                await utils.answer(message, f'<emoji document_id=5980953710157632545>🚫</emoji> <b>Error</b> // <code>{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}</code>'
                    '\n\n<emoji document_id=5818973781707722673>🗣</emoji> <b><u>Суть ошибки:</u></b>\nЭта группа уже установлена, как чат для SalGet.'
                    '\n\n<emoji document_id=5821302890932736039>🗣</emoji> <b><u>Способы исправления:</u></b>\nНапишите команду в другом чате, где есть Бизнесс Бот.')
                return
        else:
            await utils.answer(message, f'<emoji document_id=5980953710157632545>🚫</emoji> <b>Error</b> // <code>{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}</code>'
                '\n\n<emoji document_id=5818973781707722673>🗣</emoji> <b><u>Суть ошибки:</u></b>\nЭтот чат не является группой.'
                '\n\n<emoji document_id=5821302890932736039>🗣</emoji> <b><u>Способы исправления:</u></b>\nНапишите команду в другом чате, где есть Бизнесс Бот.')
            return
