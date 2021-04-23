#Dont Skid Bitch
#By XinOnGithub
#https://www.youtube.com/channel/UC-8t8_KCMoX5YpjbivyeIYQ

import requests, json, sys, time
from threading import Thread,active_count
from colorama import Fore, init, Style
from os import system, name
init()

def RFile(file,method):
    with open(file,method) as file:
        a = [line.strip('\n') for line in file]
        return a

def PrintLogo():
    system("cls" if name == 'nt' else 'clear')
    print(f"""
                                    {Fore.LIGHTMAGENTA_EX}╔═══════════════════════════════════════════════╗{Fore.RESET}
                                    {Fore.LIGHTMAGENTA_EX}║{Fore.RESET}   __   __   __             ___  __   __       {Fore.LIGHTMAGENTA_EX}║{Fore.RESET}
                                    {Fore.LIGHTMAGENTA_EX}║{Fore.RESET}  |__) |__) /  \ \_/ \ /     |  /  \ /  \ |    {Fore.LIGHTMAGENTA_EX}║{Fore.RESET}
                                    {Fore.LIGHTMAGENTA_EX}║{Fore.RESET}  |    |  \ \__/ / \  |      |  \__/ \__/ |___ {Fore.LIGHTMAGENTA_EX}║{Fore.RESET}
                                    {Fore.LIGHTMAGENTA_EX}║{Fore.RESET}                                               {Fore.LIGHTMAGENTA_EX}║{Fore.RESET}
                                    {Fore.LIGHTMAGENTA_EX}╚═══════════════════════════════════════════════╝{Fore.RESET}
                                             {Fore.LIGHTMAGENTA_EX}  A PowerFull Proxy Checker ! {Fore.RESET}""")



def CheckProxy(proxy, Timeout):
	try:
		requests.get('https://www.google.com/', proxies={'http': f'http://{proxy}', 'https': f'https://{proxy}'}, timeout=Timeout)
		print(f"{Fore.LIGHTGREEN_EX}[GOOD] {proxy}\n")
		valid = open('Result/Good.txt', 'a').write(proxy+"\n")
		valid.close()
	except:
		print(f"{Fore.RED}[BAD] {proxy}\n")

def Runner():
    Timeout = int(input("Timeout :"))
    Threads = int(input("Threads :"))
    proxy_list = RFile('Proxy.txt','r')
    time.sleep(2)
    for proxy in proxy_list:
        a = True
        while a:
            if active_count() <= Threads:
                Thread(target=CheckProxy,args=(proxy, Timeout)).start()
                a = False

if __name__ == "__main__":
    try:
        PrintLogo()
        Runner()
        time.sleep(3)
        PrintLogo()
        print(f"{Fore.GREEN}Checked all proxy with succes.")
    except KeyboardInterrupt:
        print("Stopped by user")
    except IndexError:
        print("Put proxy in Proxy.txt file")
    except:
	    print("Something went wrong")
