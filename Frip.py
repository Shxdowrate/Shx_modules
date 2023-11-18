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


import io
import random
import string

from PIL import Image, ImageFilter

from .. import loader, utils

@loader.tds
class Frip(loader.Module):
    """Всеразличные рамки для вашего фото!\nОснова для первого аргумента: #000000 - черный #ffffff - белый\nDeveloper: @mescr_m"""
    strings = {
        "name": "Frip",
        }
    
    @loader.command()
    async def frip(self, message):
        """[ Цвет рамки на англ, либо HEX ] [ Цвет подсветки на англ, либо HEX ] - создать рамку\nПример: .frip #000000 red\n"""
        args = utils.get_args_raw(message)
        args1 = (args.split(' ', 2)[0])
        args2 = (args.split(' ', 2)[1])
        
        
        
        R = False
        Q = "image"
        P = "/"
        L = "RGBA"
        K = "<b>Ответьте на фото/стикер</b>"
        A = message
        C = await A.get_reply_message()
        B = io.BytesIO()
        M = None
        if A.file:
            if A.file.mime_type.split(P)[0] == Q:
                await A.download_media(B)
            elif C:
                if C.file:
                    if C.file.mime_type.split(P)[0] == Q:
                        M = R
                        await C.download_media(B)
                else:
                    await A.edit(K)
                    return
            else:
                await A.edit(K)
                return
        elif C:
            if C.file:
                if C.file.mime_type.split(P)[0] == Q:
                    M = R
                    await C.download_media(B)
            else:
                await A.edit(K)
                return
        else:
            await A.edit(K)
            return
        try:
            I = Image.open(B) 
        except:
            await A.edit(K)
            return
        await A.edit("<b>В процессе...</b>")
        F, G = I.size
        B = Image.new(L, (F, G))
        J = min(F // 100, G // 100)
        D = Image.new(L, (F + J * 40, G + J * 40), f"{args1}")
        if I.mode == L:
            B.paste(I, (0, 0), I)
            E = Image.new(L, (F, G))
            for N in range(F):
                for O in range(G):
                    if B.getpixel((N, O)) != (0, 0, 0, 0):
                        E.putpixel((N, O), (0, 0, 0))
        else:
            B.paste(I, (0, 0))
            E = Image.new(L, (F, G), f"{args2}")
        E = E.resize((F + J * 5, G + J * 5))
        D.paste(E, ((D.width - E.width) // 2, (D.height - E.height) // 2), E)
        D = D.filter(ImageFilter.GaussianBlur(J * 5))
        D.paste(B, ((D.width - B.width) // 2, (D.height - B.height) // 2), B)
        H = io.BytesIO()
        H.name = (
            "-".join(
                [
                    "".join([random.choice(string.hexdigits) for B in range(A)])
                    for A in [5, 4, 3, 2, 1]
                ]
            )
            + ".png"
        )
        D.save(H, "PNG")
        H.seek(0)
        if utils.get_args_raw(A):
            await A.client.send_file(A.to_id, H, force_document=R)
            await A.delete()
        elif M:
            await C.reply(file=H)
            await A.delete()
        else:
            await A.edit(file=H, text="")
            
   
    @loader.command()
    async def ffrip(self, message):
        """[ Цвет рамки на англ, либо HEX ] [ Цвет подсветки на англ, либо HEX ] - создать рамку в виде файла\nПример: .ffrip #000000 red\n"""
        args = utils.get_args_raw(message)
        args1 = (args.split(' ', 2)[0])
        args2 = (args.split(' ', 2)[1])
        
        
        
        R = True
        Q = "image"
        P = "/"
        L = "RGBA"
        K = "<b>Ответьте на фото/стикер</b>"
        A = message
        C = await A.get_reply_message()
        B = io.BytesIO()
        M = None
        if A.file:
            if A.file.mime_type.split(P)[0] == Q:
                await A.download_media(B)
            elif C:
                if C.file:
                    if C.file.mime_type.split(P)[0] == Q:
                        M = R
                        await C.download_media(B)
                else:
                    await A.edit(K)
                    return
            else:
                await A.edit(K)
                return
        elif C:
            if C.file:
                if C.file.mime_type.split(P)[0] == Q:
                    M = R
                    await C.download_media(B)
            else:
                await A.edit(K)
                return
        else:
            await A.edit(K)
            return
        try:
            I = Image.open(B) 
        except:
            await A.edit(K)
            return
        await A.edit("<b>В процессе...</b>")
        F, G = I.size
        B = Image.new(L, (F, G))
        J = min(F // 100, G // 100)
        D = Image.new(L, (F + J * 40, G + J * 40), f"{args1}")
        if I.mode == L:
            B.paste(I, (0, 0), I)
            E = Image.new(L, (F, G))
            for N in range(F):
                for O in range(G):
                    if B.getpixel((N, O)) != (0, 0, 0, 0):
                        E.putpixel((N, O), (0, 0, 0))
        else:
            B.paste(I, (0, 0))
            E = Image.new(L, (F, G), f"{args2}")
        E = E.resize((F + J * 5, G + J * 5))
        D.paste(E, ((D.width - E.width) // 2, (D.height - E.height) // 2), E)
        D = D.filter(ImageFilter.GaussianBlur(J * 5))
        D.paste(B, ((D.width - B.width) // 2, (D.height - B.height) // 2), B)
        H = io.BytesIO()
        H.name = (
            "-".join(
                [
                    "".join([random.choice(string.hexdigits) for B in range(A)])
                    for A in [5, 4, 3, 2, 1]
                ]
            )
            + ".png"
        )
        D.save(H, "PNG")
        H.seek(0)
        if utils.get_args_raw(A):
            await A.client.send_file(A.to_id, H, force_document=R)
            await A.delete()
        elif M:
            await C.reply(file=H)
            await A.delete()
        else:
            await A.edit(file=H, text="")
             
