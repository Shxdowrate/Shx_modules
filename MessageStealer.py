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

from .. import utils, loader
from telethon.tl.functions.users import GetFullUserRequest

__version__ = (1, 0, 0)

@loader.tds
class MessageStealer(loader.Module):
    '''Переслать в избранное сообщение из секретного чата. Поддерживает только текстовые сообщения'''

    strings = {
        'name':'MessageStealer',
        'error':"You didn't reply to the message you want to steal."
    }
    strings_ru = {
        'error':'Вы не ответили на сообщение, которое хотите украсть.'
    }
    strings_de = {
        'error':'Sie haben nicht auf die Nachricht geantwortet, die Sie stehlen möchten.'
    }

    


    @loader.command(
            ru_doc='<ответ на сообщение> - переслать сообщение в избранное',
            de_doc='<antwort auf eine Nachricht> - Nachricht an Ihre Favoriten weiterleiten',
            alias = 'sm'
    )
    async def steal(self, message):
        '''<reply to message> - forward the message to favorites'''
        await message.delete()
        reply = await message.get_reply_message()
        prefix = utils.escape_html(self.get_prefix())
       
        if not reply:
            await self.client.send_message('me', f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error |</b> <code>{prefix}steal</code>\n' + self.strings['error'])
            return
        else:
            user = reply.sender_id
            name = reply.sender.first_name
            text = reply.text
            await self.client.send_message('me', f'<b>Сообщение от <a href="tg://user?id={user}">{name}:</a></b>\n\n<code>{text}</code>')