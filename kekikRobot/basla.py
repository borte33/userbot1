from konsolTaban import *
from roBot.kekikRobot import baslangic, bilgi, onemli
from roBot.botAlani import kekikRobot
from os import listdir

#-----------------------------------#
print(Fore.GREEN + logo)        # yeşil renk koduyla logomuzu yazdırdık
print(ust_bilgi)                # Üst Bilgimizi yazdırdık

baslangic()

onemli("Eklentilerim;\n")

eklentiler = ""

for dosya in listdir("./roBot/botAlani/Eklentiler/"):
    if not dosya.endswith(".py"):
        continue
    eklentiler += f"📂 {dosya.replace('.py','')} | "

bilgi(f"{eklentiler}\n\n")

if __name__ == "__main__":
    kekikRobot.run()
