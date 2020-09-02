# https://github.com/Skuzzy_xD/TelePyroBot

from pyrogram import Client, filters
import asyncio
import random

@Client.on_message(filters.command("stik", ['!','.','/']) & filters.me)
async def stik(client, message):
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

    if cevaplanan_mesaj is None:
        await ilk_mesaj.edit("__stikır yapılacak mesajı yanıtlamalısın..__")
        return

    await ilk_mesaj.edit("`Stikır yapıyorum`")
    await cevaplanan_mesaj.forward("@QuotLyBot")
    
    stik_mi = False
    bar = 0
    hata_limit = 0
    
    while not stik_mi:
        try:
            msg = await client.get_history("@QuotLyBot", 1)
            kontrol = msg[0]["sticker"]["file_id"]
            stik_mi = True
        except:
            await asyncio.sleep(0.5)
            bar += random.randint(0, 10)
            try:
                await ilk_mesaj.edit(f"**Stikır**\n\n`İşleniyor %{bar}`", parse_mode="md")
                if bar >= 100:
                    pass
            except Exception as hata:
                await ilk_mesaj.edit(f"**Uuppss:**\n\n`{hata}`", parse_mode="md")
                hata_limit += 1
                if hata_limit == 3:
                    break
    
    await ilk_mesaj.edit("`Tamamlandı !`", parse_mode="md")
    msg_id = msg[0]["message_id"]
    await client.forward_messages(message.chat.id, "@QuotLyBot", msg_id)
    await client.read_history("@QuotLyBot")
    await ilk_mesaj.delete()