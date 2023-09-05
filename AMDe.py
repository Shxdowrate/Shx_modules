#—————————————————————————————————————————————————————————————————————————————————
#  █▀ █ █ ▀▄▀   █▀▄▀█ █▀█ █▀▄ █ █ █   █▀▀ █▀ Channel: https://t.me/shx_modules
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

class AMDe(loader.Module):
    '''Модуль для автоматического удаления ваших сообщений.\nDeveloper: @shx_modules'''
    strings = {
        'name':'AMDe',
        'PM_status':'Удалять ли ваши сообщения в лс?',
        'deltime':'Через сколько секунд удалять сообщения?'
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "PM_status", True,
                lambda: self.strings("PM_status"),
                validator=loader.validators.Boolean()
            ),
            loader.ConfigValue(
                "deltime", 20,
                lambda: self.strings("deltime"),
                validator=loader.validators.Integer(minimum = 1)
            ),
        )
    
    @loader.watcher(out = True)
    async def watcher(self, message):
        if message:
            if self.get('delm_status') == True:
                mtime = self.config['deltime']
                if message.chat_id in self.get('delbl'):
                    return
                else:
                    if message.is_private:
                        if self.config['PM_status'] == True:
                            await asyncio.sleep(mtime)
                            await message.delete()
                            return
                    else:
                        await asyncio.sleep(mtime)
                        await message.delete()
                        return

    async def client_ready(self):
        a = self.get('delm_status')
        if a == None:
            self.set('delm_status', False)
        a = self.get('delbl')
        if a == None:
            self.set('delbl', [])

    @loader.command()
    async def amde(self, message):
        '''- включить/выключить модуль'''
        delm_status = self.get('delm_status')
        if delm_status == True:
            await utils.answer(message, f'<emoji document_id=5332533929020761310>✅</emoji> | AMD отключен.')
            self.set('delm_status', False)
            return
        else:
            pm = self.config['PM_status']
            mtime = self.config['deltime']
            if pm == True:
                pm_text = '<emoji document_id=5280736288423551158>🔒</emoji> | Удаление в лс включено.'
            else:
                pm_text = '<emoji document_id=5280736288423551158>🔒</emoji> | Удаление в лс отключено.'
            self.set('delm_status', True)
            await utils.answer(message, f'<emoji document_id=5332533929020761310>✅</emoji> | AMD включен.\n\n{pm_text}\n<emoji document_id=5307773751796964107>⏳</emoji> | Сообщения удаляются через {mtime} секунд.')
            return

    @loader.command()
    async def amdg(self, message):
        '''[ аргумент / ничего] - добавить/удалить/просмотреть чаты, в которых не будут удаляться ваши сообщения\nНапишите в аргумент что угодно, чтобы добавить текущий чат в черный список AMDe.'''
        args = utils.get_args_raw(message)
        error_cmd = f'<code>{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}</code>'
        delbl = self.get('delbl')
        
        if not args:
            if not delbl:
                await utils.answer(message, f'🟢 <b>Черный список AMDe пуст.</b>')
                return
            else:
                text = f'⚫ <b>Черный список AMDe</b>\n\n'
                s = 0
                for chat in delbl:
                    s += 1
                    try:
                        chate = await self.client.get_entity(chat)
                        chat = str(chat)
                        if '-' in chat:
                            text += f'{s} | {chate.title} (<code>{chat}</code>)\n'
                            
                        else:
                            text += f'{s} | {chate.first_name} (<code>{chat}</code>)\n'
                            
                    except:
                        text += f'_error_name_ (<code>{chat}</code>)\n'

                await utils.answer(message, f'{text}')
                return
        if args:
            chat = message.chat_id
            chate = await self.client.get_entity(chat)
            if message.is_private:
                chat_name = chate.first_name
            else:
                chat_name = chate.title
            if chat in delbl:
                
                self.get('delbl').remove(chat)
                await utils.answer(message, f'<emoji document_id=5332533929020761310>✅</emoji> | <b>Чат</b> {chat_name} (<code>{chat}</code>) <b>удален из черного списка AMDe.</b>')
                return
            else:
                self.get('delbl').append(chat)
                await utils.answer(message, f'<emoji document_id=5332533929020761310>✅</emoji> | <b>Чат</b> {chat_name} (<code>{chat}</code>) <b>добавлен в черный список AMDe.</b>')
                return
                
        