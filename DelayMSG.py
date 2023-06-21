#—————————————————————————————————————————————————————————————————————————————————
#  █▀ █ █ ▀▄▀   █▀▄▀█ █▀█ █▀▄ █ █ █   █▀▀ █▀ Chanel: https://shx_modules
#  ▄█ █▀█ █ █   █ ▀ █ █▄█ █▄▀ █▄█ █▄▄ ██▄ ▄█ Not Licensed
#—————————————————————————————————————————————————————————————————————————————————
#  █▀▀ ▀▄▀ █   █ █ █▀ █ █ █ █▀▀   █▀▄▀█ █▀█ █▀▄ █ █ █   █▀▀ █▀
#  ██▄ █ █ █▄▄ █▄█ ▄█ █ ▀▄▀ ██▄   █ ▀ █ █▄█ █▄▀ █▄█ █▄▄ ██▄ ▄█
#—————————————————————————————————————————————————————————————————————————————————
# Idea:
# meta developer: @shx_modules
# Thanks: 
#—————————————————————————————————————————————————————————————————————————————————
from .. import utils, loader
from telethon.tl.types import Message
import asyncio 
from asyncio import sleep
@loader.tds
class DelayMSG(loader.Module):
    '''Отправить сообщение через указаное кол-во секунд\nDeveloper: @shx_modules'''
    strings = {'name' : 'DelayMSG'}
    @loader.command()
    async def dm(self, message):
        '''[ Через сколько секунд отправить ] - отправляет сообщение через указаное кол-во секунд'''
        fullargs = utils.get_args_raw(message)
        delaytime = int(fullargs.split(" ")[0])
        text = str(fullargs.split(" ", maxsplit=1)[1])
        await message.delete()
        await asyncio.sleep(delaytime)
        await self.client.send_message(message.chat_id, text) 
        