#—————————————————————————————————————————————————————————————————————————————————
#  █▀ █ █ ▀▄▀   █▀▄▀█ █▀█ █▀▄ █ █ █   █▀▀ █▀ Chanel: https://mescr_m
#  ▄█ █▀█ █ █   █ ▀ █ █▄█ █▄▀ █▄█ █▄▄ ██▄ ▄█ Not Licensed
#—————————————————————————————————————————————————————————————————————————————————
#  █▀▀ ▀▄▀ █   █ █ █▀ █ █ █ █▀▀   █▀▄▀█ █▀█ █▀▄ █ █ █   █▀▀ █▀
#  ██▄ █ █ █▄▄ █▄█ ▄█ █ ▀▄▀ ██▄   █ ▀ █ █▄█ █▄▀ █▄█ █▄▄ ██▄ ▄█
#—————————————————————————————————————————————————————————————————————————————————
# Idea:
# meta developer: @mescr_m
# Thanks: 
#—————————————————————————————————————————————————————————————————————————————————

from .. import loader, utils
from hikkatl.types import Message

@loader.tds
class FevalMod(loader.Module):
    """Создайте фейковый результат к eval (.e)\nDeveloper: @mescr_m"""
    strings = {
        "name": "Feval"       
    }
  

    @loader.command(alias="fevalcmd")
    async def eecmd(self, message):
        """[ Код ] [ Результат ] - создай фейковый результат eval (.e)"""
        args = utils.get_args_raw(message).split(" / ")
        code = args[0]
        result = args[1]
       
        err1 = "<emoji document_id=5877477244938489129>🚫</emoji> <b>Error | Ошибка</b>\n Должно быть 2 аргумента, разделенных знаком '/'"
        
        if len(args) != 2:
            await utils.answer(message, err1)
            return
        
        else:
            await utils.answer(message, f"<emoji document_id=4985626654563894116>💻</emoji><b> Код:\n</b><code>{code}</code>\n\n<emoji document_id=5197688912457245639>✅</emoji><b> Результат:\n</b><code>{result}</code>")



            
