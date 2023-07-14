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
from ..inline.types import InlineCall, InlineQuery
from telethon.tl.types import Message, ChatAdminRights
from telethon import functions
import asyncio
from asyncio import sleep

__version__ = (1, 0, 0)

@loader.tds
class lvlUP(loader.Module):
    '''Модуль для inline улучшения чего-либо в MineEVO\nDeveloper: @shx_modules'''
    strings = {
        'name':'lvlUP',
        'fc_integrate':'Интегрировать ли в модуль FastCommands?'
    }
    tempdb = '0'

    async def client_ready(self):
        self._backup_channel, _ = await utils.asset_channel(
            self._client,
            "lvlUP - group",
            "Группа для работы модуля lvlUP от @Shx_modules\nНе добавляйте сюда других людей или ботов!",
            silent=True,
            archive=True,
        )
        await self.client(functions.channels.InviteToChannelRequest(self._backup_channel, ['@mine_evo_bot']))
        await self.client(functions.channels.EditAdminRequest(
                channel=self._backup_channel,
                user_id="@mine_evo_bot",
                admin_rights=ChatAdminRights(ban_users=True, post_messages=True, edit_messages=True),
                rank="lvlUP",
            )
        )


    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "fc_integrate", False,
                lambda: self.strings("fc_integrate"),
                validator=loader.validators.Boolean()
            ),
        )

    @loader.watcher()
    async def watcher_check(self, message):
        if message.raw_text == '/checklvlup':
            if message.from_id == 5195118663:
                await self.client.send_message(message.to_id, 'evo')

    @loader.watcher(out = True)
    async def watcher_integration(self, message):
        if message.raw_text == '.integration':
            self.config['fc_integrate'] = not self.config['fc_integrate']
            st = self.config['fc_integrate']
            if st == True:
                await utils.answer(message, '<emoji document_id=5204044038126182496>✅</emoji> Интеграция FastCommands включена.'
            elif st == False:
                await utils.answer(message, '<emoji document_id=5206595394728894920>❌</emoji> Интеграция FastCommands отключена.'

    @loader.command(
        ru_doc = '[ Улучшение:str ] - открыть улучшение чего либо',
        de_doc = '[ Verbesserung:str ] - Entdecke die Verbesserung von etwas'
    )
    async def up(self, message):
        '''[ Improvement:str ] - open an improvement of something'''
        args = utils.get_args_raw(message)
        self.tempdb = args
        prefix = utils.escape_html(self.get_prefix())
        st = self.config['fc_integrate']
        uplist = ['Ур', 'ур', 'Мщ', 'мщ', 'Уд', 'уд', 'Урон', 'урон', 'Крит', 'крит', 'Шп', 'шп', 'Уп', 'уп', 'Шк', 'шк', 'Мр', 'мр', 'Мп', 'мп', 'Мэ', 'мэ', 'Му', 'му', 'Зс', 'зс']
        fcuplist = ['%мб','%бб','%нс','%вм','%мс',]
        if args in uplist:
            await utils.answer(message, '<emoji document_id=5204044038126182496>✅</emoji> Выполняется...')
            async with self.client.conversation(self._backup_channel) as conv:
                await conv.send_message(f'{args}')
                res = await conv.get_response()
                await self.inline.form(
                    text = res.text,
                    message=message,
                    reply_markup=[
                        [
                            {
                                "text": "🆙 Повысить!",
                                "callback": self.lvlup,
                            }
                        ],
                    ]
                )
        elif args in fcuplist:
            if st == True:
                fc = {
                    '%мб':'💥 Мощь бура',
                    '%бб':"🛢 Бак бура",
                    '%нс':"🗼 Насосы",
                    '%вм':"🚛 Вместимость",
                    '%мс':"🏜 Месторождение"
                }
                for key, value in fc.items():
                    if args == key:
                        args = value
                        self.tempdb = args
                        async with self.client.conversation(self._backup_channel) as conv:
                            await conv.send_message(f'{args}')
                            res = await conv.get_response()
                            await self.inline.form(
                                text = res.text,
                                message=message,
                                reply_markup=[
                                    [
                                        {
                                            "text": "🆙 Повысить!",
                                            "callback": self.lvlup,
                                        }
                                    ],
                                ]
                            )
                        break
            else:
                await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error |</b> <code>{prefix}up</code>\nИнтеграция FastCommands отключена. Чтобы включить введите <code>.integration</code>')
        elif not args:
            await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error |</b> <code>{prefix}up</code>\nВы не ввели, что хотите улучшить\nПопробуйте <code>{prefix}up ур</code>')
        else:
            await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error |</b> <code>{prefix}up</code>\nУлучшение <code>{args}</code> не найдено')
            
                


    async def lvlup(self, call: InlineCall):
        args = self.tempdb
        async with self.client.conversation(self._backup_channel) as conv:
            await conv.send_message(f'{args}')
            res = await conv.get_response()
            await res.click(0)
            await asyncio.sleep(0.5)
        async with self.client.conversation(self._backup_channel) as conv:
            await conv.send_message(f'{args}')
            res = await conv.get_response()
        txt = res.text
        await call.edit(
            text=txt,
            reply_markup=[
                    [
                        {
                            "text": "🆙 Повысить!",
                            "callback": self.lvlup,
                        }
                    ],
            ]
        )

    @loader.command(
        ru_doc = '- список быстрых команд для интеграции',
        de_doc = '- liste der Schnellbefehle für die Integration'
    )
    async def fch(self, message):
        ''' - list of quick commands for integration'''
        st = self.config['fc_integrate']
        prefix = utils.escape_html(self.get_prefix())
        if st == True: 
            await utils.answer(message, f'<emoji document_id=5773781976905421370>💼</emoji> <b>Список быстрых команд:</b> \n<code>{prefix}up %мб</code> - 💥 Мощь бура\n<code>{prefix}up %бб</code> - 🛢 Бак бура\n<code>{prefix}up %нс</code> - 🗼 Насосы\n<code>{prefix}up %вм</code> - 🚛 Вместимость\n<code>{prefix}up %мс</code> - 🏜 Месторождение')
        else:
             await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error |</b> <code>{prefix}up</code>\nИнтеграция FastCommands отключена. Чтобы включить введите <code>.integration</code>')
