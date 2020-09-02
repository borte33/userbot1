# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from pyrogram import Client, filters
import asyncio
import os, pwd
from pyngrok import ngrok
from sistemBot.botAlani import bilgiler

ngrok.set_auth_token(bilgiler['ngrok_token'])

try:
    kullanici_adi = os.getlogin()                                     # Kullanıcı Adı
except:
    kullanici_adi = pwd.getpwuid(os.geteuid())[0]                     # Kullanıcı Adı

@Client.on_message(filters.regex('ssh aç'))
async def ssh(client, message):
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

    # girilen_yazi = message.text
    # if len(girilen_yazi.split()) == 1:
    #     await ilk_mesaj.edit("**ngrok ssh aç/kapat**")
    #     return
    # await ilk_mesaj.edit("__İşlem Gerçekleştiriliyor..__")

    if message.from_user.id != bilgiler['kurucu']:
        await ilk_mesaj.edit(f"Admin değilmişim :)\n\n`{message.from_user.id}` __!=__ `{bilgiler['kurucu']}`")
        return

    # Open a SSH tunnel
    ssh_url = ngrok.connect(22, "tcp")

    domain, port = ssh_url[6:].split(":")
    ssh_komut = f"ssh {kullanici_adi}@{domain} -p{port}"

    await ilk_mesaj.edit(f"**{kullanici_adi}** __oturumunda__\n\n`{ssh_komut}`")

@Client.on_message(filters.regex('flask aç'))
async def flask(client, message):
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
    
    ssh_url = ngrok.connect(5000)

    await ilk_mesaj.edit(f"**{kullanici_adi}** __oturumunda__\n\n__Flask Yayını__ `{ssh_url}`")


@Client.on_message(filters.regex('ngrok kapat'))
async def ngrokKapat(client, message):
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
    
    tuneller = ngrok.get_tunnels()
    
    kapatildi = ''
    for tunel in range(len(tuneller)):
        kapatildi += f"`{tuneller[tunel].public_url}`\n"
    
    ngrok.kill()
    await ilk_mesaj.edit(f"**{kullanici_adi}** __oturumunda__\n\n{kapatildi}__kapatıldı__")