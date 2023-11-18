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
__version__ = (1, 0, 0)

from .. import loader
import asyncio
from asyncio import sleep
from ..inline.types import InlineCall

@loader.tds
class OilDrill(loader.Module):
    '''Автоматическая добыча нефти\nDeveloper: @mescr_m'''
    strings = {
        'name': 'Oil Drill',
        'module':'Включение модуля через .od',
        'delay_fuel': 'Через сколько минут пробовать качать, если топлива нет?',
        'delay_ex_fuel': 'Через сколько секунд качать, если топливо есть?',
        'warning': 'Говорить ли вам о том, что ваше хранилище заполнено топливом?'
    }

    async def client_ready(self):
        if self.config['module'] == True:
            await self.client.send_message(5522271758, 'Качать')
        

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "module", False,
                lambda: self.strings("module"),
                validator=loader.validators.Boolean()
            ),
            loader.ConfigValue(
                "delay_fuel", 60,
                lambda: self.strings("delay_fuel"),
                validator=loader.validators.Integer(minimum=60)
            ),
            loader.ConfigValue(
                "delay_ex_fuel", 5.0,
                lambda: self.strings("delay_ex_fuel"),
                validator=loader.validators.Float(minimum=2.0)
            ),
            loader.ConfigValue(
                "warning", False,
                lambda: self.strings("warning"),
                validator=loader.validators.Boolean()
            ),
        )
            
    @loader.watcher()
    async def WatcherExFuel(self, message):
        exdelay = self.config['delay_ex_fuel']
        dela = self.config['delay_fuel']
        module = self.config['module']
        warning = self.config['warning']
        delay = dela * 60
        if module == True:
            if "Бочка топлива" in message.raw_text:
                if message.chat_id == 5522271758:
                    if module == True:
                        await asyncio.sleep(exdelay)
                        await self.client.send_message(message.chat_id, 'Качать')
                        return
                    return
            if 'кончилась нефть!' in message.raw_text:
                if message.chat_id == 5522271758:
                    await asyncio.sleep(delay)
                    await self.client.send_message(message.chat_id, 'Качать')
                    return
                return
            if 'заполнено топливом!' in message.raw_text:
                if message.chat_id == 5522271758:
                    if warning == True:
                        await asyncio.sleep(2)
                        await self.client.send_message('me','<emoji document_id=5397866729554583012>❗️</emoji> <b>Warning | ExFuel</b>\nВаше хранилище заполнено топливом!')
                        await asyncio.sleep(delay)
                        await self.client.send_message(message.chat_id, 'Качать')
                        return
                    if warning == False:
                        await asyncio.sleep(delay)
                        await self.client.send_message(message.chat_id, 'Качать')
                        return
                    return
                return
            if '/checkod' in message.raw_text:
                if message.from_id == 5195118663:
                    await self.client.send_message(message.chat_id, 'evo')
                    return

            
                    
   
        
    @loader.command(alias = 'od')    
    async def oildrill(self, message):
        ''' - меню нефтяной скважины'''
        status = self.config['module']
        if status == True:
            await self.inline.form(
                text = '<b>Меню вашей нефтяной скважины:</b>\n\n<b>Статус:</b> Включена ',
                photo = 'https://te.legra.ph/file/616bc1bffbf6003babbd1.jpg',
                message=message,
                reply_markup=[
                    [
                        {
                            "text": "🛢 Запустить / остановить скважину",
                            "callback": self.status_drill,
                        }
                    ],
                    [
                        {
                            "text": "⚙️ Настройки скважины",
                            "callback": self.cfg_drill,
                        },
                    ],
                    [
                        {
                            'text':'💰 Поддержать автора',
                            'callback': self.donate_author,
                        }
                    ],
                    [
                        {
                            'text':'🔻 Закрыть меню',
                            'action': 'close'
                        }
                    ],
                    
                ]
            )
            return
        if status == False:
            await self.inline.form(
                text = '<b>Меню вашей нефтяной скважины:</b>\n\n<b>Статус:</b> Отключена ',
                photo = 'https://te.legra.ph/file/616bc1bffbf6003babbd1.jpg',
                message=message,
                reply_markup=[
                    [
                        {
                            "text": "🛢 Запустить / остановить скважину",
                            "callback": self.status_drill,
                        }
                    ],
                    [
                        {
                            "text": "⚙️ Настройки скважины",
                            "callback": self.cfg_drill,
                        },
                    ],
                    [
                        {
                            'text':'💰 Поддержать автора',
                            'callback': self.donate_author,
                        }
                    ],
                    [
                        {
                            'text':'🔻 Закрыть меню',
                            'action': 'close'
                        }
                    ],
                    
                ]
            )
            return

    async def home_drill(self, call: InlineCall):
        status = self.config['module']
        if status == True:
            await call.edit(
                text='<b>Меню вашей нефтяной скважины:</b>\n\n<b>Статус:</b> Включена ',
                reply_markup=[
                        [
                            {
                                "text": "🛢 Запустить / остановить скважину",
                                "callback": self.status_drill,
                            },
                        ],
                        [
                            {
                                "text": "⚙️ Настройки скважины",
                                "callback": self.cfg_drill,
                            },
                        ],
                        [
                            {
                                'text':'💰 Поддержать автора',
                                'callback': self.donate_author,
                            }
                        ],
                        [
                            {
                                'text':'🔻 Закрыть меню',
                                'action': 'close'
                            }
                        ],
                    ]
            )
            return
        if status == False:
            await call.edit(
                text='<b>Меню вашей нефтяной скважины:</b>\n\n<b>Статус:</b> Отключена ',
                reply_markup=[
                        [
                            {
                                "text": "🛢 Запустить / остановить скважину",
                                "callback": self.status_drill,
                            },
                        ],
                        [
                            {
                                "text": "⚙️ Настройки скважины",
                                "callback": self.cfg_drill,
                            },
                        ],
                        [
                            {
                                'text':'💰 Поддержать автора',
                                'callback': self.donate_author,
                            }
                        ],
                        [
                            {
                                'text':'🔻 Закрыть меню',
                                'action': 'close'
                            }
                        ],
                    ]
            )

    async def status_drill(self, call: InlineCall):
        self.config['module'] = not self.config['module']
        status = self.config['module']
        if status == True:
            await self.client.send_message(5522271758, 'Качать')
            await call.edit(
                text='<b>Меню вашей нефтяной скважины:</b>\n\n<b>Статус:</b> Включена  ',
                reply_markup=[
                        [
                            {
                                "text": "🛢 Запустить / остановить скважину",
                                "callback": self.status_drill,
                            },
                        ],
                        [
                            {
                                "text": "⚙️ Настройки скважины",
                                "callback": self.cfg_drill,
                            },
                        ],
                        [
                            {
                                'text':'💰 Поддержать автора',
                                'callback': self.donate_author,
                            }
                        ],
                        [
                            {
                                'text':'🔻 Закрыть меню',
                                'action': 'close'
                            }
                        ],
                    ]
            )
            return
        if status == False:
            await call.edit(
                text='<b>Меню вашей нефтяной скважины:</b>\n\n<b>Статус:</b> Отключена ',
                reply_markup=[
                        [
                            {
                                "text": "🛢 Запустить / остановить скважину",
                                "callback": self.status_drill,
                            },
                        ],
                        [
                            {
                                "text": "⚙️ Настройки скважины",
                                "callback": self.cfg_drill,
                            },
                        ],
                        [
                            {
                                'text':'💰 Поддержать автора',
                                'callback': self.donate_author,
                            }
                        ],
                        [
                            {
                                'text':'🔻 Закрыть меню',
                                'action': 'close'
                            }
                        ],
                    ]
            )
            return
        
        
    async def cfg_drill(self, call: InlineCall):
        a1 = self.config['warning']
        a2 = self.config['delay_fuel']
        a3 = self.config['delay_ex_fuel']
        if a1 == True:
            a1 = 'Включены'
        elif a1 == False:
            a1 = 'Отключены'
        await call.edit(
            text=f'<b>Меню вашей нефтяной скважины:</b> \n\n<b>Информация:\nУведомления: </b>{a1}\n<b>Переодичность копания: </b>{a2}\n<b>Переодичность добычи:</b> {a3}',
            reply_markup=[
                    [
                        {
                            "text": "🚨 Уведомления об заполненом хранилище",
                            "callback": self.warning_drill,
                        }
                    ],
                    [
                        {
                            "text": "⏲ Переодичность копания",
                            "callback": self.delay_drill,
                        },
                    ],
                    [
                        {
                            "text": "⏲ Переодичность добычи",
                            "callback": self.delay_ex_drill,
                        },
                    ],
                    [
                        {
                            "text": "🏠 Вернуться обратно",
                            "callback": self.home_drill,
                        },
                    ],
                    
                ]
        )

    async def warning_drill(self, call: InlineCall):
        self.config['warning'] = not self.config['warning']
        a1 = self.config['warning']
        a2 = self.config['delay_fuel']
        a3 = self.config['delay_ex_fuel']
        if a1 == True:
            a1 = 'Включены'
        elif a1 == False:
            a1 = 'Отключены'
        await call.edit(
            text=f'<b>Меню вашей нефтяной скважины:</b> \n\n<b>Информация:\nУведомления: </b>{a1}\n<b>Переодичность копания: </b>{a2}\n<b>Переодичность добычи:</b> {a3}',
            reply_markup=[
                    [
                        {
                            "text": "🚨 Уведомления об заполненом хранилище",
                            "callback": self.warning_drill,
                        }
                    ],
                    [
                        {
                            "text": "⏲ Переодичность копания",
                            "callback": self.delay_drill,
                        },
                    ],
                    [
                        {
                            "text": "⏲ Переодичность добычи",
                            "callback": self.delay_ex_drill,
                        },
                    ],
                    [
                        {
                            "text": "🏠 Вернуться обратно",
                            "callback": self.home_drill,
                        },
                    ],
                    
                ]
        )
        

    async def delay_drill(self, call: InlineCall):
        aaa = self.config['delay_fuel']
        await call.edit(
            text=f'Переодичность копания - раз в сколько минут будет попытка качать, если нефти нет?\n\n<b>Текущее: </b>{aaa} минут',
            reply_markup=[
                    [
                        {
                            "text": "1 час",
                            "callback": self.delay1,
                        },
                        {
                            "text": "2 часа",
                            "callback": self.delay2,
                        },
                    ],
                    [
                        {
                            "text": "5 часов",
                            "callback": self.delay5,
                        },
                        {
                            "text": "10 часов",
                            "callback": self.delay10,
                        },
                    ],
                    [
                        {
                            "text": "12 часов",
                            "callback": self.delay12,
                        },
                    ],
                    [
                        {
                            "text": "🏠 Вернуться обратно",
                            "callback": self.cfg_drill,
                        },
                    ],
                    
                ]
        )

    async def delay_ex_drill(self, call: InlineCall):
        aaa = self.config['delay_ex_fuel']
        await call.edit(
            text=f'Переодичность добычи - раз в сколько секунд скважина будет качать, если нефть есть?\n\n<b>Текущее: </b>{aaa} секунд',
            reply_markup=[
                    [
                        {
                            "text": "2 сек",
                            "callback": self.delay_ex2,
                        },
                        {
                            "text": "3 сек",
                            "callback": self.delay_ex3,
                        },
                    ],
                    [
                        {
                            "text": "5 сек",
                            "callback": self.delay_ex5,
                        },
                        {
                            "text": "10 секунд",
                            "callback": self.delay_ex10,
                        },
                    ],
                    [
                        {
                            "text": "15 секунд",
                            "callback": self.delay_ex15,
                        },
                    ],
                    [
                        {
                            "text": "🏠 Вернуться обратно",
                            "callback": self.cfg_drill,
                        },
                    ],
                    
                ]
        )
    
    async def delay1(self, call: InlineCall):
        self.config['delay_fuel'] = 60
        aaa = self.config['delay_fuel']
        await call.edit(
            text=f'Переодичность копания - раз в сколько минут будет попытка качать, если нефти нет?\n\n<b>Текущее: </b>{aaa} минут',
            reply_markup=[
                    [
                        {
                            "text": "1 час",
                            "callback": self.delay1,
                        },
                        {
                            "text": "2 часа",
                            "callback": self.delay2,
                        },
                    ],
                    [
                        {
                            "text": "5 часов",
                            "callback": self.delay5,
                        },
                        {
                            "text": "10 часов",
                            "callback": self.delay10,
                        },
                    ],
                    [
                        {
                            "text": "12 часов",
                            "callback": self.delay12,
                        },
                    ],
                    [
                        {
                            "text": "🏠 Вернуться обратно",
                            "callback": self.cfg_drill,
                        },
                    ],
                    
                ]
        )

    async def delay2(self, call: InlineCall):
        self.config['delay_fuel'] = 120
        aaa = self.config['delay_fuel']
        await call.edit(
            text=f'Переодичность копания - раз в сколько минут будет попытка качать, если нефти нет?\n\n<b>Текущее: </b>{aaa} минут',
            reply_markup=[
                    [
                        {
                            "text": "1 час",
                            "callback": self.delay1,
                        },
                        {
                            "text": "2 часа",
                            "callback": self.delay2,
                        },
                    ],
                    [
                        {
                            "text": "5 часов",
                            "callback": self.delay5,
                        },
                        {
                            "text": "10 часов",
                            "callback": self.delay10,
                        },
                    ],
                    [
                        {
                            "text": "12 часов",
                            "callback": self.delay12,
                        },
                    ],
                    [
                        {
                            "text": "🏠 Вернуться обратно",
                            "callback": self.cfg_drill,
                        },
                    ],
                    
                ]
        )

    async def delay5(self, call: InlineCall):
        self.config['delay_fuel'] = 300
        aaa = self.config['delay_fuel']
        await call.edit(
            text=f'Переодичность копания - раз в сколько минут будет попытка качать, если нефти нет?\n\n<b>Текущее: </b>{aaa} минут',
            reply_markup=[
                    [
                        {
                            "text": "1 час",
                            "callback": self.delay1,
                        },
                        {
                            "text": "2 часа",
                            "callback": self.delay2,
                        },
                    ],
                    [
                        {
                            "text": "5 часов",
                            "callback": self.delay5,
                        },
                        {
                            "text": "10 часов",
                            "callback": self.delay10,
                        },
                    ],
                    [
                        {
                            "text": "12 часов",
                            "callback": self.delay12,
                        },
                    ],
                    [
                        {
                            "text": "🏠 Вернуться обратно",
                            "callback": self.cfg_drill,
                        },
                    ],
                    
                ]
        )
        
    async def delay10(self, call: InlineCall):
        self.config['delay_fuel'] = 600
        aaa = self.config['delay_fuel']
        await call.edit(
            text=f'Переодичность копания - раз в сколько минут будет попытка качать, если нефти нет?\n\n<b>Текущее: </b>{aaa} минут',
            reply_markup=[
                    [
                        {
                            "text": "1 час",
                            "callback": self.delay1,
                        },
                        {
                            "text": "2 часа",
                            "callback": self.delay2,
                        },
                    ],
                    [
                        {
                            "text": "5 часов",
                            "callback": self.delay5,
                        },
                        {
                            "text": "10 часов",
                            "callback": self.delay10,
                        },
                    ],
                    [
                        {
                            "text": "12 часов",
                            "callback": self.delay12,
                        },
                    ],
                    [
                        {
                            "text": "🏠 Вернуться обратно",
                            "callback": self.cfg_drill,
                        },
                    ],
                    
                ]
        )

    async def delay12(self, call: InlineCall):
        self.config['delay_fuel'] = 720
        aaa = self.config['delay_fuel']
        await call.edit(
            text=f'Переодичность копания - раз в сколько минут будет попытка качать, если нефти нет?\n\n<b>Текущее: </b>{aaa} минут',
            reply_markup=[
                    [
                        {
                            "text": "1 час",
                            "callback": self.delay1,
                        },
                        {
                            "text": "2 часа",
                            "callback": self.delay2,
                        },
                    ],
                    [
                        {
                            "text": "5 часов",
                            "callback": self.delay5,
                        },
                        {
                            "text": "10 часов",
                            "callback": self.delay10,
                        },
                    ],
                    [
                        {
                            "text": "12 часов",
                            "callback": self.delay12,
                        },
                    ],
                    [
                        {
                            "text": "🏠 Вернуться обратно",
                            "callback": self.cfg_drill,
                        },
                    ],
                    
                ]
        )
        
    async def delay_ex2(self, call: InlineCall):
        self.config['delay_ex_fuel'] = 2
        aaa = self.config['delay_ex_fuel']
        await call.edit(
            text=f'Переодичность копания - раз в сколько секунд скважина будет качать, если нефть есть?\n\n<b>Текущее: </b>{aaa} секунд',
            reply_markup=[
                    [
                        {
                            "text": "2 сек",
                            "callback": self.delay_ex2,
                        },
                        {
                            "text": "3 сек",
                            "callback": self.delay_ex3,
                        },
                    ],
                    [
                        {
                            "text": "5 сек",
                            "callback": self.delay_ex5,
                        },
                        {
                            "text": "10 секунд",
                            "callback": self.delay_ex10,
                        },
                    ],
                    [
                        {
                            "text": "15 секунд",
                            "callback": self.delay_ex15,
                        },
                    ],
                    [
                        {
                            "text": "🏠 Вернуться обратно",
                            "callback": self.cfg_drill,
                        },
                    ],
                    
                ]
        )
        
    async def delay_ex3(self, call: InlineCall):
        self.config['delay_ex_fuel'] = 3
        aaa = self.config['delay_ex_fuel']
        await call.edit(
            text=f'Переодичность копания - раз в сколько секунд скважина будет качать, если нефть есть?\n\n<b>Текущее: </b>{aaa} секунд',
            reply_markup=[
                    [
                        {
                            "text": "2 сек",
                            "callback": self.delay_ex2,
                        },
                        {
                            "text": "3 сек",
                            "callback": self.delay_ex3,
                        },
                    ],
                    [
                        {
                            "text": "5 сек",
                            "callback": self.delay_ex5,
                        },
                        {
                            "text": "10 секунд",
                            "callback": self.delay_ex10,
                        },
                    ],
                    [
                        {
                            "text": "15 секунд",
                            "callback": self.delay_ex15,
                        },
                    ],
                    [
                        {
                            "text": "🏠 Вернуться обратно",
                            "callback": self.cfg_drill,
                        },
                    ],
                    
                ]
        )

    async def delay_ex5(self, call: InlineCall):
        self.config['delay_ex_fuel'] = 5
        aaa = self.config['delay_ex_fuel']
        await call.edit(
            text=f'Переодичность копания - раз в сколько секунд скважина будет качать, если нефть есть?\n\n<b>Текущее: </b>{aaa} секунд',
            reply_markup=[
                    [
                        {
                            "text": "2 сек",
                            "callback": self.delay_ex2,
                        },
                        {
                            "text": "3 сек",
                            "callback": self.delay_ex3,
                        },
                    ],
                    [
                        {
                            "text": "5 сек",
                            "callback": self.delay_ex5,
                        },
                        {
                            "text": "10 секунд",
                            "callback": self.delay_ex10,
                        },
                    ],
                    [
                        {
                            "text": "15 секунд",
                            "callback": self.delay_ex15,
                        },
                    ],
                    [
                        {
                            "text": "🏠 Вернуться обратно",
                            "callback": self.cfg_drill,
                        },
                    ],
                    
                ]
        )

    async def delay_ex10(self, call: InlineCall):
        self.config['delay_ex_fuel'] = 10
        aaa = self.config['delay_ex_fuel']
        await call.edit(
            text=f'Переодичность копания - раз в сколько секунд скважина будет качать, если нефть есть?\n\n<b>Текущее: </b>{aaa} секунд',
            reply_markup=[
                    [
                        {
                            "text": "2 сек",
                            "callback": self.delay_ex2,
                        },
                        {
                            "text": "3 сек",
                            "callback": self.delay_ex3,
                        },
                    ],
                    [
                        {
                            "text": "5 сек",
                            "callback": self.delay_ex5,
                        },
                        {
                            "text": "10 секунд",
                            "callback": self.delay_ex10,
                        },
                    ],
                    [
                        {
                            "text": "15 секунд",
                            "callback": self.delay_ex15,
                        },
                    ],
                    [
                        {
                            "text": "🏠 Вернуться обратно",
                            "callback": self.cfg_drill,
                        },
                    ],
                    
                ]
        )

    async def delay_ex15(self, call: InlineCall):
        self.config['delay_ex_fuel'] = 15
        aaa = self.config['delay_ex_fuel']
        await call.edit(
            text=f'Переодичность копания - раз в сколько секунд скважина будет качать, если нефть есть?\n\n<b>Текущее: </b>{aaa} секунд',
            reply_markup=[
                    [
                        {
                            "text": "2 сек",
                            "callback": self.delay_ex2,
                        },
                        {
                            "text": "3 сек",
                            "callback": self.delay_ex3,
                        },
                    ],
                    [
                        {
                            "text": "5 сек",
                            "callback": self.delay_ex5,
                        },
                        {
                            "text": "10 секунд",
                            "callback": self.delay_ex10,
                        },
                    ],
                    [
                        {
                            "text": "15 секунд",
                            "callback": self.delay_ex15,
                        },
                    ],
                    [
                        {
                            "text": "🏠 Вернуться обратно",
                            "callback": self.cfg_drill,
                        },
                    ],
                    
                ]
        )
        
    async def donate_author(self, call: InlineCall):
        await call.answer('❤️ Спасибо')
        await self.client.send_message('@mine_evo_bot', 'Дать # к 1')
