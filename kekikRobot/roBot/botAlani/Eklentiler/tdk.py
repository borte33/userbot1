# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from pyrogram import Client, filters
import asyncio
import requests

@Client.on_message(filters.command(['tdk'], ['!','.','/']))
async def tdk(client, message):
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

    girilen_yazi = message.text
    if len(girilen_yazi.split()) == 1:
        await ilk_mesaj.edit("Arama yapabilmek için `bişeyler` girmelisiniz")
        return
    
    kelime = " ".join(girilen_yazi.split()[1:])

    if len(kelime.split()) > 1:
        mesaj = "**Lütfen tek kelime girin**"
        return

    istek = requests.get(f"http://sozluk.gov.tr/gts?ara={kelime}")

    kelime_anlamlari = istek.json()

    if "error" in kelime_anlamlari:
        mesaj = f"`{kelime}` `sozluk.gov.tr` __sitesinde bulunamadı..__"
    else:
        mesaj = f"📚 **{kelime}** __Kelimesinin Anlamları:__\n\n"
        anlamlar = kelime_anlamlari[0]["anlamlarListe"]
        for anlam in anlamlar:
            mesaj += f"👉 `{anlam['anlam']}` \n"

    try:
        await ilk_mesaj.edit(mesaj)
    except Exception as hata:
        await ilk_mesaj.edit(f"**Uuppss:**\n\n`{hata}`")
