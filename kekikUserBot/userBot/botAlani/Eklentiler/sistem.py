# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from pyrogram import Client, filters
import asyncio
import requests, os, platform

@Client.on_message(filters.command(['sistem'], ['!','.','/']) & filters.me)
async def sistem(client, message):
    # < Başlangıç
    uyku = await message.edit("__asyncio.sleep(0.3)__")
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

    try:
        mesaj = f"""__Kullanıcı :__ `{os.getlogin()}@{platform.node()}`
    __IP :__ `{requests.get('http://ip.42.pl/raw').text}`
    __OS :__ `{platform.system()} | {platform.release()}`
    __İşlemci :__ `{platform.processor()}`"""
        await ilk_mesaj.edit(mesaj)
    
    except Exception as hata:
        await ilk_mesaj.edit(f"__başaramadık abi__\n\n\t`{hata}`")