# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from pyrogram import Client, filters
import asyncio
import requests

@Client.on_message(filters.command(['akaryakit'], ['!','.','/']))
async def akaryakit(client, message):
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

    istek = requests.get(f"https://kolektifapi.herokuapp.com/akaryakit")

    api_yaniti = istek.json()

    mesaj = "__Güncel Akaryakıt Verileri;__\n\n"
    for yanit in api_yaniti:
        mesaj += f"`{yanit['fiyati'].split(' ')[0]} ₺`\t**{yanit['turu'].split(' -- ')[0]}**\n"

    try:
        await ilk_mesaj.edit(mesaj)
    except Exception as hata:
        await ilk_mesaj.edit(f"**Uuppss:**\n\n`{hata}`")