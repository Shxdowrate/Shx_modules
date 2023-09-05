#—————————————————————————————————————————————————————————————————————————————————
#  █▀ █ █ ▀▄▀   █▀▄▀█ █▀█ █▀▄ █ █ █   █▀▀ █▀ Chanel: https://t.me/shx_modules
#  ▄█ █▀█ █ █   █ ▀ █ █▄█ █▄▀ █▄█ █▄▄ ██▄ ▄█ Not Licensed
#—————————————————————————————————————————————————————————————————————————————————
# Idea:
# meta developer: @shx_modules
# Thanks: 
#—————————————————————————————————————————————————————————————————————————————————

from .. import utils, loader
import inspect
import asyncio
from asyncio import sleep

class MineEVOAP(loader.Module):
    '''Модуль для автоматического удаления сообщений от MineEVO через указанное кол-во секунд.\nDeveloper: @shx_modules'''
    strings = {
        'name':'MineEVOAP',
        'waiting_time':'Через сколько секунд удалять сообщение?'
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "waiting_time", 60,
                lambda: self.strings("waiting_time"),
                validator=loader.validators.Integer()
            ),
        )

    @loader.watcher(only_messages = True)
    async def watcher(self, message):
        if self.get('amstatus') == True:
            if message.from_id == 5522271758:
                groups = self.get('groups')
                if message.chat_id in groups:
                    sleep = self.config['waiting_time']
                    await asyncio.sleep(sleep)   
                    await message.delete()
                
    async def client_ready(self):
        if self.get('groups') == None:
            self.set('groups', [])
        if self.get('amstatus') == None:
            self.set('amstatus', False)

    @loader.command(alias = 'amg')
    async def amgroup(self, message):
        '''[ ID группы / ничего ] - добавить/удалить группу из MineEVOAP'''
        args = utils.get_args_raw(message)
        error_cmd = f'<code>{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}</code>'
        if args:
            if args[0] == '-':
                if args[1:].isdigit():
                    try:
                        a = await self.client.get_entity(int(args))
                    except:
                        await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error</b> | <code>{error_cmd}</code>\nГруппа не найдена.')
                        return
                    else:
                        if int(args) in self.get('groups'):
                            self.get('groups').remove(int(args))
                            await utils.answer(message, f'<emoji document_id=5332533929020761310>✅</emoji> | Группа {a.title} (<code>{int(args)}</code>) удалена из MineEVOAP')
                            return
                        else:
                            self.get('groups').append(int(args))
                            await utils.answer(message, f'<emoji document_id=5332533929020761310>✅</emoji> | Группа {a.title} (<code>{int(args)}</code>) добавлена в список MineEVOAP')
                            return
                else:
                    await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error</b> | <code>{error_cmd}</code>\nID групп может состоять только из цифр.')
                    return
            else:
                await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error</b> | <code>{error_cmd}</code>\nID групп всегда начинается с "-".')
                return
        else:
            if message.is_private == False:
                group = message.chat_id
                a = await self.client.get_entity(group)
                if group in self.get('groups'):
                    self.get('groups').remove(group)
                    await utils.answer(message, f'<emoji document_id=5332533929020761310>✅</emoji> | Группа {a.title} (<code>{group}</code>) удалена из MineEVOAP')
                    return
                else:
                    self.get('groups').append(group)
                    await utils.answer(message, f'<emoji document_id=5332533929020761310>✅</emoji> | Группа {a.title} (<code>{group}</code>) добавлена в список MineEVOAP')
                    return
            else:
                await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error</b> | <code>{error_cmd}</code>\nЛичный чат не может стать группой, увы.')
                return
                    
    @loader.command(alias = 'amgs')
    async def amgroups(self, message):
        '''- открыть список групп MineEVOAP'''
        groups = self.get('groups')
        text = '<emoji document_id=5936283232780684228>👥</emoji> | <b>Группы модуля MineEVOAP</b>:\n\n'
        place = 0
        if not groups:
            await utils.answer(message, '<emoji document_id=5936283232780684228>👥</emoji> | <b>Список групп для модуля MineEVOAP пуст :(</b>')
            return
        else:
            for group in groups:
                try:
                    a = await self.client.get_entity(group)
                    a = a.title
                    place += 1
                    text += f'{place} | {a} (<code>{group}</code>)\n'
                except Exception:
                    place += 1
                    text += f'{place} | (<code>{group}</code>)\n'
                finally:
                    await utils.answer(message, f'{text}')

    @loader.command()
    async def ams(self, message):
        '''- включить/отключить MineEVOAP'''
        wt = self.config['waiting_time']
        if self.get('amstatus') == False:
            self.set('amstatus', True)
            await utils.answer(message, f'<emoji document_id=5332533929020761310>✅</emoji> | <b>MineEVOAP включен.</b>\n<emoji document_id=5307773751796964107>⏳</emoji> | Собщения удаляются через {wt} секунд.')
            return
        else:
            self.set('amstatus', False)
            await utils.answer(message, f'<emoji document_id=5332533929020761310>✅</emoji> | <b>MineEVOAP отключен.</b>')
            return
