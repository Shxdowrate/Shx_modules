# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔐 Licensed under the GNU AGPLv3.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: AlphabetED
# Author: hikariatama
# Editor: Shxdowrate
# Commands:
# .ae
# ---------------------------------------------------------------------------------

#             █ █ ▀ █▄▀ ▄▀█ █▀█ ▀
#             █▀█ █ █ █ █▀█ █▀▄ █
#              © Copyright 2022
#           https://t.me/hikariatama
#
# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

# meta pic: https://img.icons8.com/plasticine/344/hiragana-ma.png
# meta developer: @hikarimods / @ubhikka_modules
# meta banner: https://mods.hikariatama.ru/badges/alphabet.jpg
# scope: hikka_only
# scope: hikka_min 1.4.0

import logging

from telethon.tl.types import Message

from .. import loader, utils

logger = logging.getLogger(__name__)

to_ = [
    '<emoji document_id=5256087698745076207>🔠</emoji>',
    '<emoji document_id=5258093353983025227>🔠</emoji>',
    '<emoji document_id=5258158508636905648>🔠</emoji>',
    '<emoji document_id=5256057178707469647>🔠</emoji>',
    '<emoji document_id=5258045984788717832>🔠</emoji>',
    '<emoji document_id=5255838994368834442>🔠</emoji>',
    '<emoji document_id=5258427188906042050>🔠</emoji>',
    '<emoji document_id=5256141690778952886>🔠</emoji>',
    '<emoji document_id=5255970600756718197>🔠</emoji>',
    '<emoji document_id=5256185890287396695>🔠</emoji>',
    '<emoji document_id=5258043966154088238>🔠</emoji>',
    '<emoji document_id=5258059591245110143>🔠</emoji>',
    '<emoji document_id=5258060158180794868>🔠</emoji>',
    '<emoji document_id=5255752790080234973>🔠</emoji>',
    '<emoji document_id=5255972975873632543>🔠</emoji>',
    '<emoji document_id=5255854937287435776>🔠</emoji>',
    '<emoji document_id=5255717352305076701>🔠</emoji>',
    '<emoji document_id=5256005879618086735>🔠</emoji>',
    '<emoji document_id=5256109366855083833>🔠</emoji>',
    '<emoji document_id=5256208640729163003>🔠</emoji>',
    '<emoji document_id=5255793068283536363>🔠</emoji>',
    '<emoji document_id=5255796684646007105>🔠</emoji>',
    '<emoji document_id=5255900725933779026>🔠</emoji>',
    '<emoji document_id=5255865756310054127>🔠</emoji>',
    '<emoji document_id=5256063986230633886>🔠</emoji>',
    '<emoji document_id=5255737126334506261>🔠</emoji>',
    '<emoji document_id=5258513053892222258>🔠</emoji>',
    '<emoji document_id=5255905145455126232>🔠</emoji>',
    '<emoji document_id=5256262856101341316>🔠</emoji>',
    '<emoji document_id=5255771756655813401>🔠</emoji>',
    '<emoji document_id=5258101656154809579>🔠</emoji>',
    '<emoji document_id=5256059115737719251>🔠</emoji>',
    '<emoji document_id=5255973950831208848>🔠</emoji>',
    '<emoji document_id=5256087698745076207>🔠</emoji>',
    '<emoji document_id=5258093353983025227>🔠</emoji>',
    '<emoji document_id=5258158508636905648>🔠</emoji>',
    '<emoji document_id=5256057178707469647>🔠</emoji>',
    '<emoji document_id=5258045984788717832>🔠</emoji>',
    '<emoji document_id=5255838994368834442>🔠</emoji>',
    '<emoji document_id=5258427188906042050>🔠</emoji>',
    '<emoji document_id=5256141690778952886>🔠</emoji>',
    '<emoji document_id=5255970600756718197>🔠</emoji>',
    '<emoji document_id=5256185890287396695>🔠</emoji>',
    '<emoji document_id=5258043966154088238>🔠</emoji>',
    '<emoji document_id=5258059591245110143>🔠</emoji>',
    '<emoji document_id=5258060158180794868>🔠</emoji>',
    '<emoji document_id=5255752790080234973>🔠</emoji>',
    '<emoji document_id=5255972975873632543>🔠</emoji>',
    '<emoji document_id=5255854937287435776>🔠</emoji>',
    '<emoji document_id=5255717352305076701>🔠</emoji>',
    '<emoji document_id=5256005879618086735>🔠</emoji>',
    '<emoji document_id=5256109366855083833>🔠</emoji>',
    '<emoji document_id=5256208640729163003>🔠</emoji>',
    '<emoji document_id=5255793068283536363>🔠</emoji>',
    '<emoji document_id=5255796684646007105>🔠</emoji>',
    '<emoji document_id=5255900725933779026>🔠</emoji>',
    '<emoji document_id=5255865756310054127>🔠</emoji>',
    '<emoji document_id=5256063986230633886>🔠</emoji>',
    '<emoji document_id=5255737126334506261>🔠</emoji>',
    '<emoji document_id=5258513053892222258>🔠</emoji>',
    '<emoji document_id=5255905145455126232>🔠</emoji>',
    '<emoji document_id=5256262856101341316>🔠</emoji>',
    '<emoji document_id=5255771756655813401>🔠</emoji>',
    '<emoji document_id=5258101656154809579>🔠</emoji>',
    '<emoji document_id=5256059115737719251>🔠</emoji>',
    '<emoji document_id=5255973950831208848>🔠</emoji>',
    "<emoji document_id=5256062787934756794>🅰️</emoji>", 
    "<emoji document_id=5256020804629441006>🅱️</emoji>",
    "<emoji document_id=5255885822397261485>🔠</emoji>",
    "<emoji document_id=5255902057373639707>🔠</emoji>",
    "<emoji document_id=5256025889870720224>🔠</emoji>",
    "<emoji document_id=5256072941237444967>🔠</emoji>",
    "<emoji document_id=5255885607648897261>🔠</emoji>",
    "<emoji document_id=5256090615027869813>🔠</emoji>",
    "<emoji document_id=5255715977915541085>🔠</emoji>",
    "<emoji document_id=5256117995444381773>🔠</emoji>",
    "<emoji document_id=5256214224186649542>🔠</emoji>",
    "<emoji document_id=5256131133749340590>🔠</emoji>",
    "<emoji document_id=5255763845326054075>🔠</emoji>",
    "<emoji document_id=5255720092494209804>🔠</emoji>",
    "<emoji document_id=5258169864530435665>🔠</emoji>",
    "<emoji document_id=5256100806985263252>🔠</emoji>",
    "<emoji document_id=5256073508173129005>🔠</emoji>",
    "<emoji document_id=5256163152730530629>🔠</emoji>",
    "<emoji document_id=5256198629160396232>🔠</emoji>",
    "<emoji document_id=5255702852495483873>🔠</emoji>",
    "<emoji document_id=5255990666843924021>🔠</emoji>",
    "<emoji document_id=5256261872553828743>🔠</emoji>",
    "<emoji document_id=5255930511531976150>🔠</emoji>",
    "<emoji document_id=5255733063295445732>🔠</emoji>",
    "<emoji document_id=5256220726767132498>🔠</emoji>",
    "<emoji document_id=5258332321668406770>🔠</emoji>",
    "<emoji document_id=5256062787934756794>🅰️</emoji>",
    "<emoji document_id=5256020804629441006>🅱️</emoji>",
    "<emoji document_id=5255885822397261485>🔠</emoji>",
    "<emoji document_id=5255902057373639707>🔠</emoji>",
    "<emoji document_id=5256025889870720224>🔠</emoji>",
    "<emoji document_id=5256072941237444967>🔠</emoji>",
    "<emoji document_id=5255885607648897261>🔠</emoji>",
    "<emoji document_id=5256090615027869813>🔠</emoji>",
    "<emoji document_id=5255715977915541085>🔠</emoji>",
    "<emoji document_id=5256117995444381773>🔠</emoji>",
    "<emoji document_id=5256214224186649542>🔠</emoji>",
    "<emoji document_id=5256131133749340590>🔠</emoji>",
    "<emoji document_id=5255763845326054075>🔠</emoji>",
    "<emoji document_id=5255720092494209804>🔠</emoji>",
    "<emoji document_id=5258169864530435665>🔠</emoji>",
    "<emoji document_id=5256100806985263252>🔠</emoji>",
    "<emoji document_id=5256073508173129005>🔠</emoji>",
    "<emoji document_id=5256163152730530629>🔠</emoji>",
    "<emoji document_id=5256198629160396232>🔠</emoji>",
    "<emoji document_id=5255702852495483873>🔠</emoji>",
    "<emoji document_id=5255990666843924021>🔠</emoji>",
    "<emoji document_id=5256261872553828743>🔠</emoji>",
    "<emoji document_id=5255930511531976150>🔠</emoji>",
    "<emoji document_id=5255733063295445732>🔠</emoji>",
    "<emoji document_id=5256220726767132498>🔠</emoji>",
    "<emoji document_id=5258332321668406770>🔠</emoji>",
    "<emoji document_id=5258124771668794894>1️⃣</emoji>",
    "<emoji document_id=5258326935779418457>2️⃣</emoji>",
    "<emoji document_id=5255836533352572170>3️⃣</emoji>",
    "<emoji document_id=5255973946536240678>4️⃣</emoji>",
    "<emoji document_id=5258297845965921902>5️⃣</emoji>",
    "<emoji document_id=5255715853361489891>6️⃣</emoji>",
    "<emoji document_id=5255828329965037455>7️⃣</emoji>",
    "<emoji document_id=5255849744671975334>8️⃣</emoji>",
    "<emoji document_id=5258043738520822966>9️⃣</emoji>",
    "<emoji document_id=5256065364915135470>0️⃣</emoji>",
    '<emoji document_id=5256069917580470662>🔠</emoji>',
    '<emoji document_id=5255914577203307545>🔠</emoji>',
    '<emoji document_id=5256231167832631881>⚪️</emoji>',
    '<emoji document_id=5256142738750973947>🔠</emoji>',
    '<emoji document_id=5255935626838025893>🔠</emoji>',
    '<emoji document_id=5256255954088896744>❓</emoji>',
    '<emoji document_id="6032769737509833594">📛</emoji>',
    '<emoji document_id=5255956869746271068>🔠</emoji>',
    '<emoji document_id=5255865481432146649>🔠</emoji>',
    '<emoji document_id=5255890138839393959>➕</emoji>',
    '<emoji document_id=5256021844011525298>➖</emoji>',
    '<emoji document_id=5256057019793679305>🟰</emoji>',
    '<emoji document_id=5256001730679679254>🔠</emoji>',
    '<emoji document_id=5255927878717024287>🔠</emoji>',
]

