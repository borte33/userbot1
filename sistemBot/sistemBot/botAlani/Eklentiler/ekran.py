# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from pyrogram import Client, filters
import asyncio
from PIL import ImageGrab
import os
from sistemBot.botAlani import bilgiler

@Client.on_message(filters.regex('ekran ver'))
async def ssVer(client, message):
    # < Başlangıç
    uyku = await message.reply("__asyncio.sleep(0.3)__")
    await asyncio.sleep(0.3)
    
    cevaplanan_mesaj    = message.reply_to_message
    if cevaplanan_mesaj is None:
        yanitlanacak_mesaj  = message.message_id
    else:
        yanitlanacak_mesaj = cevaplanan_mesaj.message_id
    
    await uyku.delete()
    ilk_mesaj = await message.reply("__Bekleyin..__",
        reply_to_message_id         = yanitlanacak_mesaj,
        disable_web_page_preview    = True,
        parse_mode                  = "Markdown"
    )
    #------------------------------------------------------------- Başlangıç >
    
    if message.from_user.id != bilgiler['kurucu']:
        await ilk_mesaj.edit(f"Admin değilmişim :)\n\n`{message.from_user.id}` __!=__ `{bilgiler['kurucu']}`")
        return
    
    ekran = ImageGrab.grab()
    ekran.save('Sreenshot.png')

    await ilk_mesaj.delete()
    
    await message.reply_chat_action("upload_photo")
    foto = "Sreenshot.png"
    await message.reply_photo(foto, reply_to_message_id = yanitlanacak_mesaj)
    os.remove(foto)