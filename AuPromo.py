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
import random
import asyncio 
from asyncio import sleep
from ..inline.types import InlineCall
import inspect

__version__ = (1, 2, 0)

class AuPromo(loader.Module):
    '''Модуль для создания пользовательских промо MineEVO\nDeveloper: @shx_modules'''
    strings = {
        'name':'AuPromo'
    }
    tempdb = 0

    async def client_ready(self, client, db):
        self.client = client
        self.db = db
        a = self.get( 'status')
        if a == None:
            self.set( 'status', True)
        self.set( 'sender', [])
        a = self.get( 'blacklist')
        if a == None:
            self.set( 'blacklist', [1296168600, 6695502991])
        a = self.get( 'sleep')
        if a == None:
            self.set( 'sleep', 30)
        a = self.get('senderss')
        if a == None:
            self.set('senderss', [])
        
        
        

    @loader.watcher(only_messages = True)
    async def watcher(self, message):
        sq = self.get( 'status') 
        senn = message.sender_id 
        if sq == True:

            group = self.get( 'group')
            if message.chat_id == group:
                prm = self.get( 'promo')
                pref = message.raw_text.split()[0]

                if pref == '#промо':
                    promo = message.raw_text.split()[1]
                    blacklist = self.get( 'blacklist')

                    if senn in blacklist:
                        return
                    
                    else:

                        if promo == prm:
                            acti = self.get( 'activators')
                            activ = self.get( 'activ')

                            if activ < acti:
                                sender = self.get( 'sender')

                                if message.from_id in sender:
                                    await message.reply('<emoji document_id=5210952531676504517>🚫</emoji> Вы уже активировали этот промокод.')
                                    return
                                
                                else:

                                    sleepc = self.get( 'sleep')
                                    sleep = random.randint(1, sleepc)
                                    qq = self.get( 'qq')
                                    stplus = activ + 1
                                    self.set( 'activ', stplus)
                                    await message.reply(f'<emoji document_id=5332533929020761310>✅</emoji> Промокод <code>{prm}</code> успешно активирован. Награда будет выдана через {sleep} секунд.')
                                    sender.append(senn)
                                    senderss = self.get('senderss')
                                    senderss.append(message.sender.first_name)
                                    self.set('senderss', senderss)
                                    self.set('sender', sender)
                                    await asyncio.sleep(sleep)
                                    await message.reply(f'Дать {qq}')
                                    return
                                
                            else:

                                await message.reply(f'<emoji document_id=5981043230160981261>⏱</emoji> <b>К сожалению, промо больше не действителен, так как его уже активировало {activ}/{acti} человек.</b>')
                                return
    @loader.command()
    async def np(self, message):
        '''[ Новый промо ( без пробелов ) ] [ Кол-во активаций:int ] [ Награда за ввод промо ] [ Кол-во кейсов:int ] - создать промокод'''
        args = utils.get_args_raw(message)
        error_cmd = f'{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}'
        if args:
            if ' ' in args:
                args = args.split(' ')
                if len(args) == 4:
                    if args[1].isdigit():
                        args_1 = int(args[1])
                        if args_1 > 0:
                            args[2].lower()
                            if args[2] in ['кт','ркт','к','рк','миф','кр','зв']:
                                if args[3].isdigit():
                                    args_3 = int(args[3])
                                    if args_3 > 0:
                                        newpromo = args[0]
                                        act = args[1]
                                        act = int(act)
                                        one = args[2]
                                        two = args[3]
                                        qq = f'{one} {two}'
                                        self.set( 'promo', newpromo)
                                        self.set( 'activators', act)
                                        self.set( 'activ', 0)
                                        self.set( 'qq', qq)
                                        self.set( 'sender', [])
                                        self.set('senderss', [])
                                        await utils.answer(message, f'<emoji document_id=5332533929020761310>✅</emoji> | Промокод <code>{newpromo}</code> на <code>{act}</code> активаций создан. Активировать: <code>#промо {newpromo}</code>\nНаграда: {qq}.')
                                        return
                                    else:
                                        await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error</b> | {error_cmd}\nВы ввели в кол-во кейсов {args[3]}, хотя разрешено только больше нуля.')
                                        return
                                else:
                                    await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error</b> | {error_cmd}\nВы ввели {args[3]} в кол-во кейсов, хотя разрешены только целочисленные значения.')
                                    return
                            else:
                                await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error</b> | {error_cmd}\nВашей наградой стало {args[2]}, хотя должно быть что-то из этого списка: <code>кт, ркт, к, рк, миф, кр, зв</code>.')
                                return
                        else:
                            await utils.asnwer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error</b> | {error_cmd}\nВы ввели {args[1]} активаций, хотя разрешено не меньше нуля.')    
                            return
                    else:
                        await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error</b> | {error_cmd}\nВы ввели {args[1]} активаций, хотя разрешены только целочисленные значения.')
                        return
                else:
                    await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error</b> | {error_cmd}\nВы ввели больше или меньше аргументов, чем нужно.')
                    return
            else:
                await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error</b> | {error_cmd}\nВы ввели только один аргумент, хотя необходимо четыре.')
                return
        else:
            await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error</b> | {error_cmd}\nВы не ввели аргументов.')
            return
        
                

    @loader.command()
    async def pst(self, message):
        ''' - включить / отключить промокоды'''
        a = self.get( 'status')
        if a == True:
            self.set( 'status', False)
            await utils.answer(message, f'<emoji document_id=5332533929020761310>✅</emoji> | Промокоды отключены.')
            return
        else:
            self.set( 'status', True)
            await utils.answer(message, f'<emoji document_id=5332533929020761310>✅</emoji> | Промокоды включены.')
            return
        
    @loader.command()
    async def setgroup(self, message):
        ''' - установить чат для промо'''
        error_cmd = f'<code>{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}</code>'
        if message.is_private:
            await message.edit(f"<emoji document_id=5877477244938489129>🚫</emoji> <b>Error</b> | {error_cmd}\nЭто не группа.")
            return
        args = utils.get_args_raw(message)
        to_chat = None

        try:
            if args:
                to_chat = int(args) if args.isdigit() else args
            else:
                to_chat = message.chat_id
        except ValueError:
            to_chat = message.chat_id
        chat = await message.client.get_entity(to_chat)
        chat = f'-100{chat.id}'
        chat = int(chat)
        self.set( 'group', chat)
        await message.edit(f"<emoji document_id=5332533929020761310>✅</emoji> | Группа <code>{chat}</code> установлена, как чат для промо.")

    @loader.command()
    async def stp(self, message):
        ''' - посмотреть статистику текущего промокода'''
        activ_human = self.get( 'activators')
        activ_d = self.get( 'activ')
        if activ_human == activ_d:
            st_promo = 'Истек'
        else:
            st_promo = 'Активен'
        qq = self.get( 'qq')
        group = self.get( 'group')
        promo = self.get( 'promo')
        senderss = self.get('senderss')
        senderss = '\n'.join(map(str, senderss))
        text_on_top = f'<emoji document_id=5373001317042101552>📈</emoji> <b>Статистика промокода</b> <code>{promo}</code><b>:</b>\n\n'
        promo_text = f'<emoji document_id=5978608481920355849>🎁</emoji> | <b>Промо:</b> <code>{promo}</code>\n'
        command_activate = f'<emoji document_id=5431376038628171216>💻</emoji> | <b>Команда активации:</b> <code>#промо {promo}</code>\n'
        st_promo_text = f'<emoji document_id=5328239124933515868>⚙️</emoji> | <b>Состояние промо:</b> <code>{st_promo}</code>\n'
        all_act = f'<emoji document_id=5328239124933515868>⚙️</emoji> | <b>Лимит активаций:</b> <code>{activ_human}</code>\n'
        act = f'<emoji document_id=5328239124933515868>⚙️</emoji> | <b>Уже активировано:</b> <code>{activ_d}</code>\n'
        group = f'<emoji document_id=5821388137443626414>🌐</emoji> | <b>Группа для активации:</b> <code>{group}</code>\n'
        qq = f'<emoji document_id=5436040291507247633>🎉</emoji> | <b>Награда:</b> <code>{qq}</code>\n'
        txt_senderss = f'<emoji document_id=5773781976905421370>💼</emoji> | <b>Активировали промокод:</b>\n{senderss}'
        
        await utils.answer(message, text_on_top + promo_text + command_activate + all_act + act + st_promo_text + group + qq + txt_senderss)

    @loader.command()
    async def padd(self, message):
        '''[ Кол-во:int ] - добавить кол-во максимальных активаций'''
        act = self.get( 'activators')
        error_cmd = f'<code>{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}</code>'
        args = utils.get_args_raw(message)
        if args:
            if args.isdigit():
                args = int(args)
                if args > 0:
                    act = act + args
                    self.set( 'activators', act)
                    await utils.answer(message, f'<emoji document_id=5332533929020761310>✅</emoji> | Кол-во максимальных активаций увеличено на <code>{args}</code>.\nНовый лимит активаций: <code>{act}</code>.')
                    return
                else:
                    await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error</b> | {error_cmd}\nВы ввели {args}, хотя можно добавлять только больше нуля.')
                    return
            else:
                await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error</b> | {error_cmd}\nВы ввели {args}, хотя команда поддерживает только целочисленные значения.')
                return
        else:
            await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error</b> | {error_cmd}\nВы не указали, сколько хотите добавить активаций.')
            return

    @loader.command()
    async def pdel(self, message):
        '''[ Кол-во:int ] - уменьшить кол-во максимальных активаций'''
        act = self.get( 'activators')
        error_cmd = f'<code>{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}</code>'
        args = utils.get_args_raw(message)
        if args:
            if args.isdigit():
                args = int(args)
                if args > 0:
                    act = act - args
                    self.set( 'activators', act)
                    await utils.answer(message, f'<emoji document_id=5332533929020761310>✅</emoji> | Кол-во максимальных активаций уменьшено на <code>{args}</code>.\nНовый лимит активаций: <code>{act}</code>.')
                    return
                else:
                    await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error</b> | {error_cmd}\nВы ввели {args}, хотя можно уменьшать только больше нуля.')
                    return
            else:
                await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error</b> | {error_cmd}\nВы ввели {args}, хотя команда поддерживает только целочисленные значения.')
                return
        else:
            await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error</b> | {error_cmd}\nВы не указали, сколько хотите удалить активаций.')
            return
        
    @loader.command()
    async def pconf(self, message):
        ''' < ответ на сообщение пользователя > - действия с пользователем'''
        user = await message.get_reply_message()
        error_cmd = f'<code>{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}</code>'
        if user != None:
            user = int(user.sender_id)
            if user in [5195118663, 6695502991]:
                await utils.answer(message, f'С этим пользователем заблокированы взаимодействия.')
                return
            user_sender = self.get( 'sender')
            self.tempdb = user
            if user in user_sender:
                us = '🟡 Пользователь активировал ваш промокод.\n'
            else:
                us = ''
            black_list = self.get( 'blacklist')
            if user in black_list:
                ub = '🔴 Пользователь в черном списке промо.'
            else:
                ub = '🟢 Пользователь не в черном списке промо.'

            await self.inline.form(
                text = f'<b>Действия с пользователем ID {user}:</b>\n\n{us}{ub}',
                message=message,
                reply_markup=[
                    [
                        {
                            'text':'🔴 Добавить в ЧС',
                            'callback':self.ban_user,
                        },
                        {
                            'text':'🟢 Вынести из ЧС',
                            'callback':self.unban_user,
                        }
                    ],
                    [
                        {
                            'text':'🟡 Имитировать активацию промо',
                            'callback':self.fact_promo,
                        }
                    ],
                    [
                        {
                            'text':'🟡 Снять активацию промо',
                            'callback':self.fnoact_promo,
                        }
                    ]
                ],
            )
            return
        else:
            await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error</b> | {error_cmd}\nВы не ответили на сообщение пользователя, с которым хотите взаимодействовать.')

    async def ban_user(self, call: InlineCall):
        user = self.tempdb
        blacklist = self.get( 'blacklist')
        blacklist.append(user)
        self.set( 'blacklist', blacklist)
        await call.edit(
            text='<b>Пользователь добавлен в черный список промо.</b>',
            )
    
    async def unban_user(self, call: InlineCall):
        user = self.tempdb
        blacklist = self.get( 'blacklist')
        blacklist.remove(user)
        self.set( 'blacklist', blacklist)
        await call.edit(
            text='<b>Пользователь вынесен из черного списка промо.</b>',
            )
            
    async def fact_promo(self, call: InlineCall):
        user = self.tempdb
        sender = self.get( 'sender')
        sender.append(user)
        self.set( 'sender', sender)
        await call.edit(
            text='<b>Теперь пользователь "активировал" промо и больше не сможет этого сделать.</b>',
            )
        
    async def fnoact_promo(self, call: InlineCall):
        user = self.tempdb
        sender = self.get( 'sender')
        sender.remove(user)
        self.set( 'sender', sender)
        await call.edit(
            text='<b>Теперь пользователь "не активировал" промо и сможет сделать это снова.</b>',
            )
        
    @loader.command()
    async def psleep(self, message):
        '''[ Значение:int / ничего ] - выставить период выдачи приза с промо. По дефолту стоит 1-30 секунд'''
        args = utils.get_args_raw(message)
        error_cmd = f'<code>{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}</code>'
        sleep = self.get( 'sleep')
        if args:
            if args.isdigit():
                args = int(args)
                if args > 2:
                    self.set( 'sleep', args)
                    await utils.answer(message, f'<emoji document_id=5332533929020761310>✅</emoji> | Ваш период задержки был изменен на 1-{args}')
                    return
                else:
                    await utils.asnwer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error</b> | {error_cmd}\nВы указали {args}, хотя минимальное значение для периода: <code>2</code>.')
                    return
            else:
                await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error</b> | {error_cmd}\nВы указали {args}, хотя значение может быть только целочисленным.')
                return
        else:
            await utils.answer(message, f'<emoji document_id=5217882379804221460>💤</emoji> | Ваш текущий период задержки: 1-{sleep}')
            return
        
    @loader.command()
    async def pbl(self, message):
        ''' - вывести черный список промо'''
        a = self.get( 'blacklist')
        if not a:
            await utils.answer(message, f'⚫ Черный список пуст.')
            return
        else:
            bl = ' | '.join(map(str, a))
            await utils.answer(message, f'⚫ Список заблокированных в промо людей:\n{bl}')