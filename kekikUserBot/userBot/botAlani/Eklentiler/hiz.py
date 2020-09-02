# https://github.com/Skuzzy_xD/TelePyroBot

from pyrogram import Client, filters
import asyncio
from speedtest import Speedtest

def speed_convert(size):
    power = 2 ** 10
    zero = 0
    units = {0: '', 1: 'Kb/s', 2: 'Mb/s', 3: 'Gb/s', 4: 'Tb/s'}
    while size > power:
        size /= power
        zero += 1
    return f"{round(size, 2)} {units[zero]}"

@Client.on_message(filters.command("hiz", ['!','.','/']) & filters.me)
async def hiztesti(client, message):
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
    
    await ilk_mesaj.edit("`Hız testi yapılıyor . . .`")
    test = Speedtest()
    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()
    await ilk_mesaj.edit("**Başlama Zamanı:** "
                       f"`{result['timestamp']}`\n\n"
                       "**Download:** "
                       f"`{speed_convert(result['download'])}`\n"
                       "**Upload:** "
                       f"`{speed_convert(result['upload'])}`\n"
                       "**Ping:** "
                       f"`{result['ping']} ms`\n"
                       "**ISP:** "
                       f"`{result['client']['isp']}`")