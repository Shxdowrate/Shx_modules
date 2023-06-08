# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/ubhikka_modules
# ( o.o )  🔐 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: MyModulesRu
# Author: Shx
# Commands:
# .mm
# ---------------------------------------------------------------------------------
# scope: hikka_only

import logging

from .. import loader, utils

logger = logging.getLogger(__name__)


@loader.tds
class MyModulesRuMod(loader.Module):
    """ Позволяет посмотреть все установленные модули через запятую и без лишней информации!\nDeveloper: @Shx_modules"""

    strings = {
        "name": "MyModulesRu",
        "amount": "<emoji document_id=5192947899922656408>⚡</emoji> Installed <b>{}</b> modules.",
        "modules": "<emoji document_id=5785058280397082578>📂</emoji> Modules:",
    }

    strings_ru = {
        "amount": "<emoji document_id=5192947899922656408>⚡</emoji> Установлено: <b>{}</b> модулей.",
        "modules": "<emoji document_id=5785058280397082578>📂</emoji> Модули:",
    }

    @loader.command(ru_doc="Увидеть установленые модули без лишней информации")
    async def mmcmd(self, message):
        """See the installed modules without additional information"""

        result = (
            f"{self.strings('amount').format(str(len(self.allmodules.modules)))}\n{self.strings('modules')} | "
        )

        for mod in self.allmodules.modules:
            try:
                name = mod.strings["name"]
            except KeyError:
                name = mod.__clas__.__name__
            result += f"<code>{name}</code> | "

        await utils.answer(message, result)