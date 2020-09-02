# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from pyrogram import Client, filters
import asyncio
import requests

@Client.on_message(filters.command(['sondakika'], ['!','.','/']) & filters.me)
async def sonDakika(client, message):
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

    istek = requests.get(f"https://kolektifapi.herokuapp.com/haber")

    api_yaniti = istek.json()

    mesaj = "📰 __NTV Kaynağından Son Dakika Haberleri;__\n\n"
    say = 0
    for yanit in api_yaniti:
        mesaj += f"🗞️ **[{yanit['Haber']}]({yanit['Link']})**\n\n"
        say += 1
        if say == 5:
            break

    try:
        await ilk_mesaj.edit(mesaj, disable_web_page_preview=True)
    except Exception as hata:
        await ilk_mesaj.edit(f"**Uuppss:**\n\n`{hata}`")