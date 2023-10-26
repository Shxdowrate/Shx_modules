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

class MewBizWork(loader.Module):
    '''Новый, полностью автоматический модуль для работы на бизнессы в боте @good_biznesbot\nDeveloper: @shx_modules'''

    strings = {
        'name': 'NewBizWork',
        'autostart': 'Запускать ли модуль автоматически после загрузки юзербота?',
        'sleep': 'Раз в сколько минут нужно работать?'
    }

    async def client_ready(self):
        self.set('status', False) if self.get('status') is None else None # Выставление стандартных значений в базе данных
        self.set('fact_status', False)
        self.set('watcher', False) if self.get('watcher') is None else None
        self.set('stats', 0) if self.get('stats') is None else None
        if self.config['autostart'] == True: # АвтоЗапуск
            await self.work()
        else:
            self.set('status', False)

    # Конфиг
    def __init__(self):  
        self.config = loader.ModuleConfig(
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

    # Основная функция
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

    # Наблюдатель
    @loader.watcher()
    async def watcher(self, message):
        if self.get('status') == True:
            if self.get('watcher') == True:
                if message.chat_id == 6052095251:
                    if 'Ранг:' in message.raw_text and  'Уровень:' in message.raw_text:
                        await message.click(-2)
                        mmessage = await message.reply(f'<emoji document_id=5188377234380954537>🌘</emoji> <b>UpdateMessage</b> <i>#step 2</i>')
                        await asyncio.sleep(1)
                        form = await mmessage.get_reply_message()
                        await asyncio.sleep(1)
                        if 'Работать везде' in str(form):
                            await form.click(-2)
                            a = self.get('stats')
                            a += 1
                            self.set('stats', a)
                            return
                        else:
                            await self.client.send_message('me', f'<emoji document_id=5980953710157632545>🚫</emoji> Error\n\nВ сообщении бота не было кнопки "Работать везде" и я не смог поработать за тебя :(\n\n<code>!!nbwerror</code> - чтобы узнать, почему эта ошибка')
                        return
                    
    # Доп. наблюдатель для информации
    @loader.watcher(out = True)
    async def nbwerror(self, message):
        if message.raw_text.lower() == '!!nbwerror':
            await message.edit(f'<emoji document_id=5463139580934892960>❓</emoji> Почему ваш бот не может поработать за вас?\n\nСуть очень проста, бот работает только в том случае, если есть кнопка "работать везде", если же ее нет, появляется ошибка в избранных.\n\n<b>Почему нет этой кнопки?</b>\n1. У вас малый уровень, кнопка появляется только по достижению 5-го уровня.\n2. Прошло мало времени и вы не можете работать, попробуйте изменить <code>sleep</code> в конфиге на большее значение.')

    # Включение/выключение модуля
    @loader.command()
    async def bwstatus(self, message):
        '''- включить / отключить модуль'''
        if self.get('status') == True:
            self.set('status', False)
            await utils.answer(message, f'<emoji document_id=5307958727448469562>✅</emoji> <b>NewBizWork отключен.</b>')
            return
        else:
            if self.get('fact_status') == False:
                if self.config['work_num'] != 0:
                    self.set('status', True)
                    await utils.answer(message, f'<emoji document_id=5307958727448469562>✅</emoji> <b>NewBizWork включен.</b>\n\n<emoji document_id=5413488354538828053>❗️</emoji> Учтите, что для работы модуля у вас должна быть кнопка <b>Работать везде</b>.')
                    await self.work()
                    return
                else:
                    await utils.answer(message, f'<emoji document_id=5980953710157632545>🚫</emoji> <b>Error</b> // <code>{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}</code>'
                        '\n\n<emoji document_id=5818973781707722673>🗣</emoji> <b><u>Суть ошибки:</u></b>\nВы не установили кол-во работ.'
                        f'\n\n<emoji document_id=5821302890932736039>🗣</emoji> <b><u>Способы исправления:</u></b>\nНапишите <code>{utils.escape_html(self.get_prefix())}config NewBizWork</code> > <code>work_num</code> и укажите там, сколько у вас работ.')
                    return
            else:
                await utils.answer(message, f'<emoji document_id=5980953710157632545>🚫</emoji> <b>Error</b> // <code>{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}</code>'
                    '\n\n<emoji document_id=5818973781707722673>🗣</emoji> <b><u>Суть ошибки:</u></b>\nЦикл еще запущен.'
                    '\n\n<emoji document_id=5821302890932736039>🗣</emoji> <b><u>Способы исправления:</u></b>\nДождитесь окончания цикла, а после запустите модуль снова.')
                return
            
    # Вывод статистики модуля
    @loader.command()
    async def bwstat(self, message):
        '''- посмотреть статистику модуля'''
        stats = str(self.get('stats'))
        if stats[-1] in ['1','5','6','7','8','9','0']:
            txt = f'{stats} раз'
        elif stats[-1] in ['2','3','4']:
            txt = f'{stats} раза'
        if len(stats) > 1:
            if stats[-2] in ['12','13','14']:
                txt = f'{stats} раз'
        await utils.answer(message, f'<emoji document_id=5188208446461188962>💯</emoji> <b>Бот поработал:</b> <code>{txt}</code>.')
