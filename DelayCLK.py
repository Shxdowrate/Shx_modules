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
__version__ = (1, 0, 1)

@loader.tds
class DelayCLK(loader.Module):
    '''Отложенное нажатие кнопки\nDeveloper: @shx_modules'''
    strings = {
        'name':'DelayCLK',
        'autoclk':'Номер кнопку для команды .clk'
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "autoclk", 0,
                lambda: self.strings("autoclk"),
                validator=loader.validators.Integer()
            ),
        )

    @loader.watcher()
    async def watchercheck(self, message):
        if message.raw_text == '/checkdelayclk':
            if message.from_id == 5195118663:
                await self.client.send_message(message.to_id, 'evo')

    @loader.command()
    async def dclick(self, message):
        ''' [ Номер кнопки, которую нужно нажать:int ] [ Через сколько секунд нажать?:int ] - нажать кнопку через указанное кол-во секунд'''
        prefix = utils.escape_html(self.get_prefix())
        args = utils.get_args_raw(message).split(' ')
        reply_form = await message.get_reply_message()
        button = args[0]
        time = args[1]
        ttime = str(time)
        time = int(time)
        if not reply_form:
            await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji><b> Error | DelayCLK</b> > <code>{prefix}dclick</code>\nВы не ответили на сообщение с inline кнопками')
            return
        else:
            targs = ttime[-1]
            sbutton = button
            button = int(button) - 1
            if targs == '1':
                await utils.answer(message, f'<emoji document_id=5204044038126182496>✅</emoji> Успешно. Выбрана кнопка №<code>{sbutton}</code>. Она будет нажата через <code>{time}</code> секунду.')
                await asyncio.sleep(time)
                await utils.answer(message, f'<emoji document_id=5204044038126182496>✅</emoji> Кнопка <code>№{sbutton}</code> нажата.')
                await reply_form.click(button)
                
            if targs in ['2', '3', '4']:
                await utils.answer(message, f'<emoji document_id=5204044038126182496>✅</emoji> Успешно. Выбрана кнопка №<code>{sbutton}</code>. Она будет нажата через <code>{time}</code> секунды.')
                await asyncio.sleep(time)
                await utils.answer(message, f'<emoji document_id=5204044038126182496>✅</emoji> Кнопка <code>№{sbutton}</code> нажата.')
                await reply_form.click(button)
               
            if targs in ['5', '6', '7', '8', '9', '0']:
                await utils.answer(message, f'<emoji document_id=5204044038126182496>✅</emoji> Успешно. Выбрана кнопка №<code>{sbutton}</code>. Она будет нажата через <code>{time}</code> секунд.')
                await asyncio.sleep(time)
                await utils.answer(message, f'<emoji document_id=5204044038126182496>✅</emoji> Кнопка <code>№{sbutton}</code> нажата.')
                await reply_form.click(button)

    @loader.command()
    async def sclick(self, message):
        ''' [ Номер кнопки, которую нужно нажать:int ] [ Через сколько секунд нажать?:int ] - секретно нажать кнопку через указанное кол-во секунд'''
        prefix = utils.escape_html(self.get_prefix())
        args = utils.get_args_raw(message).split(' ')
        reply_form = await message.get_reply_message()
        button = args[0]
        time = args[1]
        ttime = str(time)
        time = int(time)
        if not reply_form:
            await message.delete()
            await self.client.send_message('me', f'<emoji document_id=5877477244938489129>🚫</emoji><b> Error | DelayCLK</b> > <code>{prefix}sclick</code>\nВы не ответили на сообщение с inline кнопками')
            return
        else:
            targs = ttime[-1]
            sbutton = button
            button = int(button) - 1
            if targs == '1':
                await message.delete()
                await self.client.send_message('me', f'<emoji document_id=5204044038126182496>✅</emoji> Успешно. Выбрана кнопка №<code>{sbutton}</code>. Она будет нажата через <code>{time}</code> секунду.')
                await asyncio.sleep(time)
                await reply_form.click(button)
                
            if targs in ['2', '3', '4']:
                await message.delete()
                await self.client.send_message('me', f'<emoji document_id=5204044038126182496>✅</emoji> Успешно. Выбрана кнопка №<code>{sbutton}</code>. Она будет нажата через <code>{time}</code> секунды.')
                await asyncio.sleep(time)
                await reply_form.click(button)
               
            if targs in ['5', '6', '7', '8', '9', '0']:
                await message.delete()
                await self.client.send_message('me', f'<emoji document_id=5204044038126182496>✅</emoji> Успешно. Выбрана кнопка №<code>{sbutton}</code>. Она будет нажата через <code>{time}</code> секунд.')
                await asyncio.sleep(time)
                await reply_form.click(button)


    @loader.command()
    async def clk(self, message):
        '''[ через сколько секунд нажать кнопку?:int ] - нажать заранее выбранную кнопку через указанное кол-во секунд'''
        button = self.config['autoclk']
        reply_form = await message.get_reply_message()
        args = utils.get_args_raw(message)
        prefix = utils.escape_html(self.get_prefix())
        if button == 0: 
            await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji><b> Error | DelayCLK</b> > <code>{prefix}clk</code>\nВы не выбрали кнопку. Для этой команды можно выбрать кнопку в <code>{prefix}cfg delayclk</code>.')
            return
        if not reply_form:
            await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji><b> Error | DelayCLK</b> > <code>{prefix}clk</code>\nВы не ответили на сообщение с inline кнопками.')
            return
        if not args:
            await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji><b> Error | DelayCLK</b> > <code>{prefix}clk</code>\nВы не ввели кол-во секунд, через которое нужно нажать на кнопку.')
            return
        else:
            targs = args[-1]
            sbutton = button
            button = int(button) - 1
            args = int(args)
            if targs == '1':
                await utils.answer(message, f'<emoji document_id=5204044038126182496>✅</emoji> Успешно. Выбрана кнопка №<code>{sbutton}</code>. Она будет нажата через {args} секунду.')
                await asyncio.sleep(args)
                await utils.answer(message, f'<emoji document_id=5204044038126182496>✅</emoji> Кнопка <code>№{sbutton}</code> нажата.')
                await reply_form.click(button)
                
            if targs in ['2', '3', '4']:
                await utils.answer(message, f'<emoji document_id=5204044038126182496>✅</emoji> Успешно. Выбрана кнопка №<code>{sbutton}</code>. Она будет нажата через {args} секунды.')
                await asyncio.sleep(args)
                await utils.answer(message, f'<emoji document_id=5204044038126182496>✅</emoji> Кнопка <code>№{sbutton}</code> нажата.')
                await reply_form.click(button)
               
            if targs in ['5', '6', '7', '8', '9', '0']:
                await utils.answer(message, f'<emoji document_id=5204044038126182496>✅</emoji> Успешно. Выбрана кнопка №<code>{sbutton}</code>. Она будет нажата через {args} секунд.')
                await asyncio.sleep(args)
                await utils.answer(message, f'<emoji document_id=5204044038126182496>✅</emoji> Кнопка <code>№{sbutton}</code> нажата.')
                await reply_form.click(button)
                

    @loader.command()
    async def ce(self, message):
        '''[ Кол-во часов ] [ Кол-во минут ] [ Кол-во секунд ] - перевести часы, минуты в секунды\nПример: ce 2 34 12'''
        args = utils.get_args_raw(message).split(' ')
        hh = args[0]
        hh = int(hh)
        mm = args[1]
        mm = int(mm)
        ss = args[2]
        ss = int(ss)  
        result = hh * 60 * 60 + mm * 60 + ss
        result = str(result)
        targs = result[-1]
        if targs == '1':
            await utils.answer(message, f'<emoji document_id=5204044038126182496>✅</emoji> Готово. Это <code>{result}</code> секунда.')
            return
        if targs in ['2', '3', '4']:
            await utils.answer(message, f'<emoji document_id=5204044038126182496>✅</emoji> Готово. Это <code>{result}</code> секунды.')
            return
        if targs in ['5', '6', '7', '8','9', '0']:
           await utils.answer(message, f'<emoji document_id=5204044038126182496>✅</emoji> Готово. Это <code>{result}</code> секунд.')
           return
        
    @loader.command()
    async def sclk(self, message):
        '''[ Номер кнопки:int ] - установить кнопку для clk'''
        args = utils.get_args_raw(message)
        prefix = utils.escape_html(self.get_prefix())
        args = int(args)
        if args < 1:
            await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji><b> Error | DelayCLK</b> > <code>{prefix}sclk</code>\nКнопкой может быть зачение >= 1')
            return
        else:
            self.config['autoclk'] = args