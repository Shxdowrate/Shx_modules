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
# v1.1.0 - @Kepperok | Помощь в обнаружении проблемы базы данных
#—————————————————————————————————————————————————————————————————————————————————

from .. import loader, utils
import random
import asyncio 
from asyncio import sleep
from ..inline.types import InlineCall
import inspect

__version__ = (1, 2, 2)

class EvoPromo(loader.Module):
    '''Модуль для создания пользовательских промо MineEVO\nDeveloper: @shx_modules'''
    strings = {
        'name':'EvoPromo'
    }
    tempdb = 0

    async def client_ready(self, client, db):
        self.client = client
        self.db = db

        a = self.get( 'status') # Настраиваем статус модуля
        if a == None:
            self.set( 'status', True)
        
        a = self.get('sender') # Настраиваем список для тех, кто активировал промо
        if a == None:
            self.set( 'sender', [])

        a = self.get( 'blacklist') # Настраиваем список черного листа
        if a == None:
            self.set( 'blacklist', [1296168600, 6695502991])

        a = self.get( 'sleep') # Настраиваем период выдачи награды
        if a == None:
            self.set('sleep', 30)

        a = self.get('wintext') # Настраиваем wintext
        if a == None:
            self.set('wintext',  '<emoji document_id=5332533929020761310>✅</emoji> Промокод <code>{prm}</code> успешно активирован. Награда будет выдана через {sleep} секунд.')

        a = self.get('losetext') # Настраиваем losetext
        if a == None:
            self.set('losetext',  '<emoji document_id=5210952531676504517>🚫</emoji> Вы уже активировали этот промокод.')

        a = self.get('timetext') # Настраиваем timetext
        if a == None:
            self.set('timetext',  '<emoji document_id=5981043230160981261>⏱</emoji> <b>К сожалению, промо больше не действителен, так как его уже активировало {activ}/{acti} человек.</b>')
        
        a = self.get('prefix')  # Настраиваем префикс
        if a == None:
            self.set('prefix', '#промо')

        a = self.get('promo_groups') # Настройка списка групп для промо
        if a is None:
            self.set('promo_groups', [])



        
        

    @loader.watcher(only_messages = True)
    async def watcher(self, message):
        sq = self.get('status') 
        senn = message.sender_id 

        if sq == True:
            groups = self.get('promo_groups')

            if message.chat_id in groups:
                
                if message.media:
                    return
                elif message.file:
                    return
                elif message.sticker:
                    return
                prm = self.get( 'promo')
                pref = message.raw_text.split()[0]
                ppref = self.get('prefix')
                if pref == ppref:
                    if ' ' in message.raw_text:
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
                                    wintext = self.get('wintext')
                                    losetext = self.get('losetext')
                                    



                                    if message.from_id in sender:
                                        await message.reply(losetext.format(acti=acti, activ=activ, promo=promo, prm=prm)) # Уже активировал
                                        return
                                    
                                    else:
                                        sleepc = self.get( 'sleep')
                                        sleep = random.randint(1, sleepc)
                                        reward = self.get('reward')
                                        stplus = activ + 1
                                        self.set( 'activ', stplus)
                                        await message.reply(wintext.format(prm=prm, sleep=sleep, promo=promo, acti=acti, activ=activ)) # Промокод активирован
                                        sender.append(senn)
                                        
                                        self.set('sender', sender)
                                        await asyncio.sleep(sleep)
                                        a = await self.client.get_entity(message.from_id)
                                        await message.reply(f'{reward}')
                                        return
                                    
                                else:
                                    timetext = self.get('timetext')
                                    await message.reply(timetext.format(prm=prm, promo=promo, acti=acti, activ=activ)) # Достигнут лимит активаций
                                    return
    @loader.command(alias = 'pnp')
    async def promonewpromo(self, message):
        '''[ Новый промо ( без пробелов ) ] [ Кол-во активаций:int ] [ Тип промо: cases / credits ] [ Награда за ввод промо(кейс) / кол-во кредитов ] [ Кол-во кейсов:int / ничего ] - создать промокод'''
        await utils.answer(message, f'<emoji document_id=5307773751796964107>⏳</emoji> | Загрузка информации...')
        args = utils.get_args_raw(message)
        error_cmd = f'{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}'
        pr_cases = ['кт','ркт','к','рк','миф','кр','дк','зв']
        
        
        if args: # Если есть аргументы

            if ' ' in args: # Проверка, если аргумент не один
                args = args.split(' ')

                if len(args) == 5: # Проверка на кол-во аргументов
                    promo = args[0] # - Промокод

                    if args[1].isdigit(): # Проверка, является ли кол-во активаций целочисленным
                        act_limit = int(args[1]) # - Лимит активаций

                        if act_limit > 0:

                            if args[2] == 'cases': # Если наградой станут кейсы

                                if args[3].lower() in pr_cases: # Проверка, есть ли кейс в списке кейсов MineEVO
                                    case = args[3] # - тип кейса

                                    if args[4].isdigit(): # Проверка, является ли кол-во кейсов целочисленным
                                        num_cases = int(args[4]) # - Кол-во кейсов

                                        if num_cases > 0:

                                            # Выставление дефолтный значение бд
                                            self.set('sender', [])
                                            self.set('activ', 0)

                                            # Выставление новых зачений
                                            self.set('promo', promo)
                                            self.set('activators', act_limit)

                                            # Текст выдачи награды
                                            reward_text = f'Дать {case} {num_cases}'
                                            reward_for_stats = f'{num_cases} {case}'
                                            self.set('reward_stats', reward_for_stats)
                                            self.set('reward', reward_text)

                                            # Готово | Shx in your heart?
                                            text_1 = f'<emoji document_id=5332533929020761310>✅</emoji> | <b>Промокод</b> <code>{promo}</code> <b>успешно создан.</b>\n'
                                            text_2 = f'<emoji document_id=5818865088970362886>🚧</emoji> | <b>Кол-во активаций:</b> <code>{act_limit}</code>\n'
                                            text_3 = f'<emoji document_id=5472111548572900003>⌨️</emoji> | <b>Команда активации:</b> <code>{self.get("prefix")} {promo}</code>\n'
                                            text_4 = f'<emoji document_id=5472164874886846699>✨</emoji> | <b>Награда:</b> <code>{num_cases} {case}</code>'

                                            # Вывод
                                            await utils.answer(message, text_1 + text_2 + text_3 + text_4)
                                            return

                                            # Ошибки
                                        else:
                                            await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error</b> | <code>{error_cmd}</code>\nКол-во кейсов должно быть больше нуля.')
                                            return
                                        
                                    else:
                                        await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error</b> | <code>{error_cmd}</code>\nКол-во кейсов может быть только целочисленным значением.')
                                        return
                                    
                                else:
                                    await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error</b> | <code>{error_cmd}</code>\nКейса <code>{args[3].lower}</code> нет в MineEVO.')
                                    return
                                
                                
                            else:
                                await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error</b> | <code>{error_cmd}</code>\nНаграды типа <code>{args[2]}</code> не существует')
                                return
                            
                        else:
                            await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error</b> | <code>{error_cmd}</code>\nКол-во активаций должно быть больше нуля.')
                            return
                        
                    else:
                        await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error</b> | <code>{error_cmd}</code>\nЛимит активаций может быть только целочисленным значением.')
                        return
                    
                if len(args) == 4:
                    promo = args[0] # - Промокод

                    if args[1].isdigit(): # Проверка, является ли кол-во активаций целочисленным
                        act_limit = int(args[1]) # - Лимит активаций

                        if act_limit > 0:

                            if args[2] == 'credits': # Если наградой станут кредиты

                                if args[3].isdigit: # Проверка, является ли кол-во кредитов целочисленным значением.
                                    num_credits = int(args[3]) # - Кол-во кредитов

                                    if num_credits > 0: 
                                        
                                        # Выставление дефолтный значение бд
                                        self.set('sender', [])
                                        self.set('activ', 0)

                                        # Выставление новых зачений
                                        self.set('promo', promo)
                                        self.set('activators', act_limit)

                                        # Текст выдачи награды
                                        reward_text = f'Перечислить {num_credits}'
                                        self.set('reward', reward_text)
                                        reward_for_stats = f'{num_credits} кредитов'
                                        self.set('reward_stats', reward_for_stats)

                                        # Готово | Shx in your heart?
                                        text_1 = f'<emoji document_id=5332533929020761310>✅</emoji> | <b>Промокод</b> <code>{promo}</code> <b>успешно создан.</b>\n'
                                        text_2 = f'<emoji document_id=5818865088970362886>🚧</emoji> | <b>Кол-во активаций:</b> <code>{act_limit}</code>\n'
                                        text_3 = f'<emoji document_id=5472111548572900003>⌨️</emoji> | <b>Команда активации:</b> <code>{self.get("prefix")} {promo}</code>\n'
                                        text_4 = f'<emoji document_id=5472164874886846699>✨</emoji> | <b>Награда:</b> <code>{num_credits} кредитов</code>'

                                        # Вывод
                                        await utils.answer(message, text_1 + text_2 + text_3 + text_4)
                                        return

                                        # Ошибки
                                    else:
                                        await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error</b> | <code>{error_cmd}</code>\nКол-во кредитов должно быть больше нуля.')
                                        return
                                   
                                else:
                                    await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error</b> | <code>{error_cmd}</code>\nКол-во кредитов может быть целочисленным значением.')
                                    return
                                
                            else:
                                await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error</b> | <code>{error_cmd}</code>\nНаграды типа <code>{args[2]}</code> не существует.')
                                return
                            
                        else:
                            await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error</b> | <code>{error_cmd}</code>\nКол-во активаций должно быть больше нуля.')
                            return
                        
                    else:
                        await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error</b> | <code>{error_cmd}</code>\nЛимит активаций может быть только целочисленным значением.')
                        return
                    
                else:
                    await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error</b> | <code>{error_cmd}</code>\nВы ввели {len(args)} аргументов, хотя нужно 4 или 5.')
                    return
                
            else:
                await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error</b> | <code>{error_cmd}</code>\nВы ввели только один аргумент, хотя нужно 4 или 5.')
                return
            
        else:
            await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error</b> | <code>{error_cmd}</code>\nВы не ввели не одного аргумента, хотя нужно 4 или 5.')
            return



    @loader.command(alias = 'pst')
    async def promostatus(self, message):
        ''' - включить / отключить промокоды'''
        await utils.answer(message, f'<emoji document_id=5307773751796964107>⏳</emoji> | Загрузка информации...')
        a = self.get( 'status')

        if a == True:
            self.set( 'status', False)
            await utils.answer(message, f'<emoji document_id=5332533929020761310>✅</emoji> | Промокоды отключены.')
            return
        
        else:
            self.set( 'status', True)
            await utils.answer(message, f'<emoji document_id=5332533929020761310>✅</emoji> | Промокоды включены.')
            return
        
    @loader.command(alias = 'pg')
    async def promogroup(self, message):
        ''' [ only / ничего ] - добавить/удалить группу из списка групп для промо\nonly - чтобы удалить все группы, кроме той, в которой была прописана команда.'''
        await utils.answer(message, f'<emoji document_id=5307773751796964107>⏳</emoji> | Загрузка информации...')
        error_cmd = f'<code>{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}</code>'
        args = utils.get_args_raw(message)
        groups = self.get('promo_groups')
        
        if not args:

            if message.is_private == False:
                group = message.chat_id
                g_title = await self.client.get_entity(group)
                title = g_title.title

                if group in groups:
                    self.get('promo_groups').remove(group)
                    await utils.answer(message, f'<emoji document_id=5332533929020761310>✅</emoji> | Группа {title} (<code>{group}</code>) удалена из списка групп для промо.')
                    return
                
                else:
                    self.get('promo_groups').append(group)
                    await utils.answer(message, f'<emoji document_id=5332533929020761310>✅</emoji> | Группа {title} (<code>{group}</code>) добавлена в список групп для промо.')
                    return
                
            else:
                await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error</b> | <code>{error_cmd}</code>\nГруппой для промо не могут стать личные сообщения.')
                return
            
        else:
            
            if " " not in args:

                if args.lower() == 'only': 

                    if message.is_private == False:
                        group = message.chat_id
                        g_title = await self.client.get_entity(group)
                        title = g_title.title  
                        self.set('promo_groups', [])
                        self.get('promo_groups').append(group)
                        await utils.answer(message, f'<emoji document_id=5332533929020761310>✅</emoji> | Все группы для промо, кроме {title} (<code>{group}</code>), были удалены.')
                        return
                    
                    else:
                        await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error</b> | <code>{error_cmd}</code>\nГруппой не могут стать личные сообщения.')

                elif args[0] == '-':

                    if args[1:].isdigit():
                        group = int(args)
                        g_title = await self.client.get_entity(group)
                        title = g_title
                        if group in groups:
                            self.get('promo_groups').remove(group)
                            await utils.answer(message, f'<emoji document_id=5332533929020761310>✅</emoji> | Группа {title} (<code>{group}</code>) удалена из списка групп для промо.')
                            return
                        
                        else:
                            self.get('promo_groups').append(group)
                            await utils.answer(message, f'<emoji document_id=5332533929020761310>✅</emoji> | Группа {title} (<code>{group}</code>) добавлена в список групп для промо.')
                            return
                        
                    else:
                        await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error</b> | <code>{error_cmd}</code>\nID группы может быть только целочисленным после минуса.')
                        return
                    
                else:
                    await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error</b> | <code>{error_cmd}</code>\nID групп всегда начинается с -100.')
                    return
            
            else:
                await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error</b> | <code>{error_cmd}</code>\nЭта команда поодерживает либо нуль, либо только один аргумент - ID группы')
                    
            

    @loader.command(alias = 'psp')
    async def promostatisticpromo(self, message):
        ''' - посмотреть статистику текущего промокода'''
        await utils.answer(message, f'<emoji document_id=5307773751796964107>⏳</emoji> | Загрузка информации...')
        activ_human = self.get( 'activators')
        activ_d = self.get( 'activ')

        if activ_human == activ_d:
            st_promo = 'Истек'

        else:
            st_promo = 'Активен'

        reward = self.get('reward_stats')
        
        promo = self.get( 'promo')
        humans = self.get('sender')
        text_humans = ''
        sss = 0
        groups = self.get('promo_groups')
        for user in humans:
            try:
                user_nick = await self.client.get_entity(user)
                user_nick = user_nick.first_name
                sss += 1
                text_humans += f'{sss} | {user_nick} (<code>{user}</code>)\n'
            except Exception:
                sss += 1
                text_humans += f'{sss} | _error_nick_ (<code>{user}</code>)\n'
            

        pref = self.get('prefix') 
        text_on_top = f'<emoji document_id=5373001317042101552>📈</emoji> <b>Статистика промокода</b> <code>{promo}</code><b>:</b>\n\n'
        promo_text = f'<emoji document_id=5978608481920355849>🎁</emoji> | <b>Промо:</b> <code>{promo}</code>\n'
        pref_text = f'<emoji document_id=5431376038628171216>💻</emoji> | <b>Префикс:</b> <code>{pref}</code>\n'
        command_activate = f'<emoji document_id=5431376038628171216>💻</emoji> | <b>Команда активации:</b> <code>{pref} {promo}</code>\n'
        promo_groups = f'<emoji document_id=5936283232780684228>👥</emoji> | <b>Группы для активации промо:</b> <code>{utils.escape_html(self.get_prefix())}promogroups</code> (<code>{len(groups)}</code>)\n'
        st_promo_text = f'<emoji document_id=5328239124933515868>⚙️</emoji> | <b>Состояние промо:</b> <code>{st_promo}</code>\n'
        all_act = f'<emoji document_id=5328239124933515868>⚙️</emoji> | <b>Лимит активаций:</b> <code>{activ_human}</code>\n'
        act = f'<emoji document_id=5328239124933515868>⚙️</emoji> | <b>Уже активировано:</b> <code>{activ_d}</code>\n'
        qq = f'<emoji document_id=5436040291507247633>🎉</emoji> | <b>Награда:</b> <code>{reward}</code>\n'
        txt_senderss = f'<emoji document_id=5773781976905421370>💼</emoji> | <b>Активировали промокод:</b>\n{text_humans}'
        
        await utils.answer(message, f'{text_on_top}{promo_text}{pref_text}{command_activate}{promo_groups}{all_act}{act}{st_promo_text}{qq}{txt_senderss}')

    @loader.command(alias = 'padd')
    async def promoadd(self, message):
        '''[ Кол-во:int ] - добавить кол-во максимальных активаций'''
        await utils.answer(message, f'<emoji document_id=5307773751796964107>⏳</emoji> | Загрузка информации...')
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
                    await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error</b> | <code>{error_cmd}</code>\nВы ввели {args}, хотя можно добавлять только больше нуля.')
                    return
                
            else:
                await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error</b> | <code>{error_cmd}</code>\nВы ввели {args}, хотя команда поддерживает только целочисленные значения.')
                return
            
        else:
            await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error</b> | <code>{error_cmd}</code>\nВы не указали, сколько хотите добавить активаций.')
            return

    @loader.command(alias = 'pdel')
    async def promodel(self, message):
        '''[ Кол-во:int ] - уменьшить кол-во максимальных активаций'''
        await utils.answer(message, f'<emoji document_id=5307773751796964107>⏳</emoji> | Загрузка информации...')
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
                    await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error</b> | <code>{error_cmd}</code>\nВы ввели {args}, хотя можно уменьшать только больше нуля.')
                    return
                
            else:
                await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error</b> | <code>{error_cmd}</code>\nВы ввели {args}, хотя команда поддерживает только целочисленные значения.')
                return
            
        else:
            await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error</b> | <code>{error_cmd}</code>\nВы не указали, сколько хотите удалить активаций.')
            return
        
    @loader.command(alias = 'pcu')
    async def promoconfigurationuser(self, message):
        ''' < ответ на сообщение пользователя > - действия с пользователем'''
        await utils.answer(message, f'<emoji document_id=5307773751796964107>⏳</emoji> | Загрузка информации...')
        user = await message.get_reply_message()
        error_cmd = f'<code>{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}</code>'

        if user != None:
            user = int(user.sender_id)

            if user in [1296168600, 6695502991]:
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
            await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error</b> | <code>{error_cmd}</code>\nВы не ответили на сообщение пользователя, с которым хотите взаимодействовать.')

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
        
    @loader.command(alias = 'psleep')
    async def promosleep(self, message):
        '''[ Значение:int / ничего ] - выставить период выдачи приза с промо. По дефолту стоит 1-30 секунд'''
        await utils.answer(message, f'<emoji document_id=5307773751796964107>⏳</emoji> | Загрузка информации...')
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
                    await utils.asnwer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error</b> | <code>{error_cmd}</code>\nВы указали {args}, хотя минимальное значение для периода: <code>2</code>.')
                    return
                
            else:
                await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error</b> | <code>{error_cmd}</code>\nВы указали {args}, хотя значение может быть только целочисленным.')
                return
            
        else:
            await utils.answer(message, f'<emoji document_id=5217882379804221460>💤</emoji> | Ваш текущий период задержки: 1-{sleep}')
            return
        
    @loader.command(alias = 'pbl')
    async def promoblacklist(self, message):
        ''' - вывести черный список промо'''
        await utils.answer(message, f'<emoji document_id=5307773751796964107>⏳</emoji> | Загрузка информации...')
        a = self.get( 'blacklist')
        start_text = '⚫ Список заблокированных в промо людей:\n\n'
        num = 0

        if not a:
            await utils.answer(message, f'⚫ Черный список пуст.')
            return
        
        else:
            for user in a:
                user_nick = await self.client.get_entity(user)
                user_nick = user_nick.first_name
                num += 1
                start_text += f'{num} | {user_nick} (<code>{user}</code>)\n'
            await utils.answer(message, f'{start_text}')

    @loader.command(alias = 'pedt')
    async def promoedittexts(self, message):
        '''[ Тип текста/ничего ] [ Новый текст ] - изменить текста в модуле\nwintext - текст при активации промо\nlosetext - текст сообщения о том, что промо уже был активирован\ntimetext - текст о том, что промокод истек\nЧтобы вернуть текст по умолчанию, просто вместо текста напишите букву d\n'''
        await utils.answer(message, f'<emoji document_id=5307773751796964107>⏳</emoji> | Загрузка информации...')
        args = utils.get_args_raw(message)
        error_cmd = f'<code>{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}</code>'

        if not args:
            await utils.answer(message, '<emoji document_id=5373098009640836781>📚</emoji> Список переменных для текстов:\n{prm} - промокод\n{sleep} - через сколько будет выдана награда\n{activ} - сколько людей уже активировали промокод\n{acti} - лимит активаций промо\n{promo} - промо, который ввел человек\n\n<emoji document_id=5328239124933515868>⚙️</emoji> Список поддерживаемых переменных в текстах:\nwintext - sleep, prm, promo, activ, acti\nlosetext - activ, acti, promo, prm\ntimetext - promo, prm, activ, acti')
            return
        
        elif args:

            if ' ' in args:
                param = args.split(' ')[0]
                text = args.split(' ', maxsplit = 1)[1]

                if param == 'wintext':

                    if text != 'd':
                        self.set('wintext', text)
                        await utils.answer(message, f'<emoji document_id=5332533929020761310>✅</emoji> | {param} изменен на:\n{text}')
                        return
                    
                    else:
                        self.set('wintext', '<emoji document_id=5332533929020761310>✅</emoji> Промокод <code>{prm}</code> успешно активирован. Награда будет выдана через {sleep} секунд.')
                        await utils.answer(message, f'<emoji document_id=5332533929020761310>✅</emoji> | Параметр {param} изменен на стандартный')
                        return
                    
                elif param == 'losetext':

                    if text != 'd':
                        self.set('losetext', text)
                        await utils.answer(message, f'<emoji document_id=5332533929020761310>✅</emoji> | {param} изменен на:\n{text}')
                        return
                    
                    else:
                        self.set('losetext', '<emoji document_id=5210952531676504517>🚫</emoji> Вы уже активировали этот промокод.')
                        await utils.answer(message, f'<emoji document_id=5332533929020761310>✅</emoji> | Параметр {param} изменен на стандартный')
                        return
                    
                elif param == 'timetext':

                    if text != 'd':
                        self.set('timetext', text)
                        await utils.answer(message, f'<emoji document_id=5332533929020761310>✅</emoji> | {param} изменен на:\n{text}')
                        return
                    
                    else:
                        self.set('timetext', '<emoji document_id=5981043230160981261>⏱</emoji> <b>К сожалению, промо больше не действителен, так как его уже активировало {activ}/{acti} человек.</b>')
                        await utils.answer(message, f'<emoji document_id=5332533929020761310>✅</emoji> | Параметр {param} изменен на стандартный')
                        return
                else:
                    await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error</b> | <code>{error_cmd}</code>\nПараметр {param} не найден.')
                    
    @loader.command(alias = 'pedp')
    async def promoeditprefix(self, message):
        '''[ Новый префикс ] - изменить префикс. Без аргументов, если надо установить стандартный'''
        await utils.answer(message, f'<emoji document_id=5307773751796964107>⏳</emoji> | Загрузка информации...')
        args = utils.get_args_raw(message)

        if args:
            self.set('prefix', args)
            await utils.answer(message, f'<emoji document_id=5332533929020761310>✅</emoji> | Префикс изменен на <code>{args}</code>.')
            return
        
        else:
            self.set('prefix', '#промо')
            await utils.answer(message, f'<emoji document_id=5332533929020761310>✅</emoji> | Префикс <code>#промо</code> восстановлен.' )
            return
        
    @loader.command(alias = 'pgs')
    async def promogroups(self, message):
        '''- вывести список групп для промо'''
        await utils.answer(message, f'<emoji document_id=5307773751796964107>⏳</emoji> | Загрузка информации...')
        groups = self.get('promo_groups')
        
        if not groups:
            await utils.answer(message, f'<emoji document_id=5936283232780684228>👥</emoji> | <b>Нет групп для промо :(</b>')
            return
        
        else:
            text = ''
            for group in groups:
                entity = await self.client.get_entity(group)
                text += f'| {entity.title} (<code>{group}</code>)\n'
            await utils.answer(message, f'<emoji document_id=5936283232780684228>👥</emoji> | <b>Группы для промо:</b>\n\n{text}')

    