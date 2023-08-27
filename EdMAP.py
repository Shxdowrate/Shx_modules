#—————————————————————————————————————————————————————————————————————————————————
#  █▀ █ █ ▀▄▀   █▀▄▀█ █▀█ █▀▄ █ █ █   █▀▀ █▀ Channel: https://t.me/shx_modules
#  ▄█ █▀█ █ █   █ ▀ █ █▄█ █▄▀ █▄█ █▄▄ ██▄ ▄█ Not Licensed
#—————————————————————————————————————————————————————————————————————————————————
# Idea:
# meta developer: @shx_modules
# Thanks: 
#—————————————————————————————————————————————————————————————————————————————————

from .. import loader, utils
from telethon import functions, types
import inspect

class EdMAP(loader.Module):
    '''Модуль для управления префиксом группе.\nВы должны быть создателем!\nDeveloper: @shx_modules'''

    strings = {
        'name':'EdMAP'
    }

    @loader.command()
    async def edmap(self, message):
        '''[ Новый префикс ] - редактировать префикс'''
        args = utils.get_args_raw(message)
        error_cmd = f'<code>{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}</code>'
        
        if message.is_private: # Если команда в лс
            await utils.asnwer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error</b> | <code>{error_cmd}</code>\nЭта команда работает только в группе.')
            return
        
        if not args: # Если нет аргумента
            await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error</b> | <code>{error_cmd}</code>\nВы не указали, какой вам поставить префикс.')
            return
        
        else:
            len_args = len(args)
            
            if len_args > 16: # Если префикс длинее допустимого
                await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error</b> | <code>{error_cmd}</code>\nВы указали префикс "{args}", в нем больше 16-ти символов.')
                return
            
            else: # Если все гуд
                await self.client(functions.channels.EditAdminRequest(
                    channel=message.chat_id,
                    user_id=message.sender_id,
                    admin_rights=types.ChatAdminRights(),
                    rank=args
                ))
                await utils.answer(message, f'<emoji document_id=5332533929020761310>✅</emoji> | Ваш префикс изменен на <code>{args}</code>')
                return               