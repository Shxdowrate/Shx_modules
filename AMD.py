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

class AMD(loader.Module):
    '''Модуль для автоматического удаления ваших сообщений.\nDeveloper: @shx_modules'''
    strings = {
        'name':'AMD',
        'PM_status':'Удалять ли ваши сообщения в лс?',
        'deltime':'Через сколько секунд удалять сообщения?'
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "PM_status", False,
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
    async def delstatus(self, message):
        ''' - включить/выключить модуль'''
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
            await utils.answer(message, f'<emoji document_id=5332533929020761310>✅</emoji> | AMD включен.\n\n{pm_text}\nСообщения удаляются через {mtime} секунд.')
            return

    @loader.command()
    async def delbl(self, message):
        '''[ ! / ничего] - добавить/удалить/просмотреть чаты, в которых не будут удаляться ваши сообщения'''
        args = utils.get_args_raw(message)
        error_cmd = f'<code>{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}</code>'
        delbl = self.get('delbl')
        if not args:
            if not delbl:
                await utils.answer(message, f'🟢 <b>Черный список модуля пуст.</b>')
                return
            else:
                bllist ='</code> | <code>'.join(map(str, delbl))
                await utils.answer(message, f'⚫ <b>Черный список модуля:</b>\n\n<code>{bllist}</code>')
                return
        if args:
            chat = message.chat_id
            if args == '!':
                if chat in delbl:
                    self.get('delbl').remove(chat)
                    await utils.answer(message, f'<emoji document_id=5332533929020761310>✅</emoji> | Чат {chat} удален из черного списка модуля.')
                    return
                else:
                    self.get('delbl').append(chat)
                    await utils.answer(message, f'<emoji document_id=5332533929020761310>✅</emoji> | Чат {chat} добавлен в черный список модуля.')
                    return
            else:
                await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error</b> | <code>{error_cmd}</code>\nФункции "{args}" не существует.')
                return
                
                
        