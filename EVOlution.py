#—————————————————————————————————————————————————————————————————————————————————
#  █▀ █ █ ▀▄▀   █▀▄▀█ █▀█ █▀▄ █ █ █   █▀▀ █▀ Chanel: https://mescr_m
#  ▄█ █▀█ █ █   █ ▀ █ █▄█ █▄▀ █▄█ █▄▄ ██▄ ▄█ Not Licensed
#—————————————————————————————————————————————————————————————————————————————————
#  █▀▀ ▀▄▀ █   █ █ █▀ █ █ █ █▀▀   █▀▄▀█ █▀█ █▀▄ █ █ █   █▀▀ █▀
#  ██▄ █ █ █▄▄ █▄█ ▄█ █ ▀▄▀ ██▄   █ ▀ █ █▄█ █▄▀ █▄█ █▄▄ ██▄ ▄█
#—————————————————————————————————————————————————————————————————————————————————
# Idea: sqlmerr
# meta developer: @mescr_m
# Thanks: 
#—————————————————————————————————————————————————————————————————————————————————


import asyncio
import re
from telethon.tl.types import Message, ChatAdminRights
from telethon import functions
import logging
import argparse
from asyncio import sleep
from .. import loader, utils
from ..inline.types import InlineCall

logger = logging.getLogger(__name__)

