# —————————————————————————————————————————————————————————————————————————————————
#  █▀ █ █ ▀▄▀   █▀▄▀█ █▀█ █▀▄ █ █ █   █▀▀ █▀ Chanel: https://shx_modules
#  ▄█ █▀█ █ █   █ ▀ █ █▄█ █▄▀ █▄█ █▄▄ ██▄ ▄█ Not Licensed
# —————————————————————————————————————————————————————————————————————————————————
#  █▀▀ ▀▄▀ █   █ █ █▀ █ █ █ █▀▀   █▀▄▀█ █▀█ █▀▄ █ █ █   █▀▀ █▀
#  ██▄ █ █ █▄▄ █▄█ ▄█ █ ▀▄▀ ██▄   █ ▀ █ █▄█ █▄▀ █▄█ █▄▄ ██▄ ▄█
# —————————————————————————————————————————————————————————————————————————————————
# Idea:
# meta developer: @shx_modules
# Thanks: @visionavtr
# —————————————————————————————————————————————————————————————————————————————————

from hikkatl.types import Message

from .. import loader, utils


@loader.tds
class NoMeta(loader.Module):
    """Сообщите своему собеседнику, чтобы он сразу сказал, что ему нужно от вас!\nDeveloper: @Shx_modules"""

    strings = {
        "name": "NoMeta",
        "🔗 Url in nmeta": "Ccылка в сообщении для nmeta"
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "🔗 Link in nmeta",
                True,
                lambda: self.strings("🔗 Link in nmeta"),
                validator=loader.validators.Boolean(),
            ),
        )

    @loader.command()
    async def nometa(self, message: Message):
        """- сообщить"""

        textmessage = "<emoji document_id=5877477244938489129>🚫</emoji> Пожалуйста!\n<b>NoMeta!</b> Не говорите просто 'Привет', 'Как дела?'\nГоворите сразу, <b>что</b> вам нужно/<b>чем</b> помочь!"
        textbutton = "Прочитать подобнее про NoMeta"
        urlbutton = "https://nometa.xyz/ru.html"

        await self.inline.form(
            message=message,
            text=textmessage,
            reply_markup=[[{"text": textbutton, "url": urlbutton}]],
        )
        await message.delete()

    @loader.command()
    async def nmeta(self, message: Message):
        """- сообщить без инлайна"""
        textmessage = "<emoji document_id=5877477244938489129>🚫</emoji> Пожалуйста!\n<b>NoMeta!</b> Не говорите просто 'Привет', 'Как дела?'\nГоворите сразу,<b>что</b> вам нужно/<b>чем</b> помочь!"
        textmessage2 = "<emoji document_id=5877477244938489129>🚫</emoji> Пожалуйста!\n<b>NoMeta!</b> Не говорите просто 'Привет', 'Как дела?'\nГоворите сразу, <b>что</b> вам нужно/<b>чем</b> помочь!\n<b>» <a href=\"https://nometa.xyz/ru.html\"> Узнать больше о NoMeta </a> «</b>"
        if not self.config["🔗 Link in nmeta"]:
            await utils.answer(message, f"{textmessage}")
            return
        else:
            await utils.answer(message, f"{textmessage2}")
