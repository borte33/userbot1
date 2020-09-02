from konsolTaban import *
from userBot.kekikUserBot import baslangic, bilgi, onemli
from userBot.botAlani import kekikUserBot
from os import listdir

#-----------------------------------#
print(Fore.GREEN + logo)        # yeşil renk koduyla logomuzu yazdırdık
print(ust_bilgi)                # Üst Bilgimizi yazdırdık

baslangic()

onemli("Eklentilerim;\n")

eklentiler = ""

for dosya in listdir("./userBot/botAlani/Eklentiler/"):
    if not dosya.endswith(".py"):
        continue
    eklentiler += f"📂 {dosya.replace('.py','')} | "

bilgi(f"{eklentiler}\n\n")

if __name__ == "__main__":
    kekikUserBot.run()