# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from pyrogram import Client, filters
import asyncio
import requests
import os

@Client.on_message(filters.command(['pastever'], ['!','.','/']) & filters.me)
async def pastever(client, message):
    # < Başlangıç
    await message.reply_chat_action("typing")
    await asyncio.sleep(0.3)
    uyku = await message.edit("__asyncio.sleep(0.3)__")

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
    if cevaplanan_mesaj is None:
        if len(girilen_yazi.split()) == 1:
            await ilk_mesaj.edit("Paste yapabilmek için `uzantı` ve `kod` vermelisiniz..")
            return
        elif len(girilen_yazi.split()) == 2:
            await ilk_mesaj.edit("Paste yapabilmek için `uzantı` da vermelisiniz..\n\n`.pastever py` **kod**")
            return
        kod = " ".join(girilen_yazi.split()[2:]) 

    elif cevaplanan_mesaj and cevaplanan_mesaj.document:
        if len(girilen_yazi.split()) == 1:
            await ilk_mesaj.edit("Paste yapabilmek için `uzantı` da vermelisiniz..\n\n`.pastever py`")
            return
        
        gelen_dosya = await cevaplanan_mesaj.download()
        
        veri_listesi = None
        with open(gelen_dosya, "rb") as oku:
            veri_listesi = oku.readlines()

        inen_veri = ""
        for veri in veri_listesi:
            inen_veri += veri.decode("UTF-8")
        
        kod = inen_veri

        os.remove(gelen_dosya)

    elif cevaplanan_mesaj.text:
        if len(girilen_yazi.split()) == 1:
            await ilk_mesaj.edit("Paste yapabilmek için `uzantı` da vermelisiniz..\n\n`.pastever py`")
            return
        kod = cevaplanan_mesaj.text

    else:
        await ilk_mesaj.edit("__güldük__")
        return

    uzanti = message.text.split()[1]
    await ilk_mesaj.delete()
    
    sonuc = requests.post(f"https://hastebin.com/documents", data = kod.encode("utf-8")).json()

    await message.reply(f'https://hastebin.com/{sonuc["key"]}.{uzanti}',
                  disable_web_page_preview  = True,
                  reply_to_message_id       = yanitlanacak_mesaj
                  )

@Client.on_message(filters.command(['pasteal'], ['!','.','/']) & filters.me)
async def pasteal(client, message):
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
        await ilk_mesaj.edit("__script'e çevrilecek hastebin linki yanıtlamanız gerekli..__")
        return
    elif not cevaplanan_mesaj.text.startswith("https://hastebin.com"):
        await ilk_mesaj.edit("__sadece hastebin linki yanıtlaman gerekli..__\n\n`.pasteal`")
        return
    
    kod = message.reply_to_message.text.split('/')[-1]
    uzanti = kod.split('.')[1]
    raw = 'https://hastebin.com/raw/' + kod.split('.')[0]
    
    try:
        data = requests.get(raw).content
    except Exception as hata:
        await ilk_mesaj.edit(f"**Uuppss:**\n\n`{hata}`")

    await ilk_mesaj.delete()

    with open(f'{kod}', "wb+") as dosya: dosya.write(data)
    
    await message.reply_document(
            document                    = f"{kod}",
            caption                     = '__KekikAkademi Robot tarafından dönüştürülmüştür__',
            disable_notification        = True,
            reply_to_message_id         = cevaplanan_mesaj.message_id
        )
    os.remove(f"{kod}")