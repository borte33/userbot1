from pyrogram import Client, filters
import asyncio

@Client.on_message(filters.command(['deli'], ['!','.','/']) & filters.me)
async def deli(client, message):
    # < Başlangıç
    uyku = await message.edit("__asyncio.sleep(0.3)__")
    await asyncio.sleep(0.3)
    
    cevaplanan_mesaj    = message.reply_to_message
    if cevaplanan_mesaj is None:
        yanitlanacak_mesaj  = message.message_id
    else:
        yanitlanacak_mesaj = cevaplanan_mesaj.message_id
    
    await uyku.delete()
    
    for _ in range(50):
        ilk_mesaj = await message.reply("asdas")
        await asyncio.sleep(0.3)
        await ilk_mesaj.delete()