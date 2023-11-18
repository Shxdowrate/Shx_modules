#—————————————————————————————————————————————————————————————————————————————————
#  █▀ █ █ ▀▄▀   █▀▄▀█ █▀█ █▀▄ █ █ █   █▀▀ █▀ Chanel: https://t.me/mescr_m
#  ▄█ █▀█ █ █   █ ▀ █ █▄█ █▄▀ █▄█ █▄▄ ██▄ ▄█ Not Licensed
#—————————————————————————————————————————————————————————————————————————————————
# Idea:
# meta developer: @mescr_m
# Thanks: 
#—————————————————————————————————————————————————————————————————————————————————

from .. import loader, utils
import asyncio
from asyncio import sleep
import inspect
from ..inline.types import InlineCall

__version__ = (1, 2, ' Cycle Update')

class AuWork(loader.Module):
    '''Модуль для автоматического /work в боте @good_biznesbot\nDeveloper: @mescr_m'''
    strings = {
        'name':'AuWork',
        'time':'Переодичность отправки "Работа" между чатами.\nУказывайте в секундах.',
        'dtime':'Переодичность работы. Указывайте в минутах',
        'autostart':'Запускать ли модуль автоматически после загрузки юзербота?',
        'autodelete':'Удалять ли автоматически чат, если бот не смог отправить в него сообщение?'
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "time", 3,
                lambda: self.strings("time"),
                validator=loader.validators.Integer()
            ),
            loader.ConfigValue(
                "dtime", 70,
                lambda: self.strings("dtime"),
                validator=loader.validators.Integer(minimum = 60)
            ),
            loader.ConfigValue(
                "autostart", False,
                lambda: self.strings("autostart"),
                validator=loader.validators.Boolean()
            ),
            loader.ConfigValue(
                "autodelete", True,
                lambda: self.strings("autodelete"),
                validator=loader.validators.Boolean()
            ),
        )

    async def client_ready(self):
            self.set('status', False) if self.get('status') == None else None
            self.set('groups', []) if self.get('groups') is None else None
            if self.get('module_start') == None:
                self.set('module_start', 1)
                await self.module_start_1()
            if self.config['autostaart'] == True:
                if self.get('status') == True:
                    await self.work()
            else:
                self.set('status', False)
                self.set('fact_status', False)  

    async def module_start_1(self):
        zxc = await self.client.send_message('me', f'🌘 | AuWorkStart...')
        await self.inline.form(
            text = 'Спасибо за загрузку модуля AuWork. Давайте пройдемся по основам модуля?',
            message=zxc,
            reply_markup=[
                [
                    {
                        "text": "⚡ Начать",
                        "callback": self.cmd_status,
                    },
                ],
                [
                    {
                        "text": "❌ Нет",
                        "action": 'close',
                    },
                ],
            ],
        )

    @loader.command()
    async def workgroup(self, message):
        '''[ ID группы / ничего ] - добавить/удалить группу для работы'''
        error_cmd = f'{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}'
        args = utils.get_args_raw(message)
        if args:
            if args[:1] == '-':
                if args[1:].isdigit():
                    group = int(args)
                    groups = self.get('groups')
                    try:
                        group_info = await self.client.get_entity(group)
                        groupname = group_info.title
                    except Exception:
                        groupname = '[ <u>GroupTitleError</u> ]'
                    if group not in groups:
                        self.get('groups').append(group)
                        await utils.answer(message, f'<emoji document_id=5332533929020761310>✅</emoji> | Группа <u>{groupname}</u> (<code>{group}</code>) успешно добавлена в AuWork.')
                        return
                    else:
                        self.get('groups').remove(group)
                        await utils.answer(message, f'<emoji document_id=5332533929020761310>✅</emoji> | Группа <u>{groupname}</u> (<code>{group}</code>) успешно удалена из AuWork.')
                        return
                else:
                    await utils.asnwer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error</b> | <code>{error_cmd}</code>\nВ ID групп не может быть ничего, кроме цифр.')
                    return
            else:
                await utils.asnwer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error</b> | <code>{error_cmd}</code>\nID групп всегда начинается с <code>-</code>.')
                return
        else:
            if message.is_private != True:
                group = message.chat_id
                try:
                    group_info = await self.client.get_entity(group)
                    groupname = group_info.title
                except Exception:
                    groupname = '[ <u>GroupTitleError</u> ]'
                groups = self.get('groups')
                if group not in groups:
                    self.get('groups').append(group)
                    await utils.answer(message, f'<emoji document_id=5332533929020761310>✅</emoji> | Группа <u>{groupname}</u> (<code>{group}</code>) успешно добавлена в AuWork.')
                    return
                else:
                    self.get('groups').remove(group)
                    await utils.answer(message, f'<emoji document_id=5332533929020761310>✅</emoji> | Группа <u>{groupname}</u> (<code>{group}</code>) успешно удалена из AutWork.')
                    return
            else:
                await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error</b> | <code>{error_cmd}</code>\nДля работы могут подойти только группы.')
                return
            
    @loader.command()
    async def auwork(self, message):
        '''- выключить/выключить AuWork'''
        if self.get('status') == True:
            self.set('status', False)
            await utils.answer(message, f'<emoji document_id=5332533929020761310>✅</emoji> | AuWork выключен.')
            return
        else:
            self.set('status', True)
            txt = f'<emoji document_id=5332533929020761310>✅</emoji> | AuWork включен.'
            if self.get('fact_status') == False:
                txt += f'\n<emoji document_id=5327790373865530387>🔗</emoji> | Цикл перезапущен.'
            await utils.answer(message, txt)
            if self.get('fact_status') == False:
                await self.work()
            return
        
    async def work(self):
        while True:
            await asyncio.sleep(0.5)
            if self.get('status') == True:
                self.set('fact_status', True)
                groups = self.get('groups')
                time = self.config['time']
                dtime = self.config['dtime'] * 60
                for group in groups:
                    try:
                        await self.client.send_message(group, 'Работа')
                    except Exception:
                        txt = f'<emoji document_id=5393507664166660007>⛓</emoji> | Ваш юзербот не смог поработать в группе ID:<code>{group}</code>, вероятно, Вас там заблокировали или выдали мут.'
                        if self.config['autodelete']:
                            self.get('groups').remove(group)
                            txt += '\n\n<emoji document_id=5444961247818691184>🧡</emoji> | Эта группа была автоматически вынесена из списка групп для работы.'
                        await self.client.send_message('me', txt)
                    finally:
                        await asyncio.sleep(time)
                await asyncio.sleep(dtime)
            else:
                self.set('fact_status', False)
                break

    @loader.command()
    async def workgroups(self, message):
        '''- посмотреть группы AuWork'''
        await utils.answer(message, '<emoji document_id=5307773751796964107>⏳</emoji> | Загрузка информации...')
        groups = self.get('groups')
        num = 0
        txt = ''
        for group in groups:
            try:
                group_info = await self.client.get_entity(group)
                groupname = group_info.title
            except Exception:
                groupname = '[ <u>GroupTitleError</u> ]'
            num += 1
            txt += f'{num} | {groupname} (<code>{group}</code>)\n'
        await utils.answer(message, f'<emoji document_id=5936283232780684228>👥</emoji> | Группы AuWork:\n{txt}')

    async def cmd_status(self,  call: InlineCall):
        await call.answer('1/3 страница.')
        txt = 'Хорошо, начнем с основной команды: <code>.auwork</code>, с помощью этой команды вы сможете включать и отключать модуль.'
        await call.edit(
            text=txt,
            reply_markup=[
                [
                    {
                        "text": "⚡ Продолжить",
                        "callback": self.cmd_group,
                    },
                ],
                [
                    {
                        "text": "❌ Закончить",
                        "action": 'close',
                    },
                ]
            ]
        )

    async def cmd_group(self,  call: InlineCall):
        await call.answer('2/3 страница.')
        time = self.get('time')
        txt = f'Следущая команда: <code>.workgroup</code>, с помощью этой команды вы сможете добавлять и удалять группы модуля. В добавленные группы модуль будет автоматически отправлять каждый час сообщение "/work", после отправки сообщения в одну группу, бот подождет <code>{time}</code> сек, а после отправит сообщение в следующую группу.\nДобавлять и удалять группы можно несколькими способами:\n\n<b><u>Способ 1</u></b>:\nНапишите команду непосредственно в ту группу, которую хотите добавить/удалить.\n\n<b><u>Способ 2:</u></b>\nИспользуйте в качестве аргумента ID группы, которую хотите добавить/удалить, но помните, ID всех групп начинаются с <code>-</code>.'
        await call.edit(
            text=txt,
            reply_markup=[
                [
                    {
                        "text": "⚡ Продолжить",
                        "callback": self.cmd_time,
                    },
                ],
                [
                    {
                        "text": "❌ Закончить",
                        "action": 'close',
                    },
                ]
            ]
        )

    async def cmd_time(self,  call: InlineCall):
        await call.answer('3/3 страница.')
        time = self.get('time')
        txt = f'Следущая команда: <code>.worktime</code>. Сейчас промежуток времени между отправкой /work в каждую группу: <code>{time}</code>, то есть, отправив <code>/work</code> в одну группу, бот подождет <code>{time}</code> сек, а после отправит команду в следующую группу.'
        await call.edit(
            text=txt,
            reply_markup=[
                [
                    {
                        "text": "⚡ Закончить",
                        'action':'close',
                    },
                ],
            ]
        )
