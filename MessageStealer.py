#—————————————————————————————————————————————————————————————————————————————————
#  █▀ █ █ ▀▄▀   █▀▄▀█ █▀█ █▀▄ █ █ █   █▀▀ █▀ Chanel: https://t.me/mescr_m
#  ▄█ █▀█ █ █   █ ▀ █ █▄█ █▄▀ █▄█ █▄▄ ██▄ ▄█ Not Licensed
#—————————————————————————————————————————————————————————————————————————————————
#  █▀▀ ▀▄▀ █   █ █ █▀ █ █ █ █▀▀   █▀▄▀█ █▀█ █▀▄ █ █ █   █▀▀ █▀
#  ██▄ █ █ █▄▄ █▄█ ▄█ █ ▀▄▀ ██▄   █ ▀ █ █▄█ █▄▀ █▄█ █▄▄ ██▄ ▄█
#—————————————————————————————————————————————————————————————————————————————————
# Idea:
# meta developer: @mescr_m
# Thanks:
#—————————————————————————————————————————————————————————————————————————————————

from .. import utils, loader
from telethon.tl.functions.users import GetFullUserRequest

__version__ = (2, 0, 0)

@loader.tds
class MessageStealer(loader.Module):
    '''Forward a message from a secret chat to your favorites. Supports only text messages\n\nOr can be forwarded using a secret word'''

    strings = {
        'name':'MessageStealer',
        'error':"You didn't reply to the message you want to steal.",
        'word':'New word for secret forwarding:',
        'word_2':'Now if there is a word in your message,',
        'word_3':', the message will automatically be forwarded to your favorites',
        
    }
    strings_ru = {
        'error':'Вы не ответили на сообщение, которое хотите украсть.',
        'word':'Новое слово для секретной пересылки:',
        'word_2':'Теперь если в вашем сообщении есть слово',
        'word_3':', то сообщение автоматически перешлется к вам в избранные',
        '_cls_doc':'Переслать в избранное сообщение из секретного чата. Поддерживает только текстовые сообщения\n\nИли можно пересылать с помощью секретного слова'
    }
    strings_de = {
        'error':'Sie haben nicht auf die Nachricht geantwortet, die Sie stehlen möchten.',
        'word':'Neues Wort für geheime Weiterleitung:',
        'word_2':'Nun, wenn Ihre Nachricht ein Wort enthält',
        'word_3':', dann wird die Nachricht automatisch zu Ihren Favoriten weitergeleitet',
        '_cls_doc':'Eine Nachricht aus einem geheimen Chat an Ihre Favoriten weiterleiten. Unterstützt nur Textnachrichten\n\nUnd kann mit einem geheimen Wort weitergeleitet werden'
    }

    async def cliwnt_ready(self, client, db):
        self.client = client
        self.db = db
        a = self.db.get(self.name, 'word_steal')
        if a == None:
            self.db.set(self.name, 'word_steal', 'стил')


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

    @loader.watcher(out = True)
    async def watcher(self, message):
        word_steal = self.db.get(self.name, 'word_steal')
        if word_steal in message.raw_text:
            reply_message = await message.get_reply_message()
            if not reply_message:
                return
            else:
                user = reply_message.sender_id
                name = reply_message.sender.first_name
                text = reply_message.text
                await self.client.send_message('me', f'<b>Сообщение от <a href="tg://user?id={user}">{name}:</a></b>\n\n<code>{text}</code>')

    @loader.command(
        ru_doc = '[ Слово ] - изменить слово для секретной пересылки',
        de_doc = '[ Wort ] - das Wort für die geheime Weiterleitung ändern',
        alias = 'chw'
    )
    async def changeword(self, message):
        '''[ Word ] - change the word for secret forwarding'''
        args = utils.get_args_raw(message)
        self.db.set(self.name, 'word_steal', args)
        text = self.strings['word']
        text2 = self.strings['word_2']
        text3 = self.strings['word_3']
        await utils.answer(message, f'<emoji document_id=5332533929020761310>✅</emoji> | <b>{text}</b> <code>{args}</code>.\n{text2} <code>{args}</code>{text3}')
