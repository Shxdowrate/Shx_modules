#—————————————————————————————————————————————————————————————————————————————————
#  █▀ █ █ ▀▄▀   █▀▄▀█ █▀█ █▀▄ █ █ █   █▀▀ █▀ Chanel: https://t.me/shx_modules
#  ▄█ █▀█ █ █   █ ▀ █ █▄█ █▄▀ █▄█ █▄▄ ██▄ ▄█ Not Licensed
#—————————————————————————————————————————————————————————————————————————————————
# Idea:
# meta developer: @shx_modules
# Thanks: 
#—————————————————————————————————————————————————————————————————————————————————

from .. import loader, utils
import asyncio
from asyncio import sleep
import inspect


__version__ = (1, 0, 0)

class BizWork(loader.Module):
    '''Модуль для автоматической работы в бизнесса других игроков в боте @good_biznesbot\nDeveloper: @shx_modules'''
    strings = {
        'name': 'BizWork',
        'corp_status': 'Состоите ли вы в корпорации?',
        'work_num':'Сколько у вас работ?',
        'autostart': 'Запускать ли модуль автоматически после загрузки юзербота?',
        'sleep': 'Раз в сколько минут нужно работать?'
        
        
    }

    async def client_ready(self):
        self.set('status', False) if self.get('status') is None else None
        self.set('fact_status', False)
        self.set('watcher', False) if self.get('watcher') is None else None
        if self.config['autostart'] == True:
            await self.work()
        else:
            self.set('status', False)

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "corp_status", False,
                lambda: self.strings("corp_status"),
                validator=loader.validators.Boolean()
            ),
            loader.ConfigValue(
                "work_num", 0,
                lambda: self.strings("work_num"),
                validator=loader.validators.Integer()
            ),
            loader.ConfigValue(
                "sleep", 65,
                lambda: self.strings("sleep"),
                validator=loader.validators.Integer(minimum = 60)
            ),
            loader.ConfigValue(
                "autostart", False,
                lambda: self.strings("autostart"),
                validator=loader.validators.Boolean()
            ),
            
            
        )

    async def work(self):
        while True:
            await asyncio.sleep(0.5)
            if self.get('status') == True:
                self.set('fact_status', True)
                self.set('watcher', True)
                await self.client.send_message(6052095251, f'Я')
                await asyncio.sleep(10)
                self.set('watcher', False)
                await asyncio.sleep(self.config['sleep'] * 60)
            else:
                self.set('fact_status', False)
                break

    @loader.watcher()
    async def watcher(self, message):
        if self.get('status') == True:
            if self.get('watcher') == True:
                if message.chat_id == 6052095251:
                    if 'Ранг:' in message.raw_text and  'Уровень:' in message.raw_text:
                        button = 5 if self.config['corp_status'] == True else 4
                        await message.click(button)
                        mmessage = await message.reply(f'<code>| BizWork | UpdateReplyMessageData</code>')
                        await asyncio.sleep(1)
                        form = await mmessage.get_reply_message()
                        await asyncio.sleep(1)
                        await form.click(self.config['work_num'])
                        return

   

                        
                

    @loader.command()
    async def bwstatus(self, message):
        '''- включить / отключить модуль'''
        if self.get('status') == True:
            self.set('status', False)
            await utils.answer(message, f'<emoji document_id=5307958727448469562>✅</emoji> <b>BizWork отключен.</b>')
            return
        else:
            if self.get('fact_status') == False:
                if self.config['work_num'] != 0:
                    self.set('status', True)
                    await utils.answer(message, f'<emoji document_id=5307958727448469562>✅</emoji> <b>BizWork включен.</b>\n\n<emoji document_id=5413488354538828053>❗️</emoji> Учтите, что для работы модуля у вас даолжна быть кнопка <b>Работать везде</b>.')
                    await self.work()
                    return
                else:
                    await utils.answer(message, f'<emoji document_id=5980953710157632545>🚫</emoji> <b>Error</b> // <code>{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}</code>'
                    '\n\n<emoji document_id=5818973781707722673>🗣</emoji> <b><u>Суть ошибки:</u></b>\nВы не установили кол-во работ.'
                    f'\n\n<emoji document_id=5821302890932736039>🗣</emoji> <b><u>Способы исправления:</u></b>\nНапишите <code>{utils.escape_html(self.get_prefix())}config bizwork</code> > <code>work_num</code> и укажите там, сколько у вас работ.')
                    return
            else:
                await utils.answer(message, f'<emoji document_id=5980953710157632545>🚫</emoji> <b>Error</b> // <code>{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}</code>'
                    '\n\n<emoji document_id=5818973781707722673>🗣</emoji> <b><u>Суть ошибки:</u></b>\nЦикл еще запущен.'
                    '\n\n<emoji document_id=5821302890932736039>🗣</emoji> <b><u>Способы исправления:</u></b>\nДождитесь окончания цикла, а после запустите модуль снова.')
                return

    @loader.command()
    async def bwsetwork(self, message):
        '''[ Кол-во ] - установить кол-во работ'''
        args = utils.get_args_raw(message)
        if args:
            if args.isdigit():
                work = int(args)
                if work > 0:
                    self.config['work_num'] == work
                    await utils.answer(message, f'<emoji document_id=5307958727448469562>✅</emoji> <b>Кол-во работ изменено на <code>{work}</code></b>.')
                    return
                else:
                    await utils.answer(message, f'<emoji document_id=5980953710157632545>🚫</emoji> <b>Error</b> // <code>{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}</code>'
                    '\n\n<emoji document_id=5818973781707722673>🗣</emoji> <b><u>Суть ошибки:</u></b>\nРабот не может меньше одной.'
                    '\n\n<emoji document_id=5821302890932736039>🗣</emoji> <b><u>Способы исправления:</u></b>\nУкажите точное кол-во ваших работ.')
                    return
            else:
                await utils.answer(message, f'<emoji document_id=5980953710157632545>🚫</emoji> <b>Error</b> // <code>{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}</code>'
                    '\n\n<emoji document_id=5818973781707722673>🗣</emoji> <b><u>Суть ошибки:</u></b>\nКол-вом работ может являться только целочисленное.'
                    '\n\n<emoji document_id=5821302890932736039>🗣</emoji> <b><u>Способы исправления:</u></b>\nУкажите точное кол-во ваших работ одной цифрой.')
                return
        else:
            await utils.answer(message, f'<emoji document_id=5980953710157632545>🚫</emoji> <b>Error</b> // <code>{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}</code>'
                    '\n\n<emoji document_id=5818973781707722673>🗣</emoji> <b><u>Суть ошибки:</u></b>\nВы не указали аргумент.'
                    '\n\n<emoji document_id=5821302890932736039>🗣</emoji> <b><u>Способы исправления:</u></b>\nУкажите аргумент.')
