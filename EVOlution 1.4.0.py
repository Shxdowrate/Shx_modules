#—————————————————————————————————————————————————————————————————————————————————
#  █▀ █ █ ▀▄▀   █▀▄▀█ █▀█ █▀▄ █ █ █   █▀▀ █▀ Chanel: https://shx_modules
#  ▄█ █▀█ █ █   █ ▀ █ █▄█ █▄▀ █▄█ █▄▄ ██▄ ▄█ Not Licensed
#—————————————————————————————————————————————————————————————————————————————————
#  █▀▀ ▀▄▀ █   █ █ █▀ █ █ █ █▀▀   █▀▄▀█ █▀█ █▀▄ █ █ █   █▀▀ █▀
#  ██▄ █ █ █▄▄ █▄█ ▄█ █ ▀▄▀ ██▄   █ ▀ █ █▄█ █▄▀ █▄█ █▄▄ ██▄ ▄█
#—————————————————————————————————————————————————————————————————————————————————
# Idea: sqlmerr
# meta developer: @shx_modules
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
    """Модуль для управления аккаунтом mine_evo_bot.t.me\nDeveloper: @Shx_modules\n\nО багах/предложениях: @Shxdowrate"""
    strings = {
        "name" : "EVOlution 1.4.0",
        "cfg_waiting_time" : "Время ожидания ответа от бота\nДля .evo",
        'delay_craft' : 'Задержка между отправкой запроса на крафт бустера\nДля .craft',
        'autoattack' : 'Автоматическая атака боссов\nУчтите, вам нужно выбрать босса, а бот продолжит его атаковать',
        'delay_boss' : 'Задержка между отправкой атаки',
        'result_attack' : 'Отправлять ли результат боя к вам в избранные?\nРаботает только при включенном autoattack',
        'gif_inline' : 'Гиф в inline топе и профиле.',
        'petroleum' : 'Добывать нефть автоматически?\nВключайте через .petroleum!',
        'thank_you': "Отправлять ли при следующем включение благодарственное письмо в лс?",
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
        thank = self.config['thank_you']
        if thank == True:
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
                "thank_you", True,
                lambda: self.strings("thank_you"),
                validator=loader.validators.Boolean()
            ),
        )

    @loader.watcher()
    async def watcher2(self, message):
        autoattack = self.config['autoattack']
        delay_boss = self.config['delay_boss']
        result_attack = self.config['result_attack']
        petroleum = self.config['petroleum']
        

        if autoattack == True:
            if message.chat_id == 5522271758 and "Атк)" in message.raw_text:
                await asyncio.sleep(delay_boss)
                await self.client.send_message('@mine_evo_bot', 'Атк')    
            elif message.chat_id == 5522271758 and '🔶 Ты выбрал босса:' in message.raw_text:
                await asyncio.sleep(delay_boss)
                await self.client.send_message('@mine_evo_bot', 'Атк')    
            if result_attack == True:
                if message.chat_id == 5522271758 and "Твоя награда:" in message.raw_text: 
                    await self.client.send_message('me', message.raw_text)
        if petroleum == True:
            if message.chat_id == 5522271758 and "Нефти в месторождении:" in message.raw_text:
                await asyncio.sleep(2)
                await self.client.send_message('@mine_evo_bot', 'Качать')
            if message.chat_id == 5522271758 and "кончилась нефть!" in message.raw_text:
                await asyncio.sleep(3600)
                await self.client.send_message('@mine_evo_bot', "Качать")
                
    @loader.command()
    async def evo(self, message: Message):
        """[ Запрос ] - отправить запрос\nПример: .evo проф"""
        args = utils.get_args_raw(message)
        waiting_time = self.config["waiting_time"]
        error_not_args = "<emoji document_id=5877477244938489129>🚫</emoji> <b>Error | Ошибка </b>\nВы не ввели запрос!"
        error_not_response = f"<emoji document_id=5877477244938489129>🚫</emoji> <b>Error | Ошибка</b>\nНа ваш запрос не был получен ответ в течение {waiting_time} секунд(-ы)\n<b>Ваш запрос:</b> {args} \n\n<emoji document_id=5787544344906959608>ℹ️</emoji> <b>Возможные проблемы:</b>"
        ore = "<b>Цены на руды:</b>\n> https://teletype.in/@mine_evo/ores_prices_1"
        err_d1 = "\n> Вы ввели запрос, которого не существует."
        err_d2 = "\n> У MineEVO высокий пинг."

        if args == '':
            await utils.answer(message, error_not_args)
        elif args in ["Цены","цены","рынок","Рынок"]:
            await utils.answer(message, ore)
        else:
            await utils.answer(message, '<b>[ evo ]</b> Выполняется...')
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
        """[ Ничего/Название топика ] - Вывести помощь по всем командам, которые поддерживаются модулем"""
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
        """[ Тип бустера ( р / д ) ] [ Множитель ] [ Кол-во ] - автоматический крафт бустеров"""
        await utils.answer(message, '<b>[ Craft ]</b> Начинаю крафт бустеров...\n\nПодготовка данных... [ args, delay, type, mult, quantity, quantityl, errtype, errmult, startcraft ]')
        args = utils.get_args_split_by(message, " ")
        delay = self.config["delay_craft"]
        type = args[0]
        mult = args[1]
        quantity = args[2]
        quantityl = quantity
        errtype = f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error | Ошибка </b>\nТип бустера "{type}" не найден.\nМожно крафстить только бустеры:\nР, р - руда\nД, д - деньги'
        errmult = f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error | Ошибка </b>\nМножителя "{mult}" не существует.\nИспользуйте: 2, 2.0, 2.5, 3, 3.0'
        startcraft = 0
        await utils.answer(message, '<b>[ Craft ]</b> Начинаю крафт бустеров...\n\nПодготовка данных... [ args, delay, type, mult, quantity, quantityl, errtype, errmult, startcraft ] \n\nКрафтим...')
        if type in ['Р', 'р', 'Д', 'д' ]:
            if mult in ['2', '2.0', '2.5', '3', '3.0']:
                while int(quantity) > 0:
                    quantity = int(quantity) - 1
                    async with self.client.conversation(self._backup_channel) as conv:   
                        await conv.send_message(f'Крафт {type} {mult}')
                        await asyncio.sleep(delay)
                        startcraft = startcraft + 1
                        await utils.answer(message, f'<b>[ Craft ]</b> Начинаю крафт бустеров...\n\nПодготовка данных... [ args, delay, type, mult, quantity, quantityl, errtype, errmult, startcraft ] \n\nКрафтим...\n\nОтправлено запросов на данный момент: {startcraft}')
                await asyncio.sleep(2)    
                async with self.client.conversation(self._backup_channel) as conv:   
                        await conv.send_message(f'Бусты')
                        response = (await conv.get_response()).message
                        response = response[:-2]
                await utils.answer(message, '<b>[ Craft ]</b> Крафт завершен!\n\n\n<code>Загрузка информации...</code>')
                await asyncio.sleep(1)
                if type == 'д':
                    type = 'Деньги'
                elif type == 'р':
                    type = 'Руда'
                await utils.answer(message, f"<b>[ Craft ]</b> Крафт завершен!\n\n<b>Информация:</b>\nТип бустера: {type}\nМножитель бустера: {mult}\nКол-во раз отправлено: {quantityl}\nБыла задержка: {delay}\n\n<b>Итоговый список бустеров:</b>\n{response}")
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
        ''' - включить\выключить автоатакер'''
        self.config['autoattack'] = not self.config['autoattack']
        cfg = self.config['autoattack']
        if cfg == True:
            await utils.answer(message, '<b>[ AutoAttack ] </b>АвтоАтакер включен.')
        if cfg == False:
            await utils.answer(message, '<b>[ AutoAttack ] </b>АвтоАтакер отключен.')

    @loader.command(alias = 'pt')
    async def petroleum(self, message):
        ''' - включить/выключить автодобычу нефти'''
        self.config['petroleum'] = not self.config['petroleum']
        cfg = self.config['petroleum']
        if cfg == True:
            await utils.answer(message, '<b>[ Petroleum ]</b> Автодобыча нефти включена.')
            await self.client.send_message('@mine_evo_bot', 'Качать')
        if cfg == False:
            await utils.answer(message, '<b>[ Petroleum ]</b> Автодобыча нефти отключена.')

    @loader.command()
    async def scfg(self, message):
        '''[ delay_craft / delay_boss / gif_inline / waiting_time ] [ Значение ]- изменить параметр без открытия конфига\ndelay_craft - изменить задержку для крафта\ndelay_boss - изменить задержку атаки босса\ngif_inline - изменить гиф в инлайн функциях\nwaiting_time - время ожидания ответа от бота для evo'''
        args = utils.get_args_raw(message).split(" ")
        param = args[0]
        zz = args[1]

        if param == 'delay_boss':
            self.config['delay_boss'] = zz
            await utils.answer(message, f'<b>[ Config ] </b>Параметр <code>{param}</code> изменен на <code>{zz}</code>')
            return
        if param == 'delay_craft':
            self.config['delay_craft'] = zz
            await utils.answer(message, f'<b>[ Config ] </b>Параметр <code>{param}</code> изменен на <code>{zz}</code>')
            return
        if param == 'gif_inline':
            self.config['gif_inline'] = zz
            await utils.answer(message, f'<b>[ Config ] </b>Параметр <code>{param}</code> изменен на <code>{zz}</code>')
            return
        if param == 'waiting_time':
            self.config['waiting_time'] = zz
            await utils.answer(message, f'<b>[ Config ] </b>Параметр <code>{param}</code> изменен на <code>{zz}</code>')
            return
        else:
            await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error | Ошибка</b>\nПараметр <code>{param}</code> не найден.')


    @loader.command()
    async def upd(self, message):
        '''[ Название улучшения ( пример: Шп ) ] - улучшить что-либо'''
        args = utils.get_args_raw(message)
        if args in ['Ур','ур','Мщ','мщ','Уд','уд','Урон','урон','Крит','крит','Шп','шп','Уп','уп','Шк','шк','Мр','мр','Мп','мп','Мэ','мэ','Му','му']:
            await utils.answer(message, '<b>[ upd ]</b> Выполняется...')
            async with self.client.conversation(self._backup_channel) as conv:
                await conv.send_message(f'{args}')
                res = await conv.get_response()
                await res.click(0)
            await utils.answer(message, f'Вот, что нужно было для улучшения:\n\n{res}')
            return
        else:
            await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error | Ошибка</b>\nУлучшение <code>{args}<code> не найдено.')

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