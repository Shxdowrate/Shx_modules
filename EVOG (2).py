#—————————————————————————————————————————————————————————————————————————————————
#  █▀ █ █ ▀▄▀   █▀▄▀█ █▀█ █▀▄ █ █ █   █▀▀ █▀ Chanel: https://shx_modules
#  ▄█ █▀█ █ █   █ ▀ █ █▄█ █▄▀ █▄█ █▄▄ ██▄ ▄█ Not Licensed
#—————————————————————————————————————————————————————————————————————————————————
#  █▀▀ ▀▄▀ █   █ █ █▀ █ █ █ █▀▀   █▀▄▀█ █▀█ █▀▄ █ █ █   █▀▀ █▀
#  ██▄ █ █ █▄▄ █▄█ ▄█ █ ▀▄▀ ██▄   █ ▀ █ █▄█ █▄▀ █▄█ █▄▄ ██▄ ▄█
#—————————————————————————————————————————————————————————————————————————————————
# Idea:
# meta developer: @shx_modules
# Thanks:  @visionavtr
#—————————————————————————————————————————————————————————————————————————————————

from hikkatl.tl.types import Message

import asyncio

from .. import loader, utils


@loader.tds
class EVOG(loader.Module):
    """Module for managing account @mine_evo_bot\nDeveloper: @Shx_modules"""

    strings = {
        "name": "EVOG",
        "cfg": "The chat where the commands will be sent.",
    }

    strings_ru = {
        "cfg": "Чат, в который будут отправляться команды",
        "_cls_doc": "Модуль для управления аккаунтом @mine_evo_bot\nDeveloper: @Shx_modules",
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "chat_id",
                "@mine_evo_bot",
                lambda: self.strings["cfg"],
            )
        )

    @loader.command(
        ru_doc="[ Запрос ] - Отправляет запрос в определенную группу, изменяя сообщение на полученый ответ\nПример: .evo топ к => выдаст топ по кликам"
    )
    async def evo(self, message: Message):
        """[ Request ] - Sends a request to a specific group, changing the message to the received response\nExample: .evo топ к => will give top by clicks."""
        args = utils.get_args_raw(message)

        async with message.client.conversation(self.config["chat_id"]) as conv:
            await conv.send_message(args)
            response = await conv.get_response()
            await utils.answer(message, response)