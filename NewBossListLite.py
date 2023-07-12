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

__version__ = (2, 0, 0)

from .. import utils, loader
from telethon.tl.functions.channels import GetFullChannelRequest
class NBLL(loader.Module):
    '''Бесплатный босс лист\nDeveloper: @shx_modules'''
    strings = {
        'name':'NewBossListLite',
        'watcher':'Выполнять ли команду через наблюдателя?',
        'command_watcher':'Команда для босс листа через наблюдателя.',
        'load_mod_donate':'Давать ли 1 кейс создателю при включении юб или загрузке модуля?\nПо дефолту включено, но после загрузки модуля отключается автоматически.'

    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "watcher", True,
                lambda: self.strings("watcher"),
                validator=loader.validators.Boolean()
            ),
            loader.ConfigValue(
                "command_watcher", 'босслист',
                lambda: self.strings("command_watcher"),
                validator=loader.validators.String()
            ),
            loader.ConfigValue(
                "load_mod_donate", True,
                lambda: self.strings("load_mod_donate"),
                validator=loader.validators.Boolean()
            ),
        )

    async def client_ready(self):
        status = self.config['load_mod_donate']
        if status == True:
            self.client.send_message('@mine_evo_bot', 'дать к 1')
            self.config['load_mod_donate'] = False



    @loader.watcher(out = True)
    async def watcher_bosslist(self, message):
        status = self.config['watcher']
        command = self.config['command_watcher']
        if status == True:
            if message.raw_text == command:
                chat = await message.client(GetFullChannelRequest(-1001914297016))
                description = chat.full_chat.about.split(' | ')
                slp = description[0]
                status = description[1]
                prefix = utils.escape_html(self.get_prefix())
                chat_id = -1001914297016
                dialogs = await self.client.get_dialogs()
                chat = None
                for d in dialogs:
                    if d.id == chat_id:
                        chat = d
                        break
                if chat is None:
                    await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error</b> | <code>{prefix}bosslist</code>\nДля работы модуля вы должны находится в чате @shxbosslist')
                    return
                bosslist = await self.client.get_messages(-1001914297016,limit=1)
                bosslist = bosslist[0].text
                
                if status == 'True':
                    if bosslist in ['босс лист', 'Босс лист']:
                        prefix = utils.escape_html(self.get_prefix())
                        await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error |</b> <code>{prefix}bosslist</code>\nБосс лист находился на стадии обновления, пожалуйста, попробуйте снова.')
                        return
                    else:                              
                        bosslist = bosslist[32:]
                        await utils.answer(message, f'<emoji document_id=5204044038126182496>✅</emoji> Босс лист готов.{bosslist}\n\n<emoji document_id=5328274090262275771>🕐</emoji> Босс лист обновляется каждые <code>{slp}<code> секунд.')
                        return
                else:
                    await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error |</b> <code>{prefix}bosslist</code>\nВ данный момент возможность просмотра босс листа отключена.')



    @loader.command(alias = 'bl')
    async def bosslist(self, message):
        ''' - получить босс лист'''

        
        chat = await message.client(GetFullChannelRequest(-1001914297016))
        description = chat.full_chat.about.split(' | ')
        slp = description[0]
        status = description[1]
        prefix = utils.escape_html(self.get_prefix())
        chat_id = -1001914297016
        dialogs = await self.client.get_dialogs()
        chat = None
        for d in dialogs:
            if d.id == chat_id:
                chat = d
                break
        if chat is None:
            await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error</b> | <code>{prefix}bosslist</code>\nДля работы модуля вы должны находится в чате @shxbosslist')
            return
        bosslist = await self.client.get_messages(-1001914297016,limit=1)
        bosslist = bosslist[0].text
        
        if status == 'True':
            if bosslist in ['босс лист', 'Босс лист']:
                prefix = utils.escape_html(self.get_prefix())
                await utils.answer(message, f'Босс лист находился на стадии обновления, пожалуйста, попробуйте снова.')
                return
            else:                              
                bosslist = bosslist[32:]
                await utils.answer(message, f'<emoji document_id=5204044038126182496>✅</emoji> Босс лист готов.{bosslist}\n\n<emoji document_id=5328274090262275771>🕐</emoji> Босс лист обновляется каждые <code>{slp}<code> секунд.')
                return
        else:
            await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Error |</b> <code>{prefix}bosslist</code>\nВ данный момент возможность просмотра босс листа отключена.')