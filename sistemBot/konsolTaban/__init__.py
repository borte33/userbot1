#!/usr/bin/env python
#! -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

#-------------------------------#
import os                       # Dizinler ve dosyalarla çalışmak için
import platform                 # Çalışılan makine bilgisi sağlayacak arkadaş
import time,datetime,pytz       # Zaman/Tarih Bilgisi sağlayacak arkadaşlar
import ctypes                   # C dili veri tipleri kullanmamızı sağlayacak arkadaş (.DLL / .SO)
import colorama                 # Ortalığın renklenmesini sağlayacak arkadaş
from colorama import Fore       # Boyamayı kolaylaştıran arkadaş (BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE)
colorama.init(autoreset=True)   # Renklerin ilgili satırdan başka satıra devam etmemesi için
import requests                 # Websitelerine istek atmamızı sağlayacak arkadaş (ip için)
from time import sleep          # Uyku Vakti
#-------------------------------#

#---------------------------------------------------------------#
## GenelDegiskenler
pencere_basligi = "@keyifRobot / sistemBot"
bildirim_metni  = "keyifRobot\n sistemBot Başlatıldı.."
logo = '''
     _                _  ___ ______        _                
    | |              (_)/ __|_____ \      | |          _    
    | |  _ ____ _   _ _| |__ _____) ) ___ | | _   ___ | |_  
    | | / ) _  ) | | | |  __|_____ ( / _ \| || \ / _ \|  _) 
    | |< ( (/ /| |_| | | |        | | |_| | |_) ) |_| | |__ 
    |_| \_)____)\__  |_|_|        |_|\___/|____/ \___/ \___)
               (____/                                       
'''                                                             # Logomuz
        # logo = http://patorjk.com/software/taag/#p=display&f=Stop&t=keyifRobot
#---------------------------------------------------------------#
try:
    kullanici_adi = os.getlogin()                                     # Kullanıcı Adı
except:
    import pwd
    kullanici_adi = pwd.getpwuid(os.geteuid())[0]                     # Kullanıcı Adı

bilgisayar_adi = platform.node()                                      # Bilgisayar Adı
oturum = kullanici_adi + "@" + bilgisayar_adi                         # Örn.: "kekik@Administrator"

isletim_sistemi = platform.system()                                        # İşletim Sistemi
bellenim_surumu = platform.release()                                       # Sistem Bellenim Sürümü
cihaz = isletim_sistemi + " | " + bellenim_surumu                          # Örn.: "Windows | 10"

tarih = datetime.datetime.now(pytz.timezone("Turkey")).strftime("%d-%m-%Y") # Bugünün Tarihi
saat = datetime.datetime.now(pytz.timezone("Turkey")).strftime("%H:%M")     # Bugünün Saati
zaman = tarih + " | " + saat

ip_req = requests.get('http://ip.42.pl/raw')    # Harici IP'yi bulmak için bir GET isteği yolluyoruz
ip = ip_req.text                                # ip Adresi

ust_bilgi = f"\t\t{Fore.LIGHTBLACK_EX}{kullanici_adi} {Fore.LIGHTGREEN_EX}({ip})\n"
ust_bilgi += f"\t\t  {Fore.LIGHTRED_EX}{cihaz}\n"
ust_bilgi += f"\t\t   {Fore.YELLOW}{zaman}\n"
#-----------------------------------------------#

#---------------------------------------#
def temizle():                          # Temizle adında bir fonksiyon oluşturduk
    if isletim_sistemi == "Windows":    # Eğer İşletim Sistemi "Windows" ise
        os.system("cls")                # Sisteme "cls" komutu gönder
    else:                               # Sistem Windows değil ise
        os.system("clear")              # Sisteme "clear" komutu gönder
temizle()                               # Temizle fonksiyonumuzu çağırdık
#---------------------------------------#

#---------------------------------------------------------------------------#
def pencereBasligi():                                                       # PencereBasligi fonksiyonu
    if isletim_sistemi == "Windows":                                        # Eğer İşletim Sistemi "Windows" ise
        ctypes.windll.kernel32.SetConsoleTitleW(f"{pencere_basligi}")       # Konsol Başlığını ayarla
    elif platform.machine() == "aarch64":                                   # Eğer İşletim Sistemi "Android" ise
        pass                                                                # boşkoy
    elif isletim_sistemi == "Linux":                                        # Eğer İşletim Sistemi "Linux" ise
        os.system(f'echo "\033]0;{pencere_basligi}\007"')                   # Başlık Ayarla
    else:                                                                   # Hiçbiri değil ise
        os.system(f'title {pencere_basligi}')                               # Başlık Ayarla
pencereBasligi()                                                            # PencereBasligi çağır
#---------------------------------------------------------------------------#

#----------------------------------------------------#
def bildirim():
    if kullanici_adi == "gitpod":
        pass
    elif bellenim_surumu.split('-')[-1] == 'aws':
        pass
    elif platform.machine() == "aarch64":
        pass 
    elif isletim_sistemi == "Windows" and bellenim_surumu >= "10":
        try:
            from win10toast import ToastNotifier
        except:
            os.system('pip install win10toast')
            from win10toast import ToastNotifier
        
        bildirim = ToastNotifier()
        bildirim.show_toast(f"{pencere_basligi}", f"{bildirim_metni}",
            icon_path=None, duration=10, threaded=True
            )
    elif isletim_sistemi == "Linux":
        try:
            import notify2
        except:
            os.system('pip install notify2')
            import notify2
        
        notify2.init(pencere_basligi)
        bildirim = notify2.Notification(f"{pencere_basligi}", f"{bildirim_metni}", "notification-message-im")
        bildirim.show()
    else:
        pass
bildirim()
#----------------------------------------------------#
