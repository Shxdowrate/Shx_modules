#—————————————————————————————————————————————————————————————————————————————————
#  █▀ █ █ ▀▄▀   █▀▄▀█ █▀█ █▀▄ █ █ █   █▀▀ █▀ Chanel: https://shx_modules
#  ▄█ █▀█ █ █   █ ▀ █ █▄█ █▄▀ █▄█ █▄▄ ██▄ ▄█ Not Licensed
#—————————————————————————————————————————————————————————————————————————————————
#  █▀▀ ▀▄▀ █   █ █ █▀ █ █ █ █▀▀   █▀▄▀█ █▀█ █▀▄ █ █ █   █▀▀ █▀
#  ██▄ █ █ █▄▄ █▄█ ▄█ █ ▀▄▀ ██▄   █ ▀ █ █▄█ █▄▀ █▄█ █▄▄ ██▄ ▄█
#—————————————————————————————————————————————————————————————————————————————————
# Idea: @hikariatama
# meta developer: @shx_modules
# Thanks: 
#—————————————————————————————————————————————————————————————————————————————————



from telethon.tl.types import Message

from .. import loader, utils

to_ = [
    'a',
    'б',
    'в',
    'r',
    'д',
    'e',
    'e',
    'ж',
    'з',
    'и',
    'й',
    'к',
    'л',
    'м',
    'н',
    'o',
    'п',
    'p',
    'c',
    'т',
    'y',
    'ф',
    'x',
    'ц',
    'ч',
    'ш',
    'щ',
    'ъ',
    'ы',
    'ь',
    'э',
    'ю',
    'я',
    'A',
    'Б',
    'B',
    'Г',
    'Д',
    'E',
    'E',
    'Ж',
    '3',
    'И',
    'Й',
    'K',
    'Л',
    'M',
    'H',
    'O',
    'П',
    'P',
    'C',
    'T',
    'У',
    'Ф',
    'X',
    'Ц',
    'Ч',
    'Ш',
    'Щ',
    'Ъ',
    'Ы',
    'Ь',
    'Э',
    'Ю',
    'Я',
]

from_ = (
    "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
)


@loader.tds
class RepText(loader.Module):
    """[ Текст на русском ] - заменяет русские буквы к тексте на английские, которые на 100% идентичны русским по внешнему виду.\nDeveloper: @Shx_modules"""

    strings = {
        "name": "RepText"
    }
   
    async def client_ready(self):
        self._from = from_
        self._to = to_

    async def repcmd(self, message: Message):
        """[ Текст ] - Замена букв"""

        err = "<emoji document_id=5877477244938489129>🚫</emoji> <b>Error | Ошибка</b>\nВы не ввели текст или не ответили на сообщение с текстом"
        args = utils.get_args_raw(message)
        if not args:
            args_reply = await message.get_reply_message()
        if not args and not args_reply:
            await utils.answer(message, err)
            return
        await utils.answer(message, "".join(to_[from_.index(char)] if char in from_ else char for char in args or args_reply.raw_text))