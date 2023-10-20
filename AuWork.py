#—————————————————————————————————————————————————————————————————————————————————
#  █▀ █ █ ▀▄▀   █▀▄▀█ █▀█ █▀▄ █ █ █   █▀▀ █▀ Chanel: https://t.me/shx_modules
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
from ..inline.types import InlineCall

_version_ = (1, 1, 0)

class AuWork(loader.Module):
    '''Модуль для автоматического /work в боте @good_biznesbot\nDeveloper: @shx_modules'''
    strings = {
        'name':'AuWork'
    }

    async def client_ready(self):
        
        
                
            self.set('status', False) if self.get('status') == None else None
            self.set('groups', []) if self.get('groups') is None else None
            self.set('time', 2) if self.get('time') is None else None
            
            if self.get('module_start') == None:
                self.set('module_start', 1)
                await self.module_start_1()



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
            await utils.answer(message, f'<emoji document_id=5332533929020761310>✅</emoji> | AuWork включен.')
            return
        
    @loader.command()
    async def worktime(self, message):
        '''- установить промежуток времени между отправкой /work в каждый чат\nПо дефолту: 2 секунды'''
        args = utils.get_args_raw(message)
        if not args:
            await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error</b> | <code>{inspect.currentframe().f_code.co_name}</code>\nВведите промежуток времени между отправкой /work в каждый чат\nПо дефолту: 2 секунды')
            return
        else:
            time = int(args)
            self.set('time', time)
            await utils.answer(message, f'<emoji document_id=5332533929020761310>✅</emoji> | Новый промежуток времени между отправкой /work в каждый чат: <code>{time}</code> установлен')
            return
        
    @loader.loop(autostart=True, interval = 3600)
    async def work(self):
        status = self.get('status')
        if status == True:
            groups = self.get('groups')
            time = self.get('time')
            for group in groups:
                await self.client.send_message(group, '/work')
                await asyncio.sleep(time)

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
                    
                    
                      

                         
