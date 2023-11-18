#—————————————————————————————————————————————————————————————————————————————————
#  █▀ █ █ ▀▄▀   █▀▄▀█ █▀█ █▀▄ █ █ █   █▀▀ █▀ Chanel: https://mescr_m
#  ▄█ █▀█ █ █   █ ▀ █ █▄█ █▄▀ █▄█ █▄▄ ██▄ ▄█ Not Licensed
#—————————————————————————————————————————————————————————————————————————————————
#  █▀▀ ▀▄▀ █   █ █ █▀ █ █ █ █▀▀   █▀▄▀█ █▀█ █▀▄ █ █ █   █▀▀ █▀
#  ██▄ █ █ █▄▄ █▄█ ▄█ █ ▀▄▀ ██▄   █ ▀ █ █▄█ █▄▀ █▄█ █▄▄ ██▄ ▄█
#—————————————————————————————————————————————————————————————————————————————————
# Idea: @amoremods
# meta developer: @mescr_m
# Thanks: 
#—————————————————————————————————————————————————————————————————————————————————

import datetime
import logging

from .. import loader, utils
from ..inline.types import InlineCall

logger = logging.getLogger(__name__)


def check_time():
    offsets = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    hrs = []
    for x in offsets:
        offset = datetime.timedelta(hours=x)
        not_tz = datetime.timezone(offset)
        time = datetime.datetime.now(not_tz)
        format_ = time.strftime("%d.%m.%y | %H:%M")
        hrs.append(format_)
    b = (
        "<emoji document_id=5449408995691341691>🇷🇺</emoji> <b>Областное время России</b>\n\n"
        f"<emoji document_id=5273792924033752303>🇷🇺</emoji> Калининград  <code>{hrs[0]}</code>\n"
        f"<emoji document_id=5274108956317327229>🇷🇺</emoji> Москва            <code>{hrs[1]}</code>\n"
        f"<emoji document_id=5274159331988742053>🇷🇺</emoji> Самара            <code>{hrs[2]}</code>\n"
        f"<emoji document_id=5273938914267111564>🇷🇺</emoji> Екатеринбург  <code>{hrs[3]}</code>\n"
        f"<emoji document_id=5274082658232573772>🇷🇺</emoji> Омск                  <code>{hrs[4]}</code>\n"
        f"<emoji document_id=5275968767350808232>🇷🇺</emoji> Красноярск     <code>{hrs[5]}</code>\n"
        f"<emoji document_id=5274156600389543207>🇷🇺</emoji> Иркутск             <code>{hrs[6]}</code>\n"
        f"<emoji document_id=5273911413591515632>🇷🇺</emoji> Якутск                <code>{hrs[7]}</code>\n"
        f"<emoji document_id=5276118404011400607>🇷🇺</emoji> Владивосток    <code>{hrs[8]}</code>\n"
        f"<emoji document_id=5276383235989839294>🇷🇺</emoji> Магадан            <code>{hrs[9]}</code>\n"
        f"<emoji document_id=5273803987869507877>🇷🇺</emoji> Камчатка          <code>{hrs[10]}</code>\n"
        
    )
    return b


@loader.tds
class UniReg(loader.Module):
    """Посмотреть время по всей России!\nDeveloper: @mescr_m"""

    strings = {"name": "UniReg"}

    @loader.command()
    async def rtimecmd(self, message):
        """- увидеть время по всей России\n\n\n"""
        kk = check_time()
        await utils.answer(message, kk)
