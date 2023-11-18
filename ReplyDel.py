#—————————————————————————————————————————————————————————————————————————————————
#  █▀ █ █ ▀▄▀   █▀▄▀█ █▀█ █▀▄ █ █ █   █▀▀ █▀ Channel: https://t.me/mescr_m
#  ▄█ █▀█ █ █   █ ▀ █ █▄█ █▄▀ █▄█ █▄▄ ██▄ ▄█ Not Licensed
#—————————————————————————————————————————————————————————————————————————————————
# Idea:
# meta developer: @mescr_m
# Thanks: 
#—————————————————————————————————————————————————————————————————————————————————

__version__ = (1, 0, 0)

from .. import utils, loader
import inspect

class ReplyDel(loader.Module):
    '''Модуль автоматически удаляет ваше сообщение, если на него кто-то ответил\nDeveloper: @mescr_m'''

    strings = {
        'name':'ReplyDel',
    }


    async def client_ready(self):
        myid = await self.client.get_me()
        self.set('myid', myid.id)
        if self.get('wl') == None:
            self.set('wl', [])
        if myid.id not in self.get('wl'):
            self.get('wl').append(myid.id)
        if self.get('status') == None:
            self.set('status', False)

    @loader.command()
    async def rds(self, message):
        '''- включить/выключить модуль'''
        if self.get('status') == False:
            self.set('status', True)
            await utils.answer(message, f'<emoji document_id=5332533929020761310>✅</emoji> <b>ReplyDel включен.</b>')
            return
        else:
            self.set('status', False)
            await utils.answer(message, f'<emoji document_id=5332533929020761310>✅</emoji> <b>ReplyDel выключен.</b>')
            return
    
    @loader.command()
    async def rdwls(self, message):
        '''- добавить/удалить пользователя из белого листа ( если ответил он, то ваше сообщение не удалится )'''
        wl = self.get('wl')
        r = await message.get_reply_message()
        error_cmd = f'{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}'
        if r:
            if r.from_id in wl:
                self.get('wl').remove(r.from_id)
                await utils.answer(message, f'<emoji document_id=5332533929020761310>✅</emoji> <b>Пользователь {r.sender.first_name} (<code>{r.from_id}</code>) удален из белого списка.</b>')
                return
            else:
                self.get('wl').append(r.from_id)
                await utils.answer(message, f'<emoji document_id=5332533929020761310>✅</emoji> <b>Пользователь {r.sender.first_name} (<code>{r.from_id}</code>) добавлен в белый список.</b>')
                return
        else:
            await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error</b> | <code>{error_cmd}</code>\nВы не ответили на сообщения пользователя, которго хотите добавить или удалить из белого списка.')
            return
    
    @loader.command()
    async def rdwl(self, message):
        '''- вывести белый список ReplyDel'''
        wl = self.get('wl')
        if wl:
            text = '<emoji document_id=5936283232780684228>👥</emoji> Белый список ReplyDel:\n\n'
            num = 0
            for user in wl:
                num += 1
                try:
                    usernick = await self.client.get_entity(user)
                    usernick = usernick.first_name
                    text += f'{num} | {usernick} (<code>{user}</code>)\n'
                except:
                    text += f'{num} | <code>{user}</code>\n'
                finally:
                    await utils.answer(message, text)
        else:
            await utils.answer(message, f'<emoji document_id=5936283232780684228>👥</emoji> Белый список ReplyDel пуст.')
            return

    @loader.watcher(only_messages=True)
    async def watcher(self, message):
        if message:
            if self.get('status') == True:
                chat = str(message.chat_id)
                if '-' in chat:
                    r = await message.get_reply_message()
                    if r:
                        if r.from_id == self.get('myid'):
                            if message.from_id not in self.get('wl'):
                                await r.delete()

