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

from asyncio import sleep

from .. import loader, utils


logger = logging.getLogger(__name__)

@loader.tds
class EVOH(loader.Module):
    """Модуль для управления аккаунтом t.me/mine_evo_bot\nDeveloper: @Shx_modules"""
    strings = {
        "name": "EVOH",
        "cfg_waiting_time": "Время ожидания ответа от бота"
    }
    
    


    async def client_ready(self):
        self._backup_channel, _ = await utils.asset_channel(
            self._client,
            "EVOQasst",
            "Группа для работы модуля EVOQ от @Shx_modules\nНе добавляйте сюда других людей или ботов!",
            silent=True,
            archive=True,
            _folder="hikka",
        )

        await self.client(functions.channels.InviteToChannelRequest(self._backup_channel, ['@mine_evo_bot']))
        await self.client(functions.channels.EditAdminRequest(
                channel=self._backup_channel,
                user_id="@mine_evo_bot",
                admin_rights=ChatAdminRights(ban_users=True, post_messages=True, edit_messages=True),
                rank="EVOQ",
            )
        )

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "waiting_time", 1.0,
                lambda: self.strings("cfg_waiting_time"),
                validator=loader.validators.Float()
            )
        )
    

    @loader.command()
    async def evo(self, message: Message):
        """[ Запрос ] - отправить запрос\nПример: .evo проф"""
        args = utils.get_args_raw(message)
        waiting_time = self.config["waiting_time"]
        error_not_args = "<emoji document_id=5877477244938489129>🚫</emoji> <b>Error | Ошибка </b>\nВы не ввели запрос!"
        error_not_response = f"<emoji document_id=5877477244938489129>🚫</emoji> <b>Error | Ошибка</b>\nНа ваш запрос не был получен ответ в течение {waiting_time} секунд(-ы)\n\n<emoji document_id=5787544344906959608>ℹ️</emoji> <b>Возможные проблемы:</b>"
        ore = "<b>Цены на руды:</b>\n> https://teletype.in/@mine_evo/ores_prices_1"
        err_d1 = "\n> Вы ввели запрос, которого не существует."
        err_d2 = "\n> У MineEVO высокий пинг."

        if args == '':
            await utils.answer(message, error_not_args)
        
        elif args in ["Цены","цены","рынок","Рынок"]:
            await utils.answer(message, ore)
        else:
            await utils.answer(message, 'Выполняется...')
            async with self._client.conversation(self._backup_channel) as conv:
                await conv.send_message(f'{args}')
                try:
                    response = await asyncio.wait_for(conv.get_response(), timeout=waiting_time)
                except asyncio.TimeoutError:
                    await utils.answer(message, error_not_response + err_d1 + err_d2)
                    return
            links_regex = re.compile(r'.(https?://\S+).')
            response.text = links_regex.sub('', response.text)
            links = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', response.text)
            for link in links:
                response.text = response.text.replace(link, '')
            await utils.answer(message, response.text)


    @loader.command()
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
        cmdboost = "  > Буст [ Тип бустера ][ Множитель ]\n    > р | д | гр | гд\n    > 1.5 | 2 | 2.5 | 3\n  > Бусты\n  > Крафт [ Тип бустера ] [ Множитель ]\n    > р | д\n    > 2 | 2.5 | 3\n  > Утиль [ Тип бустера] [ Множитель ]\n    > р | д\n    > 1.5 | 2 | 2.5 | 3\n  > Время\n\n"
        cmdcases = "  > Кейсы\n  > Открыть [ Тип кейса ] [ Кол-во ]\n    > Кт | Ркт | К | Рк | Миф | Кр | Зв \n  > Дать [ Тип кейса ][ Кол-во ]\n    > Кт | Ркт | К | Рк | Миф | Кр | Зв\n  > Открыть [ Тип кейса ][ Кол-во ]\n    > Кт | Ркт | К | Рк | Миф | Кр | Зв \n\n"
        cmdtop = "  > Топ\n  > Топ [ Тип топа ]\n    >  к | д | б | р | клан\n\n"
        cmdstats = "  > Проф \n  > Стата \n  > Лим\n  > Мой реф\n\n"
        cmdstorage = "  > Б\n  > П\n  > C\n  > Зп\n  > Инв\n  > Продать [ Название руды ] [ Кол-во/Все ]\n  > Перевести [ Ник ][ Кол-во денег/Лимит ]\n\n"
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