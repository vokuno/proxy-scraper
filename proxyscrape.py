import os
from colorama import Fore
import platform
import time
from time import sleep
import requests
from tqdm import tqdm

clear=""
def oscheck():
    global clear
    ops = platform.system()
    if ops =="Windows":
        clear = "cls"
    else:
        clear = "clear"
    print(f"Running {ops} scraper.")
    time.sleep(1)

NormalBlack = "\033[38;5;0m  \033[0m"
NormalRed = "\033[38;5;1m  \033[0m"
NormalGreen = "\033[38;5;2m  \033[0m"
NormalYellow = "\033[38;5;3m  \033[0m"
NormalBlue = "\033[38;5;4m  \033[0m"
NormalMagenta = "\033[38;5;5m  \033[0m"
NormalCyan = "\033[38;5;6m  \033[0m"
NormalWhite =  "\033[38;5;7m  \033[0m"
BrightBlack = "\033[48;5;0m  \033[0m"
BrightRed =  "\033[48;5;1m  \033[0m"
BrightGreen = "\033[48;5;2m  \033[0m"
BrightYellow = "\033[48;5;3m  \033[0m"
BrightBlue = "\033[48;5;4m  \033[0m"
BrightMagenta = "\033[48;5;5m  \033[0m"
BrightCyan = "\033[48;5;6m  \033[0m"
BrightWhite = "\033[48;5;7m  \033[0m"

def main():
    global clear
os.system(clear)
print(f'''

    \033[0m\r\n
    \033[00;1;95m                       	  █▀▀ █▀█ ▄▀█ \033[00;1;96m█▀█ █▀█ █▄█                                    \033[0m\r
    \033[00;1;95m                       	  █▄▄ █▀▄ █▀█ \033[00;1;96m█▀▀ █▀▀  █\n                                    \033[0m\r
    \033[00;1;95m                              █▀█ █▀█ █▀█ \033[00;1;96m▀▄▀ █▄█                                        \033[0m\r
    \033[00;1;95m                              █▀▀ █▀▄ █▄█ \033[00;1;96m█ █  █\n
    \033[00;1;95m                              █▀ █▀▀ █▀█ \033[00;1;96m▄▀█ █▀█ █▀▀ █▀█
    \033[00;1;95m                              ▄█ █▄▄ █▀▄ \033[00;1;96m█▀█ █▀▀ ██▄ █▀▄
    \033[00;1;95m                   ╔════════════════════\033[00;1;96m════════════════════╗\033[0m\r
    \033[00;1;95m                   ║- - - - - - Made by:\033[00;1;96m \033[96mVokuno!\033[00;1;96m - - - - - -║\033[0m\r
    \033[00;1;95m                   ║- - - - - - - - - - \033[00;1;96m- - - - - - - - - - \033[00;1;96m║
    \033[00;1;95m                   ╚════════════════════\033[00;1;96m════════════════════╝\033[0m\r
''')

ssh = input(f"\033[00;1;95m[?]Enable SSH mode? y/n\n")
if ssh == "Y".lower():
    print("[+]Enabled SSH proxies")
    print("")
    rsp = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&country=all&anonymity=all&ssl=yes&timeout=2000')
    print(f"\033[00;1;96m\n[+] Downloading proxies...")
    for i in tqdm(range(4)):
        sleep(0.5)
        pass
    with open('proxies.txt','wb') as fp:
        fp.write(rsp.content)
        print(Fore.CYAN + "[✓] Proxies downloaded!")
else:
    print("[-]Disabled SSH proxies")
    print("")
    rsp = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&country=all&anonymity=all&ssl=all&timeout=1000')
    print(f"\033[00;1;96m\n[+] Downloading proxies...")
    for i in tqdm(range(3)):
        sleep(0.3)
        pass 
    with open('proxies.txt','wb') as fp:
        fp.write(rsp.content)
        print(Fore.CYAN + "[✓] Proxies downloaded!")

proxylst = str(print("\033[00;1;95m\nFinishing up..." + Fore.CYAN))
amount = len(open("proxies.txt","r+").readlines())
print(f"\033[00;1;96m \n[+] Downloaded: {amount} proxies")
input("\nPress ENTER to exit.")

main()