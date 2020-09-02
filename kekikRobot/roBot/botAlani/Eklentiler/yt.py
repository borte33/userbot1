# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from pyrogram import Client, filters
import asyncio
from pytube import YouTube
import wget
import os

@Client.on_message(filters.command(['yt'], ['!','.','/']))
async def yt(client, message):
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
    if not cevaplanan_mesaj and (girilen_yazi.split()) == 1:
        await ilk_mesaj.edit("Arama yapabilmek için `Youtube Linki` girmelisiniz, veya @vid __mesajı yanıtlamalısınız..__")
        return

    if not cevaplanan_mesaj:
        verilen_link = " ".join(girilen_yazi.split()[1:])
    else:
        verilen_link = cevaplanan_mesaj.text

    if not cevaplanan_mesaj and (len(verilen_link.split())) > 1:
        await ilk_mesaj.edit("**Yalnızca Link Verin**")
        return

    if not verilen_link.split('?')[0].endswith('youtube.com/watch'):
        await ilk_mesaj.edit("**Youtube Video Linki Verdiğine Emin OL!**")
        return

    vid = YouTube(verilen_link)
    baslik = f"**{vid.title}**"
    await ilk_mesaj.edit(f"**{baslik}**\n\n\t__İndiriliyor__")
    video = vid.streams.get_highest_resolution().download()
    resim = wget.download(vid.thumbnail_url)
    
    await ilk_mesaj.edit(f"**{baslik}**\n\n\t__Yükleniyor__")
    await client.send_video(chat_id = message.chat.id, video = video, caption = baslik, thumb = resim, reply_to_message_id = yanitlanacak_mesaj)

    os.remove(video)
    os.remove(resim)
    await ilk_mesaj.delete()