from_ = (
    "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890().,!? @#+-=/:"
)


@loader.tds
class AlphabetED(loader.Module):
    """Replaces your text with custom emojis. Telegram Premium only"""

    strings = {
        "name": "AlphabetED",
        "no_text": "🚫 <b>Specify text to replace</b>",
        "premium_only": (
            "⭐️ This module is available only to Telegram Premium subscribers"
        ),
    }
    strings_ru = {
        "no_text": "🚫 <b>Укажите текст для замены</b>",
        "premium_only": "⭐️ Этот модуль доступен только для Telegram Premium",
        "_cmd_doc_a": "Заменить текст на эмодзи",
        "_cls_doc": "Заменяет текст на кастомные эмодзи. Только для Telegram Premium",
    }
    strings_de = {
        "no_text": "🚫 <b>Gib den Text ein, der ersetzt werden soll</b>",
        "premium_only": (
            "⭐️ Dieses Modul ist nur für Telegram Premium-Abonnenten verfügbar"
        ),
        "_cmd_doc_a": "Ersetze Text durch Emojis",
        "_cls_doc": (
            "Ersetzt Text durch benutzerdefinierte Emojis. Nur für Telegram Premium"
        ),
    }
    strings_hi = {
        "no_text": "🚫 <b>बदलने के लिए पाठ निर्दिष्ट करें</b>",
        "premium_only": "⭐️ यह मॉड्यूल केवल Telegram Premium सदस्यों के लिए उपलब्ध है",
        "_cmd_doc_a": "पाठ को इमोजी के रूप में बदलें",
        "_cls_doc": (
            "आपके पाठ को कस्टम इमोजी के रूप में बदलता है। केवल Telegram Premium के लिए"
        ),
    }
    strings_uz = {
        "no_text": "🚫 <b>Almashtirish uchun matn belgilang</b>",
        "premium_only": (
            "⭐️ Bu modul faqat Telegram Premium obuna bo'lganlar uchun mavjud"
        ),
        "_cmd_doc_a": "Matnni emoji bilan almashtiring",
        "_cls_doc": (
            "Matnni sizning emojiingiz bilan almashtiradi. Faqat Telegram Premium uchun"
        ),
    }

    async def client_ready(self):
        if not (await self._client.get_me()).premium:
            raise loader.LoadError(self.strings("premium_only"))

        self._from = from_
        self._to = to_

    async def aecmd(self, message: Message):
        """[ текст ] - написаный текст превратится в эмоджи"""
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        if not args and not reply:
            await utils.answer(message, self.strings("no_text"))
            return

        await utils.answer(
            message,
            "".join(
                to_[from_.index(char)] if char in from_ else char
                for char in args or reply.raw_text
            ),
        )