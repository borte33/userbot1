from konsolTaban import *
from sistemBot.keyifRobot import baslangic, bilgi, onemli
from sistemBot.botAlani import keyifRobot
from os import listdir

#-----------------------------------#
print(Fore.GREEN + logo)        # yeşil renk koduyla logomuzu yazdırdık
print(ust_bilgi)                # Üst Bilgimizi yazdırdık

baslangic()

onemli("Eklentilerim;\n")

eklentiler = ""

for dosya in listdir("./sistemBot/botAlani/Eklentiler/"):
    if not dosya.endswith(".py"):
        continue
    eklentiler += f"📂 {dosya.replace('.py','')} | "

bilgi(f"{eklentiler}\n\n")

if __name__ == "__main__":
    keyifRobot.run()