# —————————————————————————————————————————————————————————————————————————————————
#  █▀ █ █ ▀▄▀   █▀▄▀█ █▀█ █▀▄ █ █ █   █▀▀ █▀ Chanel: https://mescr_m
#  ▄█ █▀█ █ █   █ ▀ █ █▄█ █▄▀ █▄█ █▄▄ ██▄ ▄█ Not Licensed
# —————————————————————————————————————————————————————————————————————————————————
#  █▀▀ ▀▄▀ █   █ █ █▀ █ █ █ █▀▀   █▀▄▀█ █▀█ █▀▄ █ █ █   █▀▀ █▀
#  ██▄ █ █ █▄▄ █▄█ ▄█ █ ▀▄▀ ██▄   █ ▀ █ █▄█ █▄▀ █▄█ █▄▄ ██▄ ▄█
# —————————————————————————————————————————————————————————————————————————————————
# Idea:
# meta developer: @mescr_m
# Thanks:
# —————————————————————————————————————————————————————————————————————————————————

from hikkatl.types import Message

from .. import loader, utils


@loader.tds
class IMSG(loader.Module):
    """Позволяет отправить сообщение через inline бота\nDeveloper: @mescr_m\nПосмотрите конфиг!"""

    strings = {
        "name": "IMSG",
        "Link": "Ccылка в кнопке:",
        "Button":"Добавить ли кнопку?",
        "TextButton":"Текст кнопки"
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "Link",
                "https://google.com",
                lambda: self.strings("Link"),
                validator=loader.validators.String(),
            ),
             
            loader.ConfigValue(
                "Button",
                True,
                lambda: self.strings("Button"),
                validator=loader.validators.Boolean(),
            ),

            loader.ConfigValue(
                "TextButton",
                "Google.com",
                lambda: self.strings("TextButton"),
                validator=loader.validators.String(),
            )
        )

    @loader.command()
    async def i(self, message: Message):
        """[ Текст ] - отправить текст через inline бота"""
        args = utils.get_args_raw(message)
        not_args = "<emoji document_id=5877477244938489129>🚫</emoji> <b>Error | Ошибка</b>\nВы не ввели текст!"
        link = self.config["Link"]
        button = self.config["Button"]
        TextButton = self.config["TextButton"]

        if not args:
            await utils.answer(message, not_args)
            return
        
        elif button == True:
            await self.inline.form(
                message=message,
                text=args,
                reply_markup=[[{"text": TextButton, "url": link}]],
            )

        elif button == False:
            await self.inline.form(
                message=message,
                text=args,
            )
        await message.delete()

    
