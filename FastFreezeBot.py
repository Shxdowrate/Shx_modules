#—————————————————————————————————————————————————————————————————————————————————
#  █▀ █ █ ▀▄▀   █▀▄▀█ █▀█ █▀▄ █ █ █   █▀▀ █▀ Channel: https://t.me/shx_modules
#  ▄█ █▀█ █ █   █ ▀ █ █▄█ █▄▀ █▄█ █▄▄ ██▄ ▄█ Not Licensed
#—————————————————————————————————————————————————————————————————————————————————
# Idea:
# meta developer: @shx_modules
# Thanks: 
#—————————————————————————————————————————————————————————————————————————————————

from .. import utils, loader
from time import sleep
import time

class FastFreezeBot(loader.Module):
    '''Модуль для быстрой заморозки юзербота.\nDeveloper: @shx_modules'''
    strings = {
        'name':'FastFreezeBot',
        'timefreeze':'Время, на которое нужно заморозить юзербота',
        'wordfreeze':'Слово, от которого нужно заморозить юзербота.'
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "timefreeze", 5,
                lambda: self.strings("timefreeze"),
                validator=loader.validators.Integer()
            ),
            loader.ConfigValue(
                "wordfreeze", 'ss',
                lambda: self.strings("wordfreeze"),
                validator=loader.validators.String()
            ),
        )

    @loader.watcher(out = True)
    async def watcher(self, message):
        mword = self.config['wordfreeze']
        mtime = self.config['timefreeze']
        if message.raw_text == mword:
            await message.edit(f'❄️ | <b>Ваш юзербот был заморожен на</b> <code>{mtime}</code> <b>секунд.</b>')
            await time.sleep(mtime)


    @loader.command()
    async def freezehelp(self, message):
        ''' - помощь по модулю'''
        word = self.config['wordfreeze']
        time = self.config['timefreeze']
        await utils.answer(message, f'<emoji document_id=5413700332649720173>❓</emoji> | Зачем нужен этот модуль?\nЕсли у вас сломался какой-то модуль и начал внезапно спамить сообщениями, этот модуль ваш выручит, в отличии от .suspend, тут не придется прописывать целую команду и указывать время, вам нужно лишь отправить сообщение "{word}" и ваш юзербот заморозится на <code>{time}</code> секунд.\nВ конфиге можно поменять время заморозки и слово.')