@loader.tds
class EVOlution(loader.Module):
    """Модуль для управления аккаунтом в MineEVO\nЧитайте гайд: https://telegra.ph/EVOlution-06-26\nУстанавливайте модуль исключительно из @mescr_m"""
    strings = {
        "name" : "EVOlution 1.8.1",
        "cfg_waiting_time" : "Время ожидания ответа от бота\nДля .evo",
        'delay_craft' : 'Задержка между отправкой запроса на крафт бустера\nДля .craft',
        'autoattack' : 'Автоматическая атака боссов',
        'delay_boss' : 'Задержка между атакой',
        'result_attack' : 'Отправлять ли результат боя к вам в избранные?\nРаботает только при включенном autoattack',
        'result_chat': 'Чат  в который будут отправляться результаты.\nЕсли юзернейм, то с @\nПример: @example\nЕсли в избранное - me',
        'gif_inline' : 'Гиф в inline',
        'petroleum' : 'Добывать нефть автоматически?\nВключайте через .petroleum!!!',
        'thank_you': "Не трогайте это!",
        'delay_choose_boss': 'Раз в сколько секунд нажимать инлайн кнопку?',
        'petroleum_drill':'Заправлять ли бур, если хранилище заполнено топливом?',
        'delay_collect_drill': 'Переодичность сбора руды с бура ( в минутах )',
        'auto_collect_drill': 'Собирать ли руду с бура автоматически?',
        'my_nickname': 'Ваш никнейм для быстрой команды %имя'
    }
    
    


    async def client_ready(self):
        
        self._backup_channel, _ = await utils.asset_channel(
            self._client,
            "EVOQasst",
            "Группа для работы модуля EVO от @Shx_modules\nНе добавляйте сюда других людей или ботов!",
            silent=True,
            archive=True,
            _folder="hikka",
        )

        await self.client(functions.channels.InviteToChannelRequest(self._backup_channel, ['@mine_evo_bot']))
        await self.client(functions.channels.EditAdminRequest(
                channel=self._backup_channel,
                user_id="@mine_evo_bot",
                admin_rights=ChatAdminRights(ban_users=True, post_messages=True, edit_messages=True),
                rank="EVO",
            )
        )
        self._drill_channel, _ = await utils.asset_channel(
            self._client,
            "EVO_Drill",
            "Группа для работы auto_collect_drill в модуле EVO от @Shx_modules\nНе добавляйте сюда других людей или ботов!",
            silent=True,
            archive=True,
            _folder="hikka",
        )

        await self.client(functions.channels.InviteToChannelRequest(self._backup_channel, ['@mine_evo_bot']))
        await self.client(functions.channels.EditAdminRequest(
                channel=self._drill_channel,
                user_id="@mine_evo_bot",
                admin_rights=ChatAdminRights(ban_users=True, post_messages=True, edit_messages=True),
                rank="EVO",
            )
        )
        au_drill = self.config['auto_collect_drill']
        d_drill = self.config['delay_collect_drill']
        d_drill = d_drill * 60
        while au_drill == True:
            async with self.client.conversation(self._drill_channel) as drillgroup:
                await drillgroup.send_message('Мой бур')
                aud = await drillgroup.get_response()
            await aud.click(0)
            await asyncio.sleep(d_drill)
        
        if self.config['petroleum'] == True:
            await self.client.send_message('@mine_evo_bot', 'Качать')
        thank = self.config['thank_you']
        if thank == True:
            self.config['thank_you'] = False
            await self.client.send_message('me','<emoji document_id=5206399660184313498>❤️</emoji> <b>Спасибо за установку модуля EVOlution!</b>\n\nНа самом деле, это искреннее "Спасибо"! Я и в правду очень рад, что мое творение попало к вам в список модулей.\n\nЭто сообщение отправилось только один раз и только к вам в избранное, поэтому вам не стоит переживать :D\n\nЕсли вас заинтересуют мои модули, жду вас в shx_modules.t.me\nСборник всех(почти) модулей для хикки: ubhikka_modules.t.me')
            await self.client.send_message('me', '<emoji document_id=5255900725933779026>🔠</emoji><emoji document_id=5255854937287435776>🔠</emoji><emoji document_id=5256005879618086735>🔠</emoji><emoji document_id=5255854937287435776>🔠</emoji><emoji document_id=5255737126334506261>🔠</emoji><emoji document_id=5255838994368834442>🔠</emoji><emoji document_id=5256057178707469647>🔠</emoji><emoji document_id=5255854937287435776>🔠</emoji><emoji document_id=6032769737509833594>📛</emoji><emoji document_id=5258045984788717832>🔠</emoji><emoji document_id=5255972975873632543>🔠</emoji><emoji document_id=5255973950831208848>🔠</emoji><emoji document_id=5255935626838025893>🔠</emoji>')
        
        
        

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "waiting_time", 1.0,
                lambda: self.strings("cfg_waiting_time"),
                validator=loader.validators.Float()
            ),
            loader.ConfigValue(
                "delay_craft", 2.0,
                lambda: self.strings("delay_craft"),
                validator=loader.validators.Float()
            ),
            loader.ConfigValue(
                "autoattack", False,
                lambda: self.strings("autoattack"),
                validator=loader.validators.Boolean()
            ),
            loader.ConfigValue(
                "delay_boss", 1.0,
                lambda: self.strings("delay_boss"),
                validator=loader.validators.Float()
            ),
            loader.ConfigValue(
                "result_attack", True,
                lambda: self.strings("result_attack"),
                validator=loader.validators.Boolean()
            ),           
            loader.ConfigValue(
                "result_chat", 'me',
                lambda: self.strings("result_chat"),
                validator=loader.validators.String()
            ),
            loader.ConfigValue(
                "gif_inline", 'https://x0.at/n5Gn.mp4',
                lambda: self.strings("gif_inline"),
                validator=loader.validators.String()
            ),
            loader.ConfigValue(
                "petroleum", False,
                lambda: self.strings("petroleum"),
                validator=loader.validators.Boolean()
            ),
            loader.ConfigValue(
                "petroleum_drill", False,
                lambda: self.strings("petroleum_drill"),
                validator=loader.validators.Boolean()
            ),
            loader.ConfigValue(
                "thank_you", True,
                lambda: self.strings("thank_you"),
                validator=loader.validators.Boolean()
            ),
            loader.ConfigValue(
                "delay_choose_boss", 2.0,
                lambda: self.strings("delay_choose_boss"),
                validator=loader.validators.Float(minimum = 0.5)
            ),
            loader.ConfigValue(
                "auto_collect_drill", False,
                lambda: self.strings("auto_collect_drill"),
                validator=loader.validators.Boolean()
            ),
            loader.ConfigValue(
                "delay_collect_drill", 240,
                lambda: self.strings("delay_collect_drill"),
                validator=loader.validators.Integer(minimum = 60)
            ),
            loader.ConfigValue(
                "my_nickname", '#',
                lambda: self.strings("my_nickname"),
                validator=loader.validators.String()
            ),
            
        )

   

           
                





    @loader.watcher()
    async def watcher(self, message):
        autoattack = self.config['autoattack']
        delay_boss = self.config['delay_boss']
        result_attack = self.config['result_attack']
        petroleum = self.config['petroleum']
        result_chat = self.config['result_chat']
        drill = self.config['petroleum_drill']
        



        if autoattack == True:
            if message.chat_id == 5522271758 and "Атк)" in message.raw_text:
                await asyncio.sleep(delay_boss)
                await self.client.send_message('@mine_evo_bot', 'Атк')    
            elif message.chat_id == 5522271758 and '🔶 Ты выбрал босса:' in message.raw_text:
                await asyncio.sleep(delay_boss)
                await self.client.send_message('@mine_evo_bot', 'Атк')    
            if result_attack == True:
                if message.chat_id == 5522271758 and "Твоя награда:" in message.raw_text:
                    if '@' in result_chat:
                        await self.client.send_message(result_chat, message.raw_text)
                        return
                    if result_chat == 'me':
                        await self.client.send_message(result_chat, message.raw_text)
                        return
                    else:
                        result_chat = int(result_chat)
                        await self.client.send_message(result_chat, message.raw_text)
        if message.raw_text == '/check':
            if message.from_id == 5195118663: 
                await self.client.send_message(message.to_id, 'evo')
                return
        if petroleum == True:
            if message.chat_id == 5522271758 and "Нефти в месторождении:" in message.raw_text:
                await asyncio.sleep(4)
                await self.client.send_message('@mine_evo_bot', 'Качать')
                return
            if message.chat_id == 5522271758 and "кончилась нефть!" in message.raw_text:
                await asyncio.sleep(3600)
                await self.client.send_message('@mine_evo_bot', "Качать")
                return
            if message.chat_id == 5522271758 and "заполнено топливом!" in message.raw_text:                
                if drill == True:
                    await self.client.send_message('me', '<emoji document_id=5397866729554583012>❗️</emoji> <b>Warning | Petroleum</b>\nВаше хранилище заполнено топливом!\n<emoji document_id=5787544344906959608>ℹ️</emoji> Бур был дозаправлен.')
                    async with self.client.conversation(self._backup_channel) as conv:
                        await conv.send_message(f'Мой бур')
                        au = (await conv.get_response()).message
                    await au.click(1)                   
                    await asyncio.sleep(3600)                                      
                    await self.client.send_message('@mine_evo_bot', "Качать")               
                    return
                else:
                    await self.client.send_message('me', '<emoji document_id=5397866729554583012>❗️</emoji> <b>Warning | Petroleum</b>\nВаше хранилище заполнено топливом!')
                    await asyncio.sleep(3600)                                      
                    await self.client.send_message('@mine_evo_bot', "Качать")  
                    return
        
               

    @loader.watcher(out = True)
    async def watcherfst(self, message):
        mnn = self.config['my_nickname']
        
        if message.raw_text == '%мб':
            await message.delete()
            await self.client.send_message(message.to_id, '💥 Мощь бура')          
            return
        if message.raw_text == '%бб':
            await message.delete()
            await self.client.send_message(message.to_id, '🛢 Бак бура')
            return
        if message.raw_text == '%нс':
            await message.delete()
            await self.client.send_message(message.to_id, '🗼 Насосы')
            return
        if message.raw_text == '%вм':
            await message.delete()
            await self.client.send_message(message.to_id, '🚛 Вместимость')
            return
        if message.raw_text == '%мс':
            await message.delete()
            await self.client.send_message(message.to_id, '🏜 Месторождение')
            return
        if message.raw_text == '%имя':
            await message.delete()
            await self.client.send_message(message.to_id, mnn)


        
            
            
            
    @loader.command()
    async def fchelp(self, message):
        ''' - список быстрых команд'''
        await utils.answer(message, '%мб - 💥 Мощь бура\n%бб - 🛢 Бак бура\n%нс - 🗼 Насосы\n%вм - 🚛 Вместимость\n%мс - 🏜 Месторождение\n%имя - 👤 Ваш никнейм ( указывайте в конфиге )')

    @loader.command()
    async def evo(self, message: Message):
        """ - выполнить команду MineEVO в любом чате"""
        args = utils.get_args_raw(message)
        waiting_time = self.config["waiting_time"]
        error_not_args = "<emoji document_id=5877477244938489129>🚫</emoji> <b>Error | evo</b>\nВы не ввели запрос!"
        error_not_response = f"<emoji document_id=5877477244938489129>🚫</emoji> <b>Error | evo</b>\nНа ваш запрос не был получен ответ в течение {waiting_time} секунд(-ы)\n<b>Ваш запрос:</b> {args} \n\n<emoji document_id=5787544344906959608>ℹ️</emoji> <b>Возможные проблемы:</b>"
        ore = "<b>Цены на руды:</b>\n> https://teletype.in/@mine_evo/ores_prices_1"
        err_d1 = "\n> Вы ввели запрос, которого не существует."
        err_d2 = "\n> У MineEVO высокий пинг."

        if args == '':
            await utils.answer(message, error_not_args)
        elif args in ["Цены","цены","рынок","Рынок"]:
            await utils.answer(message, ore)
        else:
            await utils.answer(message, '<emoji document_id=5204112375350831270>🕓</emoji> Выполняется...')
            async with self.client.conversation(self._backup_channel) as conv:
                await conv.send_message(f'{args}')
                try:
                    response = await asyncio.wait_for(conv.get_response(), timeout=waiting_time)
                except asyncio.TimeoutError:
                    await utils.answer(message, error_not_response + err_d1 + err_d2)
                    return
            links_regex = re.compile(r'.(https?://\S+).')
            response.text = links_regex.sub('', response.text)
            if re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', response.text):
                response.text = '\n'.join(response.text.split('\n')[:-2])
            await utils.answer(message, response.text)

            


    @loader.command(alias = 'eh')
    async def evoh(self, message: Message):
        """ - аргументы для .evo"""
        args = utils.get_args_raw(message)

        #Topics
        topic_full = "<b><emoji document_id=5334882760735598374>📝</emoji> Помощь по командам</b>\n\n"
        topic_boost = "<b>> <emoji document_id=5445284980978621387>🚀</emoji> Бустеры</b>\n"
        topic_cases = "<b>> <emoji document_id=5359785904535774578>💼</emoji> Кейсы</b>\n"
        topic_top = "<b>> <emoji document_id=5188208446461188962>💯</emoji> Топ</b>\n"
        topic_stats = "<b>> <emoji document_id=5373001317042101552>📈</emoji> Статистика</b>\n"
        topic_other = "<b>> <emoji document_id=5370869711888194012>👾</emoji> Прочее</b>\n"
        topic_storage = "<b>> <emoji document_id=5431736674147114227>🗂</emoji> Хранилище</b>\n"
        topic_add = "Чтобы посмотреть отдельный топик, не обязательно писать его название, достаточно написать любую команду из этого топика"
        
        #Commands
        cmdboost = "  > Буст [ Тип бустера ] [ Множитель ]\n    > р | д | гр | гд\n    > 1.5 | 2 | 2.5 | 3\n  > Бусты\n  > Крафт [ Тип бустера ] [ Множитель ]\n    > р | д\n    > 2 | 2.5 | 3\n  > Утиль [ Тип бустера ] [ Множитель ]\n    > р | д\n    > 1.5 | 2 | 2.5 | 3\n  > Время\n\n"
        cmdcases = "  > Кейсы\n  > Открыть [ Тип кейса ] [ Кол-во ]\n    > Кт | Ркт | К | Рк | Миф | Кр | Зв \n  > Дать [ Тип кейса ] [ Кол-во ]\n    > Кт | Ркт | К | Рк | Миф | Кр | Зв\n  > Открыть [ Тип кейса ] [ Кол-во ]\n    > Кт | Ркт | К | Рк | Миф | Кр | Зв \n\n"
        cmdtop = "  > Топ\n  > Топ [ Тип топа ]\n    >  к | д | б | р | клан\n\n"
        cmdstats = "  > Проф \n  > Стата \n  > Лим\n  > Мой реф\n\n"
        cmdstorage = "  > Б\n  > П\n  > C\n  > Зп\n  > Инв\n  > Продать [ Название руды ] [ Кол-во/Все ]\n  > Перевести [ Ник ] [ Кол-во денег/Лимит ]\n\n"
        cmdother = "  > Реф [ Реферальный код ]\n  > Ивент\n  > Конкурс\n  > Еб\n  > Thx\n  > Цены\n  > Рынок\n\n"
        
        #Error
        err_topic = "<emoji document_id=5877477244938489129>🚫</emoji> <b>Error | Ошибка</b>\nТопик не найден.\nНазвание топиков можно посмотреть в evoh."
        
        if args in ['Бустеры','бустеры','Бусты','бусты','Буст','буст','Крафт','крафт','Утиль','утиль','Время','время']:
            await utils.answer(message, topic_full + topic_boost + cmdboost)
        
        elif args in ['Кейсы','кейсы','Открыть','открыть','Дать','дать','Передать','передать']:
            await utils.answer(message, topic_full + topic_cases + cmdcases)
        
        elif args in ['Топ','топ']:
            await utils.answer(message, topic_full + topic_top + cmdtop)
        
        elif args in ['Стат','стат','Стата','стата','Статистика','статистика','Проф','проф','Лим','лим','Лимит','лимит','Мой реф','мой реф']:
            await utils.answer(message, topic_full + topic_stats + cmdstats)
        
        elif args in ['Хранилище','хранилище','Б','б','П','п','С','с','Зп','зп','Инв','инв','Продать','продать','Перевести','перевести']:
            await utils.answer(message, topic_full + topic_storage + cmdstorage )
        
        elif args in ['Прочее','прочее','Реф','реф','Ивент','ивент','Конкурс','конкурс','Еб','еб','Thx','thx','Цены','цены','Рынок','рынок']:
            await utils.answer(message, topic_full + topic_other + cmdother)
        
        elif args == '':
            await utils.answer(message, topic_full + topic_boost + cmdboost + topic_cases + cmdcases + topic_top + cmdtop + topic_stats + cmdstats + topic_storage + cmdstorage + topic_other + cmdother + topic_add)
        
        else:
            await utils.answer(message, err_topic)

    @loader.command(alias = 'c')
    async def craft(self, message: Message):
        """ - крафт большого кол-ва бустеров"""
        await utils.answer(message, '<emoji document_id=5204112375350831270>🕓</emoji> Начинаю крафт бустеров...\n\nПодготовка данных... [ args, delay, type, mult, quantity, quantityl, errtype, errmult, startcraft ]')
        args = utils.get_args_split_by(message, " ")
        delay = self.config["delay_craft"]
        type = args[0]
        mult = args[1]
        quantity = args[2]
        quantityl = quantity
        errtype = f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error | craft </b>\nТип бустера "{type}" не найден.\nМожно крафстить только бустеры:\nР, р - руда\nД, д - деньги'
        errmult = f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error | craft </b>\nМножителя "{mult}" не существует.\nИспользуйте: 2, 2.0, 2.5, 3, 3.0'
        startcraft = 0
        await utils.answer(message, '<emoji document_id=5204112375350831270>🕓</emoji> Начинаю крафт бустеров...\n\nПодготовка данных... [ args, delay, type, mult, quantity, quantityl, errtype, errmult, startcraft ] \n\nКрафтим...')
        if type in ['Р', 'р', 'Д', 'д' ]:
            if mult in ['2', '2.0', '2.5', '3', '3.0']:
                while int(quantity) > 0:
                    quantity = int(quantity) - 1
                    async with self.client.conversation(self._backup_channel) as conv:   
                        await conv.send_message(f'Крафт {type} {mult}')
                        await asyncio.sleep(delay)
                        startcraft = startcraft + 1
                        await utils.answer(message, f'<emoji document_id=5204112375350831270>🕓</emoji> Начинаю крафт бустеров...\n\nПодготовка данных... [ args, delay, type, mult, quantity, quantityl, errtype, errmult, startcraft ] \n\nКрафтим...\n\nОтправлено запросов на данный момент: {startcraft}')
                await asyncio.sleep(2)    
                async with self.client.conversation(self._backup_channel) as conv:   
                        await conv.send_message(f'Бусты')
                        response = (await conv.get_response()).message
                        response = response[:-2]
                await utils.answer(message, '<emoji document_id=5204044038126182496>✅</emoji> Крафт завершен!\n\n\n<code>Загрузка информации...</code>')
                await asyncio.sleep(1)
                if type == 'д':
                    type = 'Деньги'
                elif type == 'р':
                    type = 'Руда'
                await utils.answer(message, f"<emoji document_id=5204044038126182496>✅</emoji> Крафт завершен!\n\n<b>Информация:</b>\n▫️<b>Тип бустера:</b> <code>{type}</code>\n▫️<b>Множитель бустеров:</b> <code>{mult}</code>\n▫️<b>Кол-во раз отправлено:</b> <code>{quantityl}</code>\n▫️<b>Была задержка:</b> <code>{delay}</code>\n\n<b>Итоговый список бустеров:</b>\n{response}")
            else:
                await utils.answer(message, errmult)
        else:
            await utils.answer(message, errtype)

    @loader.command(alias = 't')    
    async def top(self, message):
        ''' - инлайн топ'''
        gif_on_top = self.config['gif_inline']

        await self.inline.form(
            text = 'Выберите топ: ',
            gif = gif_on_top,
            message=message,
            reply_markup=[
                [
                    {
                        "text": "⭐️ Уровень",
                        "callback": self.toplvl,
                    },
                    {
                        "text": "👆 Клики ",
                        "callback": self.topclicks,
                    },
                ],
                [
                    
                    {
                        "text": "💎 Донат",
                        "callback": self.topdonate,
                    },
                    {
                        "text": "🧱 Руда",
                        "callback": self.topore,
                    }
                ],
                [
                    {
                        "text": "🏰 Кланы",
                        "callback": self.topclan,
                    },
                    {
                        'text':'💵 Баланс',
                        'callback':self.topbalance,
                    }
                ],
                [
                    {
                        'text':'💰 Поддержать автора ( 1 кейс )',
                        'callback': self.donate_author,
                    },
                ],              
                [
                    {
                        "text": "🔻 Закрыть",
                        "action": "close",
                    }
                ],
            ],
        )
    @loader.command(alias = 'p')    
    async def prof(self, message):
        ''' - инлайн профиль'''
        gif_on_top = self.config['gif_inline']

        await self.inline.form(
            text = 'Куда пойдем?',
            gif = gif_on_top,
            message=message,
            reply_markup=[
                    [
                        {
                            "text": "📋 Профиль",
                            "callback": self.stor_prof,
                        },
                        {
                            'text': '📈 Статистика',
                            'callback': self.stor_stata,
                        }
                    ],
                    [
                        {
                            "text": "🎒 Инвентарь",
                            "callback": self.stor_inv,
                        },
                    ],
                    [
                        {
                            'text': '🌌 Звездная Пыль',
                            'callback': self.stor_star
                        }
                    ],
                    [
                        {
                            'text':'📦 Кейсы',
                            'callback':self.stor_cases,
                        },
                        {
                            'text':'⚡️ Бустеры',
                            'callback':self.stor_boosters,
                        }
                    ],
                    [
                        {
                            "text": "🎆 Плазма",
                            "callback": self.stor_plasm,
                        },
                        {
                            "text": "💵 Баланс",
                            "callback": self.stor_balance,
                        },
                        {
                            "text": "🔩 Скрап",
                            "callback": self.stor_scrap,
                        }
                    ],      
                    [
                        {
                        'text':'💰 Поддержать автора ( 1 кейс )',
                        'callback': self.donate_author,
                        },
                    ],
                    [
                        {
                        "text": "🔻 Закрыть",
                        "action": "close",
                        }
                    ],
            ],
        )


    @loader.command(alias = 'aa')
    async def autoattack(self, message):
        ''' - включить / выключить автоатакер'''
        self.config['autoattack'] = not self.config['autoattack']
        cfg = self.config['autoattack']
        if cfg == True:
            await utils.answer(message, '<emoji document_id=5204044038126182496>✅</emoji> АвтоАтакер включен.')
        if cfg == False:
            await utils.answer(message, '<emoji document_id=5206595394728894920>❌</emoji> АвтоАтакер отключен.')

    @loader.command(alias = 'pt')
    async def petroleum(self, message):
        ''' - включить / выключить автодобычу нефти'''
        self.config['petroleum'] = not self.config['petroleum']
        cfg = self.config['petroleum']
        if cfg == True:
            await utils.answer(message, '<emoji document_id=5204044038126182496>✅</emoji> Автодобыча нефти включена.')
            await self.client.send_message('@mine_evo_bot', 'Качать')
        if cfg == False:
            await utils.answer(message, '<emoji document_id=5206595394728894920>❌</emoji> Автодобыча нефти отключена.')

    @loader.command(alias = 'acd')
    async def autocollectdrill(self, message):
        ''' - включить / выключить автосбор лута из бура'''
        self.config['auto_collect_drill'] = not self.config['auto_collect_drill']
        acd_status = self.config['auto_collect_drill']
        if acd_status == True:
            await utils.answer(message, '<emoji document_id=5204044038126182496>✅</emoji> Автосбор руды включен.')
            return
        if acd_status == False:
            await utils.answer(message, '<emoji document_id=5206595394728894920>❌</emoji> Автосбор руды отключен.')
            return

    @loader.command()
    async def scfg(self, message):
        ''' - изменить параметр без открытия конфига'''
        args = utils.get_args_raw(message).split(" ")
        param = args[0]
        zz = args[1]

        if param == 'db':
            self.config['delay_boss'] = zz
            await utils.answer(message, f'<emoji document_id=5204044038126182496>✅</emoji> Параметр <code>{param}</code> изменен на <code>{zz}</code>')
            return
        if param == 'dct':
            self.config['delay_craft'] = zz
            await utils.answer(message, f'<emoji document_id=5204044038126182496>✅</emoji> Параметр <code>{param}</code> изменен на <code>{zz}</code>')
            return
        if param == 'gi':
            self.config['gif_inline'] = zz
            await utils.answer(message, f'<emoji document_id=5204044038126182496>✅</emoji> Параметр <code>{param}</code> изменен на <code>{zz}</code>')
            return
        if param == 'wt':
            self.config['waiting_time'] = zz
            await utils.answer(message, f'<emoji document_id=5204044038126182496>✅</emoji> Параметр <code>{param}</code> изменен на <code>{zz}</code>')
            return
        if param == 'rc':
            self.config['result_chat'] = zz
            await utils.answer(message, f'<emoji document_id=5204044038126182496>✅</emoji> Параметр <code>{param}</code> изменен на <code>{zz}</code>')
            return
        if param == 'dcb':
            self.config['delay_choose_boss'] = zz
            await utils.answer(message, f'<emoji document_id=5204044038126182496>✅</emoji> Параметр <code>{param}</code> изменен на <code>{zz}</code>')
            return
        if param == 'dcd':
            zz = int(zz)
            if zz < 60:
                await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error | scfg</b>\nЗначение {param} не может быть меньше 60!')
                return
            if zz > 60:
                self.config['delay_collect_drill'] = zz
                await utils.answer(message, f'<emoji document_id=5204044038126182496>✅</emoji> Параметр <code>{param}</code> изменен на <code>{zz}</code>')
                return
        else:
            await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error | scfg</b>\nПараметр <code>{param}</code> не найден.')


    @loader.command()
    async def up(self, message):
        ''' - улучшить что-либо'''
        args = utils.get_args_raw(message)
        uplist = ['Ур', 'ур', 'Мщ', 'мщ', 'Уд', 'уд', 'Урон', 'урон', 'Крит', 'крит', 'Шп', 'шп', 'Уп', 'уп', 'Шк', 'шк', 'Мр', 'мр', 'Мп', 'мп', 'Мэ', 'мэ', 'Му', 'му', 'Зс', 'зс']
        if args in uplist:
            await utils.answer(message, 'Выполняется...')
            async with self.client.conversation(self._backup_channel) as conv:
                await conv.send_message(f'{args}')
                res = await conv.get_response()
            await res.click(0)
            res = res.text
            await utils.answer(message, f'<emoji document_id=5204044038126182496>✅</emoji> <b>Выполнено. Вот какие были условия:</b>\n\n{res}')
            return
        else:
            await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji><b> Error | up</b>\nУлучшение {args} не найдено.')
            return

    @loader.command(alias = 'sb')
    async def sboss(self, message):
        ''' - автоматически выбрать босса при его появлении'''
        reply_arg = await message.get_reply_message()
        arg = utils.get_args_raw(message)
        delay_choose_boss = self.config['delay_choose_boss']
        if arg == '':
            await utils.answer(message, '<emoji document_id=5877477244938489129>🚫</emoji><b> Error | sboss</b>\nВы не выбрали босса!')
            return
        if not reply_arg:
            await utils.answer(message, '<emoji document_id=5877477244938489129>🚫</emoji><b> Error | sboss</b>\nВы не ответили на сообщение с выбором босса!')
            return
        await utils.answer(message, f'<emoji document_id=5204044038126182496>✅</emoji> Успешно! Выбран босс №{arg}')
        select_boss = int(arg) - 1
        if int(arg) >= 1 and int(arg) <= 25:
            while reply_arg != '':
                await asyncio.sleep(delay_choose_boss)
                await reply_arg.click(select_boss)
            await utils.answer(message, 'АаАаАаАа')
            return
        else:
            await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji><b> Error | sboss</b>\nВы выбрали босса №{arg}, хотя разрешены только боссы от 1 до 25')
        
    async def toplvl(self, call: InlineCall):
        async with self.client.conversation(self._backup_channel) as conv:
                await conv.send_message(f'топ')
                response = (await conv.get_response()).message
        await call.edit(
            text=response,
            reply_markup=[
                [
                    {
                        "text": "> ⭐️ Уровень <",
                        "callback": None,
                    },
                    {
                        "text": "👆 Клики ",
                        "callback": self.topclicks,
                    },
                ],
                [
                    
                    {
                        "text": "💎 Донат",
                        "callback": self.topdonate,
                    },
                    {
                        "text": "🧱 Руда",
                        "callback": self.topore,
                    }
                ],
                [
                    {
                        "text": "🏰 Кланы",
                        "callback": self.topclan,
                    },
                    {
                        'text':'💵 Баланс',
                        'callback': self.topbalance,
                    }
                ],         
                [
                    {
                        'text':'💰 Поддержать автора ( 1 кейс )',
                        'callback': self.donate_author,
                    },
                ],
                [
                    {
                        "text": "🔻 Закрыть",
                        "action": "close",
                    }
                ],
            ],
        )
        
    async def topclicks(self, call: InlineCall):
        async with self.client.conversation(self._backup_channel) as conv:
                await conv.send_message(f'топ к')
                response = (await conv.get_response()).message
        await call.edit(
            text=response,
            reply_markup=[
               [
                    {
                        "text": "⭐️ Уровень",
                        "callback": self.toplvl,
                    },
                    {
                        "text": "> 👆 Клики <",
                        "callback": None,
                    },
                ],
                [
                    
                    {
                        "text": "💎 Донат",
                        "callback": self.topdonate,
                    },
                    {
                        "text": "🧱 Руда",
                        "callback": self.topore,
                    }
                ],
                [
                    {
                        "text": "🏰 Кланы",
                        "callback": self.topclan,
                    },
                    {
                        'text':'💵 Баланс',
                        'callback':self.topbalance,
                    }
                ],
                [
                    {
                        'text':'💰 Поддержать автора ( 1 кейс )',
                        'callback': self.donate_author,
                    },
                ],      
                [
                    {
                        "text": "🔻 Закрыть",
                        "action": "close",
                    }
                ],
                
            ],
        )
    async def topdonate(self, call: InlineCall):
        async with self.client.conversation(self._backup_channel) as conv:
                await conv.send_message(f'топ д')
                response = (await conv.get_response()).message
        await call.edit(
            text=response,
            reply_markup=[
                [
                    {
                        "text": "⭐️ Уровень",
                        "callback": self.toplvl,
                    },
                    {
                        "text": "👆 Клики ",
                        "callback": self.topclicks,
                    },
                ],
                [
                    
                    {
                        "text": "> 💎 Донат <",
                        "callback": None,
                    },
                    {
                        "text": "🧱 Руда",
                        "callback": self.topore,
                    }
                ],
                [
                    {
                        "text": "🏰 Кланы",
                        "callback": self.topclan,
                    },
                    {
                        'text':'💵 Баланс',
                        'callback':self.topbalance,
                    }
                ],
                [
                    {
                        'text':'💰 Поддержать автора ( 1 кейс )',
                        'callback': self.donate_author,
                    },
                ],            
                [
                    {
                        "text": "🔻 Закрыть",
                        "action": "close",
                    }
                ],
            ],
        )

    async def topore(self, call: InlineCall):
        async with self.client.conversation(self._backup_channel) as conv:
                await conv.send_message(f'топ р')
                response = (await conv.get_response()).message
        await call.edit(
            text=response,
            reply_markup=[
                [
                    {
                        "text": "⭐️ Уровень",
                        "callback": self.toplvl,
                    },
                    {
                        "text": "👆 Клики ",
                        "callback": self.topclicks,
                    },
                ],
                [
                    
                    {
                        "text": "💎 Донат",
                        "callback": self.topdonate,
                    },
                    {
                        "text": "> 🧱 Руда <",
                        "callback": None,
                    }
                ],
                [
                    {
                        "text": "🏰 Кланы",
                        "callback": self.topclan,
                    },
                    {
                        'text':'💵 Баланс',
                        'callback':self.topbalance,
                    }
                ],
                [
                    {
                        'text':'💰 Поддержать автора ( 1 кейс )',
                        'callback': self.donate_author,
                    },
                ],             
                [
                    {
                        "text": "🔻 Закрыть",
                        "action": "close",
                    }
                ],
            ],
        )

    async def topclan(self, call: InlineCall):
        async with self.client.conversation(self._backup_channel) as conv:
                await conv.send_message(f'топ клан')
                response = (await conv.get_response()).message
        await call.edit(
            text=response,
            reply_markup=[
                [
                    {
                        "text": "⭐️ Уровень",
                        "callback": self.toplvl,
                    },
                    {
                        "text": "👆 Клики ",
                        "callback": self.topclicks,
                    },
                ],
                [
                    
                    {
                        "text": "💎 Донат",
                        "callback": self.topdonate,
                    },
                    {
                        "text": "🧱 Руда",
                        "callback": self.topore,
                    }
                ],
                [
                    {
                        "text": "> 🏰 Кланы <",
                        "callback": None,
                    },
                    {
                        'text':'💵 Баланс',
                        'callback':self.topbalance,
                    }
                ],
                [
                    {
                        'text':'💰 Поддержать автора ( 1 кейс )',
                        'callback': self.donate_author,
                    },
                ],               
                [
                    {
                        "text": "🔻 Закрыть",
                        "action": "close",
                    }
                ],
            ],
        )    

    async def topbalance(self, call: InlineCall):
        async with self.client.conversation(self._backup_channel) as conv:
                await conv.send_message(f'топ б')
                response = (await conv.get_response()).message
        await call.edit(
            text=response,
            reply_markup=[
                [
                    {
                        "text": "⭐️ Уровень",
                        "callback": self.toplvl,
                    },
                    {
                        "text": "👆 Клики ",
                        "callback": self.topclicks,
                    },
                ],
                [
                    
                    {
                        "text": "💎 Донат",
                        "callback": self.topdonate,
                    },
                    {
                        "text": "🧱 Руда",
                        "callback": self.topore,
                    }
                ],
                [
                    {
                        "text": "🏰 Кланы",
                        "callback": self.topclan,
                    },
                    {
                        'text':'> 💵 Баланс <',
                        'callback': None,
                    }
                ],
                [
                    {
                        'text':'💰 Поддержать автора ( 1 кейс )',
                        'callback': self.donate_author,
                    },
                ],              
                [
                    {
                        "text": "🔻 Закрыть",
                        "action": "close",
                    }
                ],
            ],
        )


    

    async def stor_prof(self, call: InlineCall):
        async with self.client.conversation(self._backup_channel) as conv:
            await conv.send_message('проф')
            response = (await conv.get_response()).message
            links_regex = re.compile(r'.(https?://\S+).')
            response = links_regex.sub('', response)
            if re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', response):
                response = '\n'.join(response.split('\n')[:-2])
            await call.edit(
                text=response,
                reply_markup=[
                    [
                        {
                            "text": "> 📋 Профиль  <",
                            "callback": self.stor_prof,
                        },
                        {
                            'text': '📈 Статистика',
                            'callback': self.stor_stata,
                        }
                    ],
                    [
                        {
                            "text": "🎒 Инвентарь",
                            "callback": self.stor_inv,
                        },
                    ],
                    [
                        {
                            'text': '🌌 Звездная Пыль',
                            'callback': self.stor_star
                        }
                    ],
                    [
                        {
                            'text':'📦 Кейсы',
                            'callback':self.stor_cases,
                        },
                        {
                            'text':'⚡️ Бустеры',
                            'callback':self.stor_boosters,
                        }
                    ],
                    [
                        {
                            "text": "🎆 Плазма",
                            "callback": self.stor_plasm,
                        },
                        {
                            "text": "💵 Баланс",
                            "callback": self.stor_balance,
                        },
                        {
                            "text": "🔩 Скрап",
                            "callback": self.stor_scrap,
                        }
                    ],
                    [
                        {
                            'text':'💰 Поддержать автора ( 1 кейс )',
                            'callback': self.donate_author,
                        },
                    ],     
                    [
                        {
                        "text": "🔻 Закрыть",
                        "action": "close",
                        }
                    ],
                ],
            )    

    async def stor_stata(self, call: InlineCall):
        async with self.client.conversation(self._backup_channel) as conv:
            await conv.send_message('стата')
            response = (await conv.get_response()).message
            links_regex = re.compile(r'.(https?://\S+).')
            response = links_regex.sub('', response)
            if re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', response):
                response = '\n'.join(response.split('\n')[:-2])
            await call.edit(
                text=response,
                reply_markup=[
                    [
                        {
                            "text": "📋 Профиль",
                            "callback": self.stor_prof,
                        },
                        {
                            'text': '> 📈 Статистика <',
                            'callback': self.stor_stata,
                        }
                    ],
                    [
                        {
                            "text": "🎒 Инвентарь",
                            "callback": self.stor_inv,
                        },
                    ],
                    [
                        {
                            'text': '🌌 Звездная Пыль',
                            'callback': self.stor_star
                        }
                    ],
                    [
                        {
                            'text':'📦 Кейсы',
                            'callback':self.stor_cases,
                        },
                        {
                            'text':'⚡️ Бустеры',
                            'callback':self.stor_boosters,
                        }
                    ],
                    [
                        {
                            "text": "🎆 Плазма",
                            "callback": self.stor_plasm,
                        },
                        {
                            "text": "💵 Баланс",
                            "callback": self.stor_balance,
                        },
                        {
                            "text": "🔩 Скрап",
                            "callback": self.stor_scrap,
                        }
                    ],
                    [
                        {
                            'text':'💰 Поддержать автора ( 1 кейс )',
                            'callback': self.donate_author,
                        },
                    ],      
                    [
                        {
                        "text": "🔻 Закрыть",
                        "action": "close",
                        }
                    ],
                ],
            )            

    async def stor_inv(self, call: InlineCall):
        async with self.client.conversation(self._backup_channel) as conv:
            await conv.send_message('инв')
            response = (await conv.get_response()).message
            links_regex = re.compile(r'.(https?://\S+).')
            response = links_regex.sub('', response)
            if re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', response):
                response = '\n'.join(response.split('\n')[:-2])
            await call.edit(
                text=response,
                reply_markup=[
                    [
                        {
                            "text": "📋 Профиль",
                            "callback": self.stor_prof,
                        },
                        {
                            'text': '📈 Статистика',
                            'callback': self.stor_stata,
                        }
                    ],
                    [
                        {
                            "text": "> 🎒 Инвентарь <",
                            "callback": self.stor_inv,
                        },
                    ],
                    [
                        {
                            'text': '🌌 Звездная Пыль',
                            'callback': self.stor_star
                        }
                    ],
                    [
                        {
                            'text':'📦 Кейсы',
                            'callback':self.stor_cases,
                        },
                        {
                            'text':'⚡️ Бустеры',
                            'callback':self.stor_boosters,
                        }
                    ],
                    [
                        {
                            "text": "🎆 Плазма",
                            "callback": self.stor_plasm,
                        },
                        {
                            "text": "💵 Баланс",
                            "callback": self.stor_balance,
                        },
                        {
                            "text": "🔩 Скрап",
                            "callback": self.stor_scrap,
                        }
                    ],
                    [
                        {
                            'text':'💰 Поддержать автора ( 1 кейс )',
                            'callback': self.donate_author,
                        },
                    ],      
                    [
                        {
                        "text": "🔻 Закрыть",
                        "action": "close",
                        }
                    ],
                ],
            )            

    async def stor_cases(self, call: InlineCall):
        async with self.client.conversation(self._backup_channel) as conv:
            await conv.send_message('кейсы')
            response = (await conv.get_response()).message
            links_regex = re.compile(r'.(https?://\S+).')
            response = links_regex.sub('', response)
            if re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', response):
                response = '\n'.join(response.split('\n')[:-2])
            await call.edit(
                text=response,
                reply_markup=[
                    [
                        {
                            "text": "📋 Профиль",
                            "callback": self.stor_prof,
                        },
                        {
                            'text': '📈 Статистика',
                            'callback': self.stor_stata,
                        }
                    ],
                    [
                        {
                            "text": "🎒 Инвентарь",
                            "callback": self.stor_inv,
                        },
                    ],
                    [
                        {
                            'text': '🌌 Звездная Пыль',
                            'callback': self.stor_star
                        }
                    ],
                    [
                        {
                            'text':'> 📦 Кейсы <',
                            'callback':self.stor_cases,
                        },
                        {
                            'text':'⚡️ Бустеры',
                            'callback':self.stor_boosters,
                        }
                    ],
                    [
                        {
                            "text": "🎆 Плазма",
                            "callback": self.stor_plasm,
                        },
                        {
                            "text": "💵 Баланс",
                            "callback": self.stor_balance,
                        },
                        {
                            "text": "🔩 Скрап",
                            "callback": self.stor_scrap,
                        }
                    ],
                    [
                        {
                            'text':'💰 Поддержать автора ( 1 кейс )',
                            'callback': self.donate_author,
                        },
                    ],   
                    [
                        {
                        "text": "🔻 Закрыть",
                        "action": "close",
                        }
                    ],
                ],
            )     

    async def stor_boosters(self, call: InlineCall):
        async with self.client.conversation(self._backup_channel) as conv:
            await conv.send_message('бусты')
            response = (await conv.get_response()).message
            links_regex = re.compile(r'.(https?://\S+).')
            response = links_regex.sub('', response)
            if re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', response):
                response = '\n'.join(response.split('\n')[:-2])
            await call.edit(
                text=response,
                reply_markup=[
                    [
                        {
                            "text": "📋 Профиль",
                            "callback": self.stor_prof,
                        },
                        {
                            'text': '📈 Статистика',
                            'callback': self.stor_stata,
                        }
                    ],
                    [
                        {
                            "text": "🎒 Инвентарь",
                            "callback": self.stor_inv,
                        },
                    ],
                    [
                        {
                            'text': '🌌 Звездная Пыль',
                            'callback': self.stor_star
                        }
                    ],
                    [
                        {
                            'text':'📦 Кейсы',
                            'callback':self.stor_cases,
                        },
                        {
                            'text':'> ⚡️ Бустеры <',
                            'callback':self.stor_boosters,
                        }
                    ],
                    [
                        {
                            "text": "🎆 Плазма",
                            "callback": self.stor_plasm,
                        },
                        {
                            "text": "💵 Баланс",
                            "callback": self.stor_balance,
                        },
                        {
                            "text": "🔩 Скрап",
                            "callback": self.stor_scrap,
                        }
                    ],
                    [
                        {
                            'text':'💰 Поддержать автора ( 1 кейс )',
                            'callback': self.donate_author,
                        },
                    ],      
                    [
                        {
                        "text": "🔻 Закрыть",
                        "action": "close",
                        }
                    ],
                ],
            )                   

    async def stor_plasm(self, call: InlineCall):
        async with self.client.conversation(self._backup_channel) as conv:
            await conv.send_message('п')
            response = (await conv.get_response()).message
            links_regex = re.compile(r'.(https?://\S+).')
            response = links_regex.sub('', response)
            if re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', response):
                response = '\n'.join(response.split('\n')[:-2])
            await call.edit(
                text=response,
                reply_markup=[
                    [
                        {
                            "text": "📋 Профиль",
                            "callback": self.stor_prof,
                        },
                        {
                            'text': '📈 Статистика',
                            'callback': self.stor_stata,
                        }
                    ],
                    [
                        {
                            "text": "🎒 Инвентарь",
                            "callback": self.stor_inv,
                        },
                    ],
                    [
                        {
                            'text': '🌌 Звездная Пыль',
                            'callback': self.stor_star
                        }
                    ],
                    [
                        {
                            'text':'📦 Кейсы',
                            'callback':self.stor_cases,
                        },
                        {
                            'text':'⚡️ Бустеры',
                            'callback':self.stor_boosters,
                        }
                    ],
                    [
                        {
                            "text": "> 🎆 Плазма <",
                            "callback": self.stor_plasm,
                        },
                        {
                            "text": "💵 Баланс",
                            "callback": self.stor_balance,
                        },
                        {
                            "text": "🔩 Скрап",
                            "callback": self.stor_scrap,
                        }
                    ],
                    [
                        {
                            'text':'💰 Поддержать автора ( 1 кейс )',
                            'callback': self.donate_author,
                        },
                    ],  
                    [
                        {
                        "text": "🔻 Закрыть",
                        "action": "close",
                        }
                    ],
                ],
            )          

    async def stor_balance(self, call: InlineCall):
        async with self.client.conversation(self._backup_channel) as conv:
            await conv.send_message('б')
            response = (await conv.get_response()).message
            links_regex = re.compile(r'.(https?://\S+).')
            response = links_regex.sub('', response)
            if re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', response):
                response = '\n'.join(response.split('\n')[:-2])
            await call.edit(
                text=response,
                reply_markup=[
                    [
                        {
                            "text": "📋 Профиль",
                            "callback": self.stor_prof,
                        },
                        {
                            'text': '📈 Статистика',
                            'callback': self.stor_stata,
                        }
                    ],
                    [
                        {
                            "text": "🎒 Инвентарь",
                            "callback": self.stor_inv,
                        },
                    ],
                    [
                        {
                            'text': '🌌 Звездная Пыль',
                            'callback': self.stor_star
                        }
                    ],
                    [
                        {
                            'text':'📦 Кейсы',
                            'callback':self.stor_cases,
                        },
                        {
                            'text':'⚡️ Бустеры',
                            'callback':self.stor_boosters,
                        }
                    ],
                    [
                        {
                            "text": "🎆 Плазма",
                            "callback": self.stor_plasm,
                        },
                        {
                            "text": "> 💵 Баланс <",
                            "callback": self.stor_balance,
                        },
                        {
                            "text": "🔩 Скрап",
                            "callback": self.stor_scrap,
                        }
                    ],
                    [
                        {
                            'text':'💰 Поддержать автора ( 1 кейс )',
                            'callback': self.donate_author,
                        },
                    ],   
                    [
                        {
                        "text": "🔻 Закрыть",
                        "action": "close",
                        }
                    ],
                ],
            )              

    async def stor_scrap(self, call: InlineCall):
        async with self.client.conversation(self._backup_channel) as conv:
            await conv.send_message('с')
            response = (await conv.get_response()).message
            links_regex = re.compile(r'.(https?://\S+).')
            response = links_regex.sub('', response)
            if re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', response):
                response = '\n'.join(response.split('\n')[:-2])
            await call.edit(
                text=response,
                reply_markup=[
                    [
                        {
                            "text": "📋 Профиль",
                            "callback": self.stor_prof,
                        },
                        {
                            'text': '📈 Статистика',
                            'callback': self.stor_stata,
                        }
                    ],
                    [
                        {
                            "text": "🎒 Инвентарь",
                            "callback": self.stor_inv,
                        },
                    ],
                    [
                        {
                            'text': '🌌 Звездная Пыль',
                            'callback': self.stor_star
                        }
                    ],
                    [
                        {
                            'text':'📦 Кейсы',
                            'callback':self.stor_cases,
                        },
                        {
                            'text':'⚡️ Бустеры',
                            'callback':self.stor_boosters,
                        }
                    ],
                    [
                        {
                            "text": "🎆 Плазма",
                            "callback": self.stor_plasm,
                        },
                        {
                            "text": "💵 Баланс",
                            "callback": self.stor_balance,
                        },
                        {
                            "text": "> 🔩 Скрап <",
                            "callback": self.stor_scrap,
                        }
                    ],
                    [
                        {
                            'text':'💰 Поддержать автора ( 1 кейс )',
                            'callback': self.donate_author,
                        },
                    ],   
                    [
                        {
                        "text": "🔻 Закрыть",
                        "action": "close",
                        }
                    ],
                ],
            )            

    async def stor_star(self, call: InlineCall):
        async with self.client.conversation(self._backup_channel) as conv:
            await conv.send_message('зп')
            response = (await conv.get_response()).message
            links_regex = re.compile(r'.(https?://\S+).')
            response = links_regex.sub('', response)
            if re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', response):
                response = '\n'.join(response.split('\n')[:-2])
            await call.edit(
                text=response,
                reply_markup=[
                    [
                        {
                            "text": "📋 Профиль",
                            "callback": self.stor_prof,
                        },
                        {
                            'text': '📈 Статистика',
                            'callback': self.stor_stata,
                        }
                    ],
                    [
                        {
                            "text": "🎒 Инвентарь",
                            "callback": self.stor_inv,
                        },
                    ],
                    [
                        {
                            'text': '> 🌌 Звездная Пыль <',
                            'callback': self.stor_star
                        }
                    ],
                    [
                        {
                            'text':'📦 Кейсы',
                            'callback':self.stor_cases,
                        },
                        {
                            'text':'⚡️ Бустеры',
                            'callback':self.stor_boosters,
                        }
                    ],
                    [
                        {
                            "text": "🎆 Плазма",
                            "callback": self.stor_plasm,
                        },
                        {
                            "text": "💵 Баланс",
                            "callback": self.stor_balance,
                        },
                        {
                            "text": "🔩 Скрап",
                            "callback": self.stor_scrap,
                        }
                    ],
                    [
                        {
                            'text':'💰 Поддержать автора ( 1 кейс )',
                            'callback': self.donate_author,
                        },
                    ],      
                    [
                        {
                        "text": "🔻 Закрыть",
                        "action": "close",
                        }
                    ],
                ],
            )            

    async def donate_author(self, call: InlineCall):
        await self.client.send_message('@mine_evo_bot','Дать # к 1')
        await call.answer('Спасибо ❤️')
