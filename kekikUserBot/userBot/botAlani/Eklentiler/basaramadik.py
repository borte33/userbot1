# https://github.com/Quiec/AsenaUserBot

from pyrogram import Client, filters
import asyncio

@Client.on_message(filters.command(['basaramadik'], ['!','.','/']) & filters.me)
async def basaramadik(client, message):
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

    await ilk_mesaj.edit("Başaramadık Abi")

    animasyon = [
        "oLuM gE BurAyA QırMızi ŞortLi",
        "uLaN sEn bEnim EliMdeN tUttun İBiNe",
        "Benİ bUrdan YuQarı ÇekMedİn ULAN",
        "bEn boĞuLim ÇeQmeDin bEnİ",
        "sEnle MahMüd",
        "BAŞARAMADIK ABİ",
        "nEyi BAşaraMadıN AmınaGoyim",
        "...",
        "GüLme OğlıM ŞerEfSız",
        "**QırMızi ŞortLi SuNar**"
        ]
    
    for anime in animasyon:
        await asyncio.sleep(0.7)
        await ilk_mesaj.edit(anime)
    
    await asyncio.sleep(3)

    yarak = '...............▄▄ ▄▄\n......▄▌▒▒▀▒▒▐▄\n.... ▐▒▒▒▒▒▒▒▒▒▌\n... ▐▒▒▒▒▒▒▒▒▒▒▒▌\n....▐▒▒▒▒▒▒▒▒▒▒▒▌\n....▐▀▄▄▄▄▄▄▄▄▄▀▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n...▄█▓░░░░░░░░░▓█▄\n..▄▀░░░░░░░░░░░░░ ▀▄\n.▐░░░░░░░▀▄▒▄▀░░░░░░▌\n▐░░░░░░░▒▒▐▒▒░░░░░░░▌\n▐▒░░░░░▒▒▒▐▒▒▒░░░░░▒▌\n.▀▄▒▒▒▒▒▄▀▒▀▄▒▒▒▒▒▄▀\n.. ▀▀▀▀▀ ▀▀▀▀▀'

    await ilk_mesaj.edit(yarak)
    
    await ilk_mesaj.delete()