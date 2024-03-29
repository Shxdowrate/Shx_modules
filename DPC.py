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

from .. import utils, loader

from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.types import ChannelParticipantsSearch

__version__ = (1, 0, 1)

class DPC(loader.Module):
    '''Калькулятор плазмы для улучшения автобура MineEVO.\nDeveloper: @mescr_m'''
    strings = {
        'name': 'DPC'
    }

    async def client_ready(self, client, db):
        self.client = client
        self.db = db

    @loader.command()
    async def dpc(self, message):
        '''[ Начальный уровень ] [ Конечный уровень ](или наоборот) - высчитать плазму'''
        args = utils.get_args_raw(message)
        prefix = utils.escape_html(self.get_prefix())  
        if not args:
            await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error |</b> <code>{prefix}dpc</code>\nВы не указали аргументов.\nПопробуйте: <code>{prefix}dpc 1 80</code>')
            return
        if ' ' in args:
            args = args.split()
            if len(args) > 2:
                await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error |</b> <code>{prefix}dpc</code>\nМодуль принимает только два аргументв: начальный уровень и конечный, а было указано больше двух.')
                return
            else:
                args_start = int(args[0])
                args_end = int(args[1])
                if args_start < 1:
                    await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error |</b> <code>{prefix}dpc</code>\nНачальный уровень не может быть меньше одного.')
                    return
                elif args_end > 80:
                    await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error |</b> <code>{prefix}dpc</code>\nКонечный уровень не может быть больше 80.')
                    return
                else:
                    if args_start > args_end:
                        args_start, args_end = args_end, args_start
                    plasma_cost = sum(10000 + 5000 * (level - 1) for level in range(args_start, args_end))
                    await utils.answer(message, f'🎆 <b><u>Итог:</u></b>\n<b>Начальный уровень:<b> <code>{args_start}</code>\n<b>Конечный уровень:</b> <code>{args_end}</code>\n<b><u>Цена:</b></u> <code>{plasma_cost}</code>')
                    return
        else:
            await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error |</b> <code>{prefix}dpc</code>\nМодуль поддерживает только два аргумента, а было указано менее двух.\nПопробуйте: <code>{prefix}dpc 1 80</code>')



        
