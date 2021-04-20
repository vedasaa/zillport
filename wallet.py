# import random
"""
    vedpratama x SGBTEAM
    vedasaa
"""
import requests
import json
import os
import time
import colorama
import re
import html
from colorama import Fore, Back, Style

colorama.init(autoreset=True)
ovo = "zil18f5rlhqz9vndw4w8p60d0n7vg3n9sqvta7n6t2"
gopay = "zil1hpwshtxspjakjh5sn7vn4e7pp4gaqkefup24h2"
def becareful(target):
    bahaya = "https://api.viewblock.io/zilliqa/addresses/"+target+"?"
    header = {
        "Host": "api.viewblock.io",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Access-Control-Request-Method": "GET",
        "Access-Control-Request-Headers": "content-type",
        "Referer": "https://viewblock.io/",
        "Origin": "https://viewblock.io",
        "Connection": "keep-alive",
        "Cache-Control": "max-age=0"
    }
    liminho = {
        "network": "mainnet",
        "page": 1
    }
    w = requests.get(bahaya, params=liminho, headers=header)
    return w

# password = input("Wallet : ")
infofile = input("Nama filenya (xxx.txt) : ")
result = os.name
if result == 'nt':
    os.system('cls')
else :
    os.system('clear')
time.sleep(1)
print("\n"+Fore.YELLOW + "   Requesting . . .\n")
time.sleep(1)
datafile = []
try:
    with open(infofile) as f :
        datafile = f.readlines()
except FileNotFoundError:
    print("File gak ada!")
# except NameError:
    # print("")

for line in datafile:
    # print(line.rstrip())
    # print(type(line))
    hadiah = becareful(line.rstrip())
    hadiah1 = hadiah.json()
    hadiah2 = json.dumps(hadiah1, indent=4)
    hadiah3 = json.loads(hadiah2)
    saldoovo = hadiah3["tokens"]
    saldogopay = hadiah3["tokens"]
    if ovo in saldoovo and gopay in saldogopay:
        ovo1 = saldoovo[ovo]
        gopay1 = saldogopay[gopay]
        if "balance" in ovo1 and "balance" in gopay1:
            ovofinal = Fore.GREEN + str(int(ovo1["balance"])/10000)
            gopayfinal = Fore.GREEN + str(int(gopay1["balance"])/10000)
        elif "balance" in ovo1 and "balance" not in gopay1:
            ovofinal = Fore.GREEN + str(int(ovo1["balance"])/10000)
            gopayfinal = Fore.RED+"0"
        elif "balance" not in ovo1 and "balance" in gopay1:
            ovofinal = Fore.RED+"0"
            gopayfinal = Fore.GREEN + str(int(gopay1["balance"])/10000)
        else:
            ovofinal = Fore.RED+"0"
            gopayfinal = Fore.RED+"0"
    elif ovo in saldoovo and gopay not in saldogopay:
        ovo1 = saldoovo[ovo]
        gopayfinal = Fore.RED+"0"
        if "balance" in ovo1:
            ovofinal = Fore.GREEN + str(int(ovo1["balance"])/10000)
        else:
            ovofinal = Fore.RED+"0"
    elif ovo not in saldoovo and gopay in saldogopay:
        ovofinal = Fore.RED+"0"
        gopay1 = saldogopay[gopay]
        if "balance" in gopay1:
            gopayfinal = Fore.GREEN + str(int(gopay1["balance"])/10000)
        else :
            gopayfinal = Fore.RED+"0"
    else:
        ovofinal=Fore.RED+"0"
        gopayfinal=Fore.RED+"0"
    print(Fore.BLUE + "[+] " + Fore.CYAN+line.rstrip() + Fore.YELLOW +" " + "[Balance : " +ovofinal+" PORT "+ Fore.YELLOW +"| "+gopayfinal+ " XPORT"+ Fore.YELLOW +"]")
else:
    print("\n"+Fore.YELLOW + "   DONE !\n")
    # print(str(saldoovo) + "\n")
    # if 
    
        # continue
        # saldoovo = '0'
    # try:
    #     saldogopay = hadiah3["tokens"][gopay]["balance"]
    # except KeyError:
    #     saldogopay = '0'

    
    # print(saldoovo + "\n")

