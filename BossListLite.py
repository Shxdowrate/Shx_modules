#—————————————————————————————————————————————————————————————————————————————————
#  █▀ █ █ ▀▄▀   █▀▄▀█ █▀█ █▀▄ █ █ █   █▀▀ █▀ Chanel: https://t.me/shx_modules
#  ▄█ █▀█ █ █   █ ▀ █ █▄█ █▄▀ █▄█ █▄▄ ██▄ ▄█ Not Licensed
#—————————————————————————————————————————————————————————————————————————————————
#  █▀▀ ▀▄▀ █   █ █ █▀ █ █ █ █▀▀   █▀▄▀█ █▀█ █▀▄ █ █ █   █▀▀ █▀
#  ██▄ █ █ █▄▄ █▄█ ▄█ █ ▀▄▀ ██▄   █ ▀ █ █▄█ █▄▀ █▄█ █▄▄ ██▄ ▄█
#—————————————————————————————————————————————————————————————————————————————————
# Idea:
# meta developer: @shx_modules
# Thanks: sqlmerr, GPT
#—————————————————————————————————————————————————————————————————————————————————

__version__ = (1, 0, 0)

from .. import utils, loader

class BossListLite(loader.Module):
    '''Бесплатный босс лист\nDeveloper: @shx_modules'''
    strings = {
        'name':'BossListLite',

    }

    @loader.command(alias = 'bl')
    async def bosslist(self, message):
        ''' - получить босс лист'''
        
        bosslist = await self.client.get_messages(-1001914297016,limit=1)
        bosslist = bosslist[0].text
        if bosslist in ['босс лист', 'Босс лист']:
            prefix = utils.escape_html(self.get_prefix())
            await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error</b> | <code>{prefix}bosslist</code>\nБосс лист находился на стадии обновления, пожалуйста, попробуйте снова.')
            return
        else:
            bosslist = bosslist[32:]
            await utils.answer(message, f'<emoji document_id=5204044038126182496>✅</emoji> Босс лист готов.{bosslist}\n\n<emoji document_id=5328274090262275771>🕐</emoji> Босс лист обновляется каждые 30 секунд.')
            return