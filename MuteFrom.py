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
from telethon.tl.functions.users import GetFullUserRequest

__version__ = (1, 0, 0)

@loader.tds
class MuteFrom(loader.Module):
    '''A module for automatically reading messages from certain users/bots, which will save you from notifications.\nDeveloper: @shx_modules'''
    strings = {
        'name':'MuteFrom',
        'from_id':'Which users do not receive notifications from? \nID Only',
        'add_user_1':'<emoji document_id=5204044038126182496>✅</emoji> User',
        'add_user_2':'added to mute list.',
        'error_args_isdigit':'Only user and bot IDs can be in the mutе list.',
        'already_add_1':'The user',
        'already_add_2':'is already in the mute list.',
        'error_add_not_reply_or_args':'You did not respond to the message and did not provide arguments.',
        'remove_user':'has been successfully removed from the mute list.',
        'error_not_user_1':'The user',
        'error_not_user_2':'is already not in the mute list.',
        'remove_user':'removed from the mute list.',
        'blank':'<emoji document_id=5204044038126182496>✅</emoji> <b>The list is empty.</b>',
        'no_blank':'<b>List of IDs in the mutlist:</b>'
    }
    strings_ru = {
        'from_id':'От каких пользователей не получать уведомления? \nТолько ID',
        'add_user_1':'<emoji document_id=5204044038126182496>✅</emoji> Пользователь',
        'add_user_2':'добавлен в мут лист.',
        'error_args_isdigit':'В мут листе могут находиться только ID пользователей и ботов.',
        'already_add_1':'Пользователь',
        'already_add_2':'уже есть в мут листе.',
        'error_add_not_reply_or_args':'Вы не ответили на сообщение и не указали аргументы.',
        'remove_user':'успешно удален из мут листа.',
        'error_not_user_1':'Пользователя',
        'error_not_user_2':'и так нет в мут листе.',
        'remove_user':'удален из мут листа.',
        '_cls_doc':'Модуль для автоматического чтения сообщений от определенных пользователей/ботов, который будет избавлять вас от уведомлений.\nDeveloper: @shx_modules',
        'blank':'<emoji document_id=5204044038126182496>✅</emoji> <b>Список пуст.</b>',
        'no_blank':'<b>Список ID в мут листе:</b>'
    }
    strings_de = {
        'from_id':'Von welchen Benutzern erhalten Sie keine Benachrichtigungen? \nNur ID',
        'add_user_1':'<emoji document_id=5204044038126182496>✅</emoji> Benutzer',
        'add_user_2':'wurde dem stillen Blatt hinzugefügt.',
        'error_args_isdigit':'Das stille Blatt kann nur Benutzer- und Bots-IDs enthalten.',
        'already_add_1':'Benutzer',
        'already_add_2':'bereits im stillen Blatt vorhanden.',
        'error_add_not_reply_or_args':'Sie haben auf die Nachricht nicht geantwortet und keine Argumente angegeben.',
        'remove_user':'wurde erfolgreich aus dem stillen Blatt entfernt.',
        'error_not_user_1':'Der Benutzer',
        'error_not_user_2':'ist nicht im stillen Blatt.',
        'remove_user':'aus dem stillen Blatt entfernt.',
        '_cls_doc':'Ein Modul zum automatischen Lesen von Nachrichten von bestimmten Benutzern/Bots, das Sie vor Benachrichtigungen schützt.\nDeveloper: @shx_modules',
        'blank':'<emoji document_id=5204044038126182496>✅</emoji> <b>Die Liste ist leer.</b>',
        'no_blank':'<b>ID-Liste in einem stillen Blatt:</b>'
    }



    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "from_id", '',
                lambda: self.strings("from_id"),
                validator=loader.validators.Series()
            ),
        )

    @loader.watcher()
    async def watcher(self, message):
        mutelist = self.config['from_id']
        if message.from_id in mutelist:
                await self._client.send_read_acknowledge(
                message.peer_id,
                message,
                )

    @loader.command(
        ru_doc = '<ответ на сообщение/ID> добавить пользователя/бота в мут лист.',
        de_doc = '<antwort auf eine Nachricht/ID> Benutzer/Bot zur Stille-Tabelle hinzufügen.',
    )
    async def addmf(self, message):
        '''<reply to message/ID> add user/bot to mute list'''
        args = utils.get_args_raw(message)
        mutelist = self.config['from_id']
        error_add_not_reply_or_args = self.strings['error_add_not_reply_or_args']
        prefix = utils.escape_html(self.get_prefix())
        add_1 = self.strings['add_user_1']
        add_2 = self.strings['add_user_2']
        error_args_isdigit = self.strings['error_args_isdigit']
        error_already_add_1 = self.strings['already_add_1']
        error_already_add_2 = self.strings['already_add_2']
        reply_user = await message.get_reply_message()
        if args:
            if args.isdigit() == True:
                if args in mutelist:
                    await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error |</b> <code>{prefix}addmf</code>\n{error_already_add_1} {args} {error_already_add_2}')
                    return
                else:
                    self.config['from_id'].append(args)
                    await utils.answer(f'{add_1} <code>{args}</code> {add_2}')
                    return
            else:
                await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error |</b> <code>{prefix}addmf</code>\n{error_args_isdigit}')
                return
        elif reply_user:
            user = reply_user.sender_id
            user_name = reply_user.sender.first_name
            if user in mutelist:
                await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error |</b> <code>{prefix}addmf</code>\n{error_already_add_1} {user_name} {error_already_add_2}')
                return
            else:
                self.config['from_id'].append(user)
                await utils.answer(message, f'{add_1} <code>{user_name}</code> {add_2}')
                return
        else:
            await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error |</b> <code>{prefix}addmf</code>\n{error_add_not_reply_or_args}')
            return
             
    @loader.command(
        ru_doc = '<ответ на сообщение/ID> - удалить человека из мут листа.',
        de_doc = '<antwort auf Nachricht/ID> - Entfernt den Benutzer aus dem stillen Blatt.'
    )
    async def rmmf(self, message):
        '''<reply to the message/ID> - remove the user from the mute list.'''
        args = utils.get_args_raw(message)
        mutelist = self.config['from_id']
        prefix = utils.escape_html(self.get_prefix())
        reply_user = await message.get_reply_message()
        us = self.strings['add_user_1']
        us2 = self.strings['remove_user']
        enu1 = self.strings['error_not_user_1']
        enu2 = self.strings['error_not_user_2']
        error_args_isdigit = self.strings['error_args_isdigit']
        ru = self.strings['remove_user']
        enraa = self.strings['error_add_not_reply_or_args']
        if args:
            if args.isdigit() == True:
                if args in mutelist:
                    self.config['from_id'].remove(args)
                    await utils.answer(message, f'{us} {args} {us2}')
                    return
                else:
                    await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error |</b> <code>{prefix}rmmf</code>\n{enu1} <code>{args}</code> {enu2}')
                    return
            else:
                await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error |</b> <code>{prefix}rmmf</code>\n{error_args_isdigit}')
        elif reply_user:
            user = reply_user.sender_id
            user_name = reply_user.sender.first_name
            if user in mutelist:
                self.config['from_id'].remove(user)
                await utils.answer(message, f'{us} {user_name} {ru}')
                return
            else:
                await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error |</b> <code>{prefix}rmmf</code>\n{enu1} <code>{user_name}</code> {enu2}')
                return
        else:
            await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error |</b> <code>{prefix}rmmf</code>\n{enraa}')

    @loader.command(
        ru_doc = '- список пользователей/ботов в мут листе.',
        de_doc = '- listet Benutzer/Bots in einem stillen Blatt auf.'
    )
    async def mflist(self, message):
        '''- the list of users/bots in the mutlist.'''
        mutelist = self.config['from_id']
        b = self.strings['blank']
        nb = self.strings['no_blank']
        if not len(mutelist):
            await utils.answer(message, b)
            return
        else:
            mutelisttxt = ' | '.join(map(str, mutelist))
            await utils.answer(message, f'<emoji document_id=5188666899860298925>🌒</emoji> {nb}\n\n{mutelisttxt}')
            return