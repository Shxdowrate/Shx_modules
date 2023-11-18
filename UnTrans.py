#—————————————————————————————————————————————————————————————————————————————————
#  █▀ █ █ ▀▄▀   █▀▄▀█ █▀█ █▀▄ █ █ █   █▀▀ █▀ Chanel: https://mescr_m
#  ▄█ █▀█ █ █   █ ▀ █ █▄█ █▄▀ █▄█ █▄▄ ██▄ ▄█ Not Licensed
#—————————————————————————————————————————————————————————————————————————————————
#  █▀▀ ▀▄▀ █   █ █ █▀ █ █ █ █▀▀   █▀▄▀█ █▀█ █▀▄ █ █ █   █▀▀ █▀
#  ██▄ █ █ █▄▄ █▄█ ▄█ █ ▀▄▀ ██▄   █ ▀ █ █▄█ █▄▀ █▄█ █▄▄ ██▄ ▄█
#—————————————————————————————————————————————————————————————————————————————————
# Idea: @hikariatama
# meta developer: @mescr_m
# Thanks: 
#—————————————————————————————————————————————————————————————————————————————————



from telethon.tl.types import Message

from .. import loader, utils

to_ = [
    'а',
    'б',
    'в',
    'г',
    'д',
    'е',
    'е',
    'ж',
    'з',
    'и',
    'й',
    'к',
    'л',
    'м',
    'н',
    'о',
    'п',
    'р',
    'с',
    'т',
    'у',
    'ф',
    'х',
    'э',
    'ю',
    'я',
    'А',
    'Б',
    'В',
    'Г',
    'Д',
    'Е',
    'Е',
    'Ж',
    'З',
    'И',
    'Й',
    'К',
    'Л',
    'М',
    'Н',
    'О',
    'П',
    'Р',
    'С',
    'Т',
    'У',
    'Ф',
    'Х',
    'Э',
    'Ю',
    'Я',
]

from_ = (
    "abvgdeejziyklmnoprstufheuaABVGDEEJZIIKLMNOPRSTUFHEUA"
)


@loader.tds
class UnTrans(loader.Module):
    """[ Текст на англ ] - переводит англ. транслит на  русский\nРаботает не идеально, не все буквы были реализованы, тк не все буквы имеют аналоги\nDeveloper: @mescr_m"""

    strings = {
        "name": "UnTrans"
    }
   
    async def client_ready(self):
        self._from = from_
        self._to = to_

    async def untcmd(self, message: Message):
        """[ Текст ] - перевод"""

        err = "<emoji document_id=5877477244938489129>🚫</emoji> <b>Error | Ошибка</b>\nВы не ввели текст или не ответили на сообщение с текстом"
        args = utils.get_args_raw(message)
        if not args:
            args_reply = await message.get_reply_message()
        if not args and not args_reply:
            await utils.answer(message, err)
            return
        await utils.answer(message, "".join(to_[from_.index(char)] if char in from_ else char for char in args or args_reply.raw_text))
