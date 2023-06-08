#—————————————————————————————————————————————————————————————————————————————————
#  █▀ █ █ ▀▄▀   █▀▄▀█ █▀█ █▀▄ █ █ █   █▀▀ █▀ Chanel: https://shx_modules
#  ▄█ █▀█ █ █   █ ▀ █ █▄█ █▄▀ █▄█ █▄▄ ██▄ ▄█ Not Licensed
#—————————————————————————————————————————————————————————————————————————————————
#  █▀▀ ▀▄▀ █   █ █ █▀ █ █ █ █▀▀   █▀▄▀█ █▀█ █▀▄ █ █ █   █▀▀ █▀
#  ██▄ █ █ █▄▄ █▄█ ▄█ █ ▀▄▀ ██▄   █ ▀ █ █▄█ █▄▀ █▄█ █▄▄ ██▄ ▄█
#—————————————————————————————————————————————————————————————————————————————————
# Idea: @amoremods
# meta developer: @shx_modules
# Thanks: 
#—————————————————————————————————————————————————————————————————————————————————

import datetime
import logging

from .. import loader, utils

logger = logging.getLogger(__name__)


def check_time():
    offsets = [5, 6]
    hrs = []
    for x in offsets:
        offset = datetime.timedelta(hours=x)
        not_tz = datetime.timezone(offset)
        time = datetime.datetime.now(not_tz)
        format_ = time.strftime("%d.%m.%y | %H:%M")
        hrs.append(format_)
    b = (
        "🇰🇿 <b>Областное время Казахстана</b>\n\n"
        f"<b>Области:</b> \nАктюбинская область \nАтырауская область\nЗападно-Казахстанская область\nКызылординская область\nМангистауская область\n<emoji document_id=5785209342986817408>🌎</emoji> <b>Время:</b>    <code>{hrs[0]}</code>\n\n"
        f"<b>Области:</b> \nУлытауская область\nТуркестанская область\nСеверо-Казахстанская область\nПавлодарская область\nКостанайская область\nКарагандинская область\nЖетысуская область\nЖамбылская область\nВосточно-Казахстанская область\nАлматинская область\nАкмолинская область\nАбайская область\n<emoji document_id=5785209342986817408>🌎</emoji> <b>Время:</b>    <code>{hrs[1]}</code>\n"
       
        
    )
    return b


@loader.tds
class KzUniReg(loader.Module):
    """Посмотреть время по всему Казахстану!\nDeveloper: @Shx_modules"""

    strings = {"name": "KzUniReg"}

    @loader.command()
    async def kztimecmd(self, message):
        """- увидеть время по всему Казахстану\n\n\n"""
        kk = check_time()
        await utils.answer(message, kk)