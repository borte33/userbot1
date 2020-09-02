# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from pyrogram import Client, filters
import asyncio
import cv2
import os
from sistemBot.botAlani import bilgiler

@Client.on_message(filters.regex('foto ver'))
async def fotoVer(client, message):
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
    
    
    cap = cv2.VideoCapture(0)
    cap.set(3,640) #width=640
    cap.set(4,480) #height=480

    if cap.isOpened():
        _,frame = cap.read()
        cap.release() #releasing camera immediately after capturing picture
        if _ and frame is not None:
            cv2.imwrite('img.jpg', frame)

    await ilk_mesaj.delete()
    
    await message.reply_chat_action("upload_photo")
    foto = "img.jpg"
    await message.reply_photo(foto, reply_to_message_id = yanitlanacak_mesaj)
    os.remove(foto)


def yayin():
    cap = cv2.VideoCapture(0)

    while(True):
        ret, frame = cap.read()
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
 
        cv2.imshow('frame', rgb)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            out = cv2.imwrite('capture.jpg', frame)
            break

    cap.release()
    cv2.destroyAllWindows()