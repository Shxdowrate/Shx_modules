from .. import loader, utils
import asyncio 
from asyncio import sleep

__version__ = (1, 0, 0)

class unoca(loader.Module):
    '''Возможность безлимитного открытия кейсов в MineEVO\nDeveloper: @shx_modules'''

    strings = {
        'name':'unoca'
    }
    
    async def client_ready(self):
        self.set('opst', False)
    @loader.command()
    async def usetgroup(self, message):
        ''' - установить группу для открытия кейсов'''
        if message.is_private:

            await message.edit("<emoji document_id=5210952531676504517>🚫</emoji> | Это не группа.")
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
        self.set('group', chat)
        await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji> | Группа <code>{chat}</code> установлена, как чат для открытия кейсов.")

    @loader.command()
    async def usettings(self, message):
        ''' - настройки модуля'''
        args = utils.get_args_raw(message)
        prefix = utils.escape_html(self.get_prefix())
        if not args:

            mylimit = self.get('mylimit')
            sleeptime = self.get('sleeptime')

            await utils.answer(message, f'<emoji document_id=5328239124933515868>⚙️</emoji> | <b>Настройки модуля unoca:</b>\n\n<code>{prefix}usettings s1</code> [ Лимит ] - установить лимит открытия кейсов за раз.\n   Текущий: {mylimit}\n<code>{prefix}usettings s2</code> [ Секунды ] - указать, раз в сколько секунд открывать кейсы.\n   Текущий: {sleeptime}')
            return
        if args:

            if ' ' in args:

                args = args.split()
                if args[0] == 's1':

                    limit = int(args[1])
                    self.set('mylimit', limit)
                    await utils.answer(message, f'<emoji document_id=5332533929020761310>✅</emoji> | Параметр limit изменен на <code>{limit}</code>.')
                    return
                if args[0] == 's2':

                    sleeptime = int(args[1])
                    self.set('sleeptime', sleeptime)
                    await utils.answer(message, f'<emoji document_id=5332533929020761310>✅</emoji> | Параметр sleeptime изменен на <code>{sleeptime}</code>.')
                    return

    @loader.command()
    async def uoc(self, message):
        '''[ Тип ] [ Кол-во ] - открытие кейсов'''
        args = utils.get_args_raw(message)
        prefix = utils.escape_html(self.get_prefix())
        if not args:

            await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error |</b> <code>{prefix}uoc</code>\nЧто мне делать? Ты бы хоть написал, вот, попробуй: <code>{prefix}uoc ркт 20</code>')
            return
        elif args:

            opst = self.get('opst')
            args = args.lower()
            if ' ' in args:

                args = args.split()
                if len(args) == 2:

                    if args[0] in ['кт','ркт','к','рк','миф','кр','зв']:

                        if args[1].isdigit():

                            if opst == False:
                                val = int(args[1])
                                textval = val
                                await utils.answer(message, f'<emoji document_id=5332533929020761310>✅</emoji> | Открытие кейсов началось.\nОсталось открыть <code>{textval}</code> {args[0]}')
                                limit = self.get('mylimit')
                                if val > limit:
                                    sleeptime = self.get('sleeptime')
                                    gval = val/limit
                                    gval = int(gval)
                                    tval = val%limit
                                    self.set('opst', True)
                                    await asyncio.sleep(sleeptime)
                                    while gval > 0:

                                        
                                        chat = self.get('group')
                                        await self.client.send_message(chat, f'Отк {args[0]} {limit}')
                                        gval -= 1
                                        textval -= limit
                                        await utils.answer(message, f'<emoji document_id=5332533929020761310>✅</emoji> | Открытие кейсов началось.\nОсталось открыть <code>{textval}</code> {args[0]}')
                                        await asyncio.sleep(sleeptime)
                                    await self.client.send_message(chat, f'Отк {args[0]} {tval}')
                                    await utils.answer(message, f'<emoji document_id=5332533929020761310>✅</emoji> | Все {val} {args[0]} открыты.')
                                    self.set('opst', False)
                                    return
                                else:
                                    await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error |</b> <code>{prefix}uoc</code>\nЭй, ты хочешь открыть {val} {args[0]}, когда твой лимит {limit}? Подними свою задницу и открой кейсы вручную, я что, должен все делать за тебя?')
                            else:
                                await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error |</b> <code>{prefix}uoc</code>\nМы пытались открывать кейсы, но... Они уже открываются. Подождите, пожалуйста.')
                                return
                        else:
                            await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error |</b> <code>{prefix}uoc</code>\nЯ хотел уже начать открывать кейсы, но... Ты в кол-во указал не цифры, как мне понять, что ты от меня хочешь, друг? Попробуй написать <code>{prefix}uoc ркт 20</code>, тогда я может быть выполню это.')
                            return
                    else:
                        await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error |</b> <code>{prefix}uoc</code>\nОткрывать что? {args[0]}? Это что вообще? Прости, но я готов открывать только <code>кт, ркт, к, рк, миф, кр, зв...</code>')
                        return
                else:
                    await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error |</b> <code>{prefix}uoc</code>\nСколько-сколько? Эээ, куда столько аргументов, мне всего 2 надо...')
                    return
            else:
                await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error |</b> <code>{prefix}uoc</code>\nНу камон... Друг... Вот ты написал мне один аргумент и как я должен понять, чего ты хочешь от меня? Вот, попробуй: <code>{prefix}uoc ркт 20</code>')
                return
        

                    
# await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error |</b> <code>{prefix}uoc</code>\nВы указали больше двух аргументов, хотя команда расчитана только на два аргумента.')
#                     return