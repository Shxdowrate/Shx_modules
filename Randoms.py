#—————————————————————————————————————————————————————————————————————————————————
#  █▀ █ █ ▀▄▀   █▀▄▀█ █▀█ █▀▄ █ █ █   █▀▀ █▀ Chanel: https://t.me/shx_modules
#  ▄█ █▀█ █ █   █ ▀ █ █▄█ █▄▀ █▄█ █▄▄ ██▄ ▄█ Not Licensed
#—————————————————————————————————————————————————————————————————————————————————
# Idea:
# meta developer: @shx_modules
# Thanks: 
#—————————————————————————————————————————————————————————————————————————————————

__version__ = (1, 0, 0, ' beta')

from .. import utils, loader
import random
import inspect

class Randoms(loader.Module):
    '''Модуль для получения всего рандомного.\nDeveloper: @shx_modules'''

    strings = {
        'name':'Randoms',
        'sep':'Знак-разделитель для команд randval и randvals',
    }

    def __init__(self):  
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "sep", ',',
                lambda: self.strings("sep"),
                validator=loader.validators.String()
            ),
        )

    @loader.command()
    async def randint(self, message):
        '''[ от ] [ до ] - вывести случайное число в заданном диапазоне'''
        args = utils.get_args_raw(message)
        if args:
            if ' ' in args: 
                if len(args.split(' ')) == 2:
                    try:
                        int1 = int(args.split(' ')[0])
                    except ValueError:
                        await utils.answer(message, f'<emoji document_id=5980953710157632545>🚫</emoji> <b>Error</b> // <code>{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}</code>'
                        '\n\n<emoji document_id=5818973781707722673>🗣</emoji> <b><u>Суть ошибки:</u></b>\nВы ввели неправильное первое значение.'
                        '\n\n<emoji document_id=5821302890932736039>🗣</emoji> <b><u>Способы исправления:</u></b>\nВведите целочисленное значение.')
                        return
                    try:
                        int2 = int(args.split(' ')[1])
                    except ValueError:
                        await utils.answer(message, f'<emoji document_id=5980953710157632545>🚫</emoji> <b>Error</b> // <code>{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}</code>'
                        '\n\n<emoji document_id=5818973781707722673>🗣</emoji> <b><u>Суть ошибки:</u></b>\nВы ввели неправильное второе значение.'
                        '\n\n<emoji document_id=5821302890932736039>🗣</emoji> <b><u>Способы исправления:</u></b>\nВведите целочисленное значение.')
                        return
                    if int1 < int2:
                        result = random.randint(int1, int2) # Вывод результата
                        await utils.answer(message, f'<emoji document_id=5391240565679465844>⚡️</emoji> | <b>Ваш результат:</b> <code>{result}</code>')
                        return
                    else:
                        await utils.answer(message, f'<emoji document_id=5980953710157632545>🚫</emoji> <b>Error</b> // <code>{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}</code>'
                        '\n\n<emoji document_id=5818973781707722673>🗣</emoji> <b><u>Суть ошибки:</u></b>\nПервое значение должно быть меньше, чем второе.'
                        '\n\n<emoji document_id=5821302890932736039>🗣</emoji> <b><u>Способы исправления:</u></b>\nПопробуйте поменять значения местами.')
                        return
                else:
                    await utils.answer(message, f'<emoji document_id=5980953710157632545>🚫</emoji> <b>Error</b> // <code>{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}</code>'
                    '\n\n<emoji document_id=5818973781707722673>🗣</emoji> <b><u>Суть ошибки:</u></b>\nВы ввели больше аргументов, чем нужно.'
                    '\n\n<emoji document_id=5821302890932736039>🗣</emoji> <b><u>Способы исправления:</u></b>\nВведите только два аргумента.')
                    return
            else:
                await utils.answer(message, f'<emoji document_id=5980953710157632545>🚫</emoji> <b>Error</b> // <code>{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}</code>'
                '\n\n<emoji document_id=5818973781707722673>🗣</emoji> <b><u>Суть ошибки:</u></b>\nВы ввели всего один аргумент.'
                '\n\n<emoji document_id=5821302890932736039>🗣</emoji> <b><u>Способы исправления:</u></b>\nВведите два аргумента, этого требует команда.')
                return
        else:
            await utils.answer(message, f'<emoji document_id=5980953710157632545>🚫</emoji> <b>Error</b> // <code>{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}</code>'
            '\n\n<emoji document_id=5818973781707722673>🗣</emoji> <b><u>Суть ошибки:</u></b>\nВы не ввели аргументы.'
            '\n\n<emoji document_id=5821302890932736039>🗣</emoji> <b><u>Способы исправления:</u></b>\nВведите два аргумента, этого требует команда.')
            return
        
    @loader.command()
    async def randints(self, message):
        '''[ кол-во чисел ] [ от ] [ до ] - вывести несколько случайных чисел в заданном диапазоне'''
        args = utils.get_args_raw(message)
        if args:
            if ' ' in args: 
                if len(args.split(' ')) == 2:
                    await utils.answer(message, f'<emoji document_id=5980953710157632545>🚫</emoji> <b>Error</b> // <code>{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}</code>'
                    '\n\n<emoji document_id=5818973781707722673>🗣</emoji> <b><u>Суть ошибки:</u></b>\nВы указали два аргумента, эта команда требует три.'
                    '\n\n<emoji document_id=5821302890932736039>🗣</emoji> <b><u>Способы исправления:</u></b>\nУкажите три аргумента.')
                    return
                if len(args.split(' ')) < 4:
                    try:
                        qty = int(args.split(' ')[0])
                    except ValueError:
                        await utils.answer(message, f'<emoji document_id=5980953710157632545>🚫</emoji> <b>Error</b> // <code>{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}</code>'
                        '\n\n<emoji document_id=5818973781707722673>🗣</emoji> <b><u>Суть ошибки:</u></b>\nВы ввели неправильное кол-во чисел.'
                        '\n\n<emoji document_id=5821302890932736039>🗣</emoji> <b><u>Способы исправления:</u></b>\nКол-во чисел должно быть так же целочисленным значением.')
                        return
                    try:
                        int1 = int(args.split(' ')[1])
                    except ValueError:
                        await utils.answer(message, f'<emoji document_id=5980953710157632545>🚫</emoji> <b>Error</b> // <code>{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}</code>'
                        '\n\n<emoji document_id=5818973781707722673>🗣</emoji> <b><u>Суть ошибки:</u></b>\nВы ввели неправильное первое значение.'
                        '\n\n<emoji document_id=5821302890932736039>🗣</emoji> <b><u>Способы исправления:</u></b>\nВведите целочисленное значение.')
                        return
                    try:
                        int2 = int(args.split(' ')[2])
                    except ValueError:
                        await utils.answer(message, f'<emoji document_id=5980953710157632545>🚫</emoji> <b>Error</b> // <code>{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}</code>'
                        '\n\n<emoji document_id=5818973781707722673>🗣</emoji> <b><u>Суть ошибки:</u></b>\nВы ввели неправильное второе значение.'
                        '\n\n<emoji document_id=5821302890932736039>🗣</emoji> <b><u>Способы исправления:</u></b>\nВведите целочисленное значение.')
                        return
                    if qty <= 1000:
                        if int1 < int2:
                            txt = ''
                            for i in range(qty): # Вывод результата
                                result = random.randint(int1, int2)
                                txt += f'<code>{result}</code> <b>|</b> '
                            await utils.answer(message, f'<emoji document_id=5391240565679465844>⚡️</emoji> | <b>Ваш результат:</b> {txt}')
                            return
                        else:
                            await utils.answer(message, f'<emoji document_id=5980953710157632545>🚫</emoji> <b>Error</b> // <code>{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}</code>'
                            '\n\n<emoji document_id=5818973781707722673>🗣</emoji> <b><u>Суть ошибки:</u></b>\nПервое значение должно быть больше второго.'
                            '\n\n<emoji document_id=5821302890932736039>🗣</emoji> <b><u>Способы исправления:</u></b>\nПопробуйте поменять значения местами.')
                            return
                    else:
                        await utils.answer(message, f'<emoji document_id=5980953710157632545>🚫</emoji> <b>Error</b> // <code>{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}</code>'
                        '\n\n<emoji document_id=5818973781707722673>🗣</emoji> <b><u>Суть ошибки:</u></b>\nНельзя вызвать больше случайных чисел, чем 1000.'
                        '\n\n<emoji document_id=5821302890932736039>🗣</emoji> <b><u>Способы исправления:</u></b>\nВведите число меньше 1000.')
                        return
                else:
                    await utils.answer(message, f'<emoji document_id=5980953710157632545>🚫</emoji> <b>Error</b> // <code>{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}</code>'
                    '\n\n<emoji document_id=5818973781707722673>🗣</emoji> <b><u>Суть ошибки:</u></b>\nВы ввели больше аргументов, чем нужно.'
                    '\n\n<emoji document_id=5821302890932736039>🗣</emoji> <b><u>Способы исправления:</u></b>\nВведите три аргумента.')
                    return
            else:
                await utils.answer(message, f'<emoji document_id=5980953710157632545>🚫</emoji> <b>Error</b> // <code>{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}</code>'
                '\n\n<emoji document_id=5818973781707722673>🗣</emoji> <b><u>Суть ошибки:</u></b>\nВы ввели только 1 аргумент.'
                '\n\n<emoji document_id=5821302890932736039>🗣</emoji> <b><u>Способы исправления:</u></b>\nВведите три аргумента.')
                return
        else:
            await utils.answer(message, f'<emoji document_id=5980953710157632545>🚫</emoji> <b>Error</b> // <code>{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}</code>'
            '\n\n<emoji document_id=5818973781707722673>🗣</emoji> <b><u>Суть ошибки:</u></b>\nВы не указали ни единого аргумента.'
            '\n\n<emoji document_id=5821302890932736039>🗣</emoji> <b><u>Способы исправления:</u></b>\nВведите три аргумента.')
            return

    @loader.command()
    async def randword(self, message):
        '''[ слова разделенные пробелом ] - вывести случайное слово из заданных'''
        args = utils.get_args_raw(message)
        if args:
            if ' ' in args:
                words = args.split(' ')
                result = random.choice(words)
                await utils.answer(message, f'<emoji document_id=5391240565679465844>⚡️</emoji> | <b>Ваш результат:</b> <code>{result}</code>')
                return
            else:
                await utils.answer(message, f'<emoji document_id=5980953710157632545>🚫</emoji> <b>Error</b> // <code>{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}</code>'
                '\n\n<emoji document_id=5818973781707722673>🗣</emoji> <b><u>Суть ошибки:</u></b>\nВы указали лишь одно слово, хотя нужно минимум 2.'
                '\n\n<emoji document_id=5821302890932736039>🗣</emoji> <b><u>Способы исправления:</u></b>\nУкажите больше слов.')
                return
        else:
            await utils.answer(message, f'<emoji document_id=5980953710157632545>🚫</emoji> <b>Error</b> // <code>{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}</code>'
            '\n\n<emoji document_id=5818973781707722673>🗣</emoji> <b><u>Суть ошибки:</u></b>\nВы не указали ни единого аргумента.'
            '\n\n<emoji document_id=5821302890932736039>🗣</emoji> <b><u>Способы исправления:</u></b>\nВведите минимум два слова.')
            return
        
    @loader.command()
    async def randwords(self, message):
        '''[ кол-во слов ] [ слова разделенные пробелом ] - вывести несколько случайных слов из заданных'''
        args = utils.get_args_raw(message)
        if args:
            if ' ' in args:
                if len(args.split(' ')) > 2:
                    try:
                        qty = int(args.split(' ')[0])
                    except ValueError:
                        await utils.answer(message, f'<emoji document_id=5980953710157632545>🚫</emoji> <b>Error</b> // <code>{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}</code>'
                        '\n\n<emoji document_id=5818973781707722673>🗣</emoji> <b><u>Суть ошибки:</u></b>\nПервым аргументом должно быть целочисленное, обозначающее кол-во слов, которое вы хотите получить.'
                        '\n\n<emoji document_id=5821302890932736039>🗣</emoji> <b><u>Способы исправления:</u></b>\nУкажите первым аргументом целочисленное.')
                        return
                    if qty <= 1000:
                        words = args.split(' ')[1:]
                        txt = ''
                        for i in range(qty):
                            txt += f'<code>{random.choice(words)}</code> <b>|</b> '
                        await utils.answer(message, f'<emoji document_id=5391240565679465844>⚡️</emoji> | <b>Ваш результат:</b> {txt}')
                        return
                    else:
                        await utils.answer(message, f'<emoji document_id=5980953710157632545>🚫</emoji> <b>Error</b> // <code>{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}</code>'
                        '\n\n<emoji document_id=5818973781707722673>🗣</emoji> <b><u>Суть ошибки:</u></b>\nНельзя вызвать больше случайных чисел, чем 1000.'
                        '\n\n<emoji document_id=5821302890932736039>🗣</emoji> <b><u>Способы исправления:</u></b>\nВведите число меньше 1000.')
                        return
                else:
                    await utils.answer(message, f'<emoji document_id=5980953710157632545>🚫</emoji> <b>Error</b> // <code>{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}</code>'
                    '\n\n<emoji document_id=5818973781707722673>🗣</emoji> <b><u>Суть ошибки:</u></b>\nВы указали лишь два аргумента, когда необходимо минимум 3.'
                    '\n\n<emoji document_id=5821302890932736039>🗣</emoji> <b><u>Способы исправления:</u></b>\nВведите больше аргументов.')
                    return
            else:
                await utils.answer(message, f'<emoji document_id=5980953710157632545>🚫</emoji> <b>Error</b> // <code>{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}</code>'
                '\n\n<emoji document_id=5818973781707722673>🗣</emoji> <b><u>Суть ошибки:</u></b>\nВы указали лишь один аргумент, когда необходимо минимум 3.'
                '\n\n<emoji document_id=5821302890932736039>🗣</emoji> <b><u>Способы исправления:</u></b>\nВведите больше аргументов.')
                return
        else:
            await utils.answer(message, f'<emoji document_id=5980953710157632545>🚫</emoji> <b>Error</b> // <code>{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}</code>'
            '\n\n<emoji document_id=5818973781707722673>🗣</emoji> <b><u>Суть ошибки:</u></b>\nВы не указали ни единого аргумента.'
            '\n\n<emoji document_id=5821302890932736039>🗣</emoji> <b><u>Способы исправления:</u></b>\nВведите минимум 3 аргумента.')
            return
        
    @loader.command()
    async def randval(self, message):
        '''[ значения, разделенные знаком-разделителем(подефолт - запятая) ] - вывести случайное значение из заданных'''
        args = utils.get_args_raw(message)
        if args:
            if self.config['sep'] in args:
                words = args.split(self.config['sep'])
                result = random.choice(words)
                await utils.answer(message, f'<emoji document_id=5391240565679465844>⚡️</emoji> | <b>Ваш результат:</b> <code>{result}</code>')
                return
            else:
                await utils.answer(message, f'<emoji document_id=5980953710157632545>🚫</emoji> <b>Error</b> // <code>{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}</code>'
                '\n\n<emoji document_id=5818973781707722673>🗣</emoji> <b><u>Суть ошибки:</u></b>\nВы указали лишь одно слово, хотя нужно минимум 2.'
                '\n\n<emoji document_id=5821302890932736039>🗣</emoji> <b><u>Способы исправления:</u></b>\nУкажите больше слов.')
                return
        else:
            await utils.answer(message, f'<emoji document_id=5980953710157632545>🚫</emoji> <b>Error</b> // <code>{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}</code>'
            '\n\n<emoji document_id=5818973781707722673>🗣</emoji> <b><u>Суть ошибки:</u></b>\nВы не указали ни единого аргумента.'
            '\n\n<emoji document_id=5821302890932736039>🗣</emoji> <b><u>Способы исправления:</u></b>\nВведите минимум два слова.')
            return
        
    @loader.command()
    async def randvals(self, message):
        '''[ кол-во значений ], [ значения, разделенные знаком-разделителем(дефолт - запятая) ] - вывести несколько случайных значений из заданных'''
        args = utils.get_args_raw(message)
        if args:
            if self.config['sep'] in args:
                if len(args.split(self.config['sep'])) > 2:
                    try:
                        qty = int(args.split(self.config['sep'])[0])
                    except ValueError:
                        await utils.answer(message, f'<emoji document_id=5980953710157632545>🚫</emoji> <b>Error</b> // <code>{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}</code>'
                        '\n\n<emoji document_id=5818973781707722673>🗣</emoji> <b><u>Суть ошибки:</u></b>\nПервым аргументом должно быть целочисленное, обозначающее кол-во слов, которое вы хотите получить.'
                        '\n\n<emoji document_id=5821302890932736039>🗣</emoji> <b><u>Способы исправления:</u></b>\nУкажите первым аргументом целочисленное.')
                        return
                    if qty <= 1000:
                        words = args.split(self.config['sep'])[1:]
                        txt = ''
                        for i in range(qty):
                            txt += f'<code>{random.choice(words)}</code> <b>|</b> '
                        await utils.answer(message, f'<emoji document_id=5391240565679465844>⚡️</emoji> | <b>Ваш результат:</b> {txt}')
                        return
                    else:
                        await utils.answer(message, f'<emoji document_id=5980953710157632545>🚫</emoji> <b>Error</b> // <code>{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}</code>'
                        '\n\n<emoji document_id=5818973781707722673>🗣</emoji> <b><u>Суть ошибки:</u></b>\nНельзя вызвать больше случайных чисел, чем 1000.'
                        '\n\n<emoji document_id=5821302890932736039>🗣</emoji> <b><u>Способы исправления:</u></b>\nВведите число меньше 1000.')
                        return
                else:
                    await utils.answer(message, f'<emoji document_id=5980953710157632545>🚫</emoji> <b>Error</b> // <code>{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}</code>'
                    '\n\n<emoji document_id=5818973781707722673>🗣</emoji> <b><u>Суть ошибки:</u></b>\nВы указали лишь два аргумента, когда необходимо минимум 3.'
                    '\n\n<emoji document_id=5821302890932736039>🗣</emoji> <b><u>Способы исправления:</u></b>\nВведите больше аргументов.')
                    return
            else:
                await utils.answer(message, f'<emoji document_id=5980953710157632545>🚫</emoji> <b>Error</b> // <code>{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}</code>'
                '\n\n<emoji document_id=5818973781707722673>🗣</emoji> <b><u>Суть ошибки:</u></b>\nВы указали лишь один аргумент, когда необходимо минимум 3.'
                '\n\n<emoji document_id=5821302890932736039>🗣</emoji> <b><u>Способы исправления:</u></b>\nВведите больше аргументов.')
                return
        else:
            await utils.answer(message, f'<emoji document_id=5980953710157632545>🚫</emoji> <b>Error</b> // <code>{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}</code>'
            '\n\n<emoji document_id=5818973781707722673>🗣</emoji> <b><u>Суть ошибки:</u></b>\nВы не указали ни единого аргумента.'
            '\n\n<emoji document_id=5821302890932736039>🗣</emoji> <b><u>Способы исправления:</u></b>\nВведите минимум 3 аргумента.')
            return
        
    @loader.command()
    async def randuser(self, message):
        '''- получить случайного пользователя из чата'''
        if message.is_private == False:
            users = []
            async for user in self.client.iter_participants(message.chat_id):
                users.append(user)
            result = random.choice(users)
            try:
                full = await self.client.get_entity(result)
                name = full.first_name
                username = full.username
                id = result.id
                txt = f'Ник | Юзернейм | ID\n{name} | {username} | {id}'
            except Exception:
                txt = f'Ник | Юзернейм | ID\nerror | error | {id}'
            await utils.answer(message, f'<emoji document_id=5391240565679465844>⚡️</emoji> | <b>Ваш результат:</b>\n\n{txt}')
        else:
            await utils.answer(message, f'<emoji document_id=5980953710157632545>🚫</emoji> <b>Error</b> // <code>{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}</code>'
            '\n\n<emoji document_id=5818973781707722673>🗣</emoji> <b><u>Суть ошибки:</u></b>\nЭта команда может работать только в группах.'
            '\n\n<emoji document_id=5821302890932736039>🗣</emoji> <b><u>Способы исправления:</u></b>\nИспользуйте команду в группе.')
            return

    @loader.command()
    async def randusers(self, message):
        '''[ кол-во ] - получить несколько случайных пользователей из чата (-r после кол-ва, чтобы не повторялись)'''
        args = utils.get_args_raw(message)
        if message.is_private == False:
            if args:
                if ' ' not in args:
                    try:
                        qty = int(args)
                    except ValueError:
                        await utils.answer(message, f'<emoji document_id=5980953710157632545>🚫</emoji> <b>Error</b> // <code>{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}</code>'
                        '\n\n<emoji document_id=5818973781707722673>🗣</emoji> <b><u>Суть ошибки:</u></b>\nПервый аргумент может быть только целочисленным.'
                        '\n\n<emoji document_id=5821302890932736039>🗣</emoji> <b><u>Способы исправления:</u></b>\nВведите целочисленное значение.')
                        return
                    if qty <= 50:
                        users = []
                        async for user in self.client.iter_participants(message.chat_id):
                            users.append(user)
                        gusers = []
                        for i in range(qty):
                            gusers.append(random.choice(users))
                        txt = 'Ник | Юзернейм | ID\n'
                        for user in gusers:
                            try:
                                txt += f'{user.first_name} | {user.username} | {user.id}\n'
                            except Exception:
                                txt += f'error | error | error\n'
                        await utils.answer(message, f'<emoji document_id=5391240565679465844>⚡️</emoji> | <b>Ваш результат:</b>\n\n{txt}')
                        return
                    else:
                        await utils.answer(message, f'<emoji document_id=5980953710157632545>🚫</emoji> <b>Error</b> // <code>{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}</code>'
                        '\n\n<emoji document_id=5818973781707722673>🗣</emoji> <b><u>Суть ошибки:</u></b>\nНельзя делать кол-во запрашиваемых людей больше 50.'
                        '\n\n<emoji document_id=5821302890932736039>🗣</emoji> <b><u>Способы исправления:</u></b>\nВведите меньшее кол-во.')
                        return
                if ' ' in args:
                    if args.split(' ')[1] == '-r':
                        try:
                            qty = int(args.split(' ')[0])
                        except ValueError:
                            await utils.answer(message, f'<emoji document_id=5980953710157632545>🚫</emoji> <b>Error</b> // <code>{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}</code>'
                            '\n\n<emoji document_id=5818973781707722673>🗣</emoji> <b><u>Суть ошибки:</u></b>\nПервый аргумент может быть только целочисленным.'
                            '\n\n<emoji document_id=5821302890932736039>🗣</emoji> <b><u>Способы исправления:</u></b>\nВведите целочисленное значение.')
                            return
                        if qty <= 50:
                            users = []
                            async for user in self.client.iter_participants(message.chat_id):
                                users.append(user)
                            if len(users) > qty:
                                gusers = []
                                for i in range(qty):
                                    uu = random.choice(users)
                                    gusers.append(uu)
                                    users.remove(uu)
                                txt = 'Ник | Юзернейм | ID\n'
                                for user in gusers:
                                    try:
                                        txt += f'{user.first_name} | {user.username} | {user.id}\n'
                                    except Exception:
                                        txt += f'error | error | error\n'
                                await utils.answer(message, f'<emoji document_id=5391240565679465844>⚡️</emoji> | <b>Ваш результат:</b>\n\n{txt}')
                                return
                            else:
                                await utils.answer(message, f'<emoji document_id=5980953710157632545>🚫</emoji> <b>Error</b> // <code>{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}</code>'
                                '\n\n<emoji document_id=5818973781707722673>🗣</emoji> <b><u>Суть ошибки:</u></b>\nЧисло полученных участников группы больше или равно запрашиваемому вами кол-ву, в таком случае рандом без повторейний невозможно.'
                                '\n\n<emoji document_id=5821302890932736039>🗣</emoji> <b><u>Способы исправления:</u></b>\nУкажите меньше кол-во.')
                                return
                        else:
                            await utils.answer(message, f'<emoji document_id=5980953710157632545>🚫</emoji> <b>Error</b> // <code>{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}</code>'
                            '\n\n<emoji document_id=5818973781707722673>🗣</emoji> <b><u>Суть ошибки:</u></b>\nНельзя делать кол-во запрашиваемых людей больше 50.'
                            '\n\n<emoji document_id=5821302890932736039>🗣</emoji> <b><u>Способы исправления:</u></b>\nВведите меньшее кол-во.')
                            return
                    else:
                        await utils.answer(message, f'<emoji document_id=5980953710157632545>🚫</emoji> <b>Error</b> // <code>{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}</code>'
                        f'\n\n<emoji document_id=5818973781707722673>🗣</emoji> <b><u>Суть ошибки:</u></b>\nНеизхвестный аргумент - {args.split(" ")[1]}'
                        '\n\n<emoji document_id=5821302890932736039>🗣</emoji> <b><u>Способы исправления:</u></b>\nЕсли вы хотите результат без повторей, введите "-r"')
                        return
            else:
                await utils.answer(message, f'<emoji document_id=5980953710157632545>🚫</emoji> <b>Error</b> // <code>{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}</code>'
                '\n\n<emoji document_id=5818973781707722673>🗣</emoji> <b><u>Суть ошибки:</u></b>\nВы не указали аргументы.'
                '\n\n<emoji document_id=5821302890932736039>🗣</emoji> <b><u>Способы исправления:</u></b>\nУкажите аргументы.')
                return
        else:
            await utils.answer(message, f'<emoji document_id=5980953710157632545>🚫</emoji> <b>Error</b> // <code>{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}</code>'
            '\n\n<emoji document_id=5818973781707722673>🗣</emoji> <b><u>Суть ошибки:</u></b>\nЭта команда может работать только в группах.'
            '\n\n<emoji document_id=5821302890932736039>🗣</emoji> <b><u>Способы исправления:</u></b>\nИспользуйте команду в группе.')
            return

                
