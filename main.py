#Dint Skid Bitch
#By XinOnGithub
#https://www.youtube.com/channel/UC-8t8_KCMoX5YpjbivyeIYQ

import requests, json, sys, time
from threading import Thread,active_count
from colorama import Fore, init, Style
from os import system, name
init()

with open('config.json') as f:
	cfg = json.load(f)

Threads = cfg.get("Threads")
Timeout = cfg.get("Timeout")
Console_Details = cfg.get("Console_Details")
Website = cfg.get("Website")

def menu():
    if name == 'posix':
        system('clear')
        system('clear')
    elif name in ('ce', 'nt', 'dos'):
        system('cls')
        system('cls')
    else:
        print("Please Check config.json File")
        exit()
    banner = f"""
                                    {Fore.LIGHTMAGENTA_EX}╔═══════════════════════════════════════════════╗{Fore.RESET}
                                    {Fore.LIGHTMAGENTA_EX}║{Fore.RESET}   __   __   __             ___  __   __       {Fore.LIGHTMAGENTA_EX}║{Fore.RESET}
                                    {Fore.LIGHTMAGENTA_EX}║{Fore.RESET}  |__) |__) /  \ \_/ \ /     |  /  \ /  \ |    {Fore.LIGHTMAGENTA_EX}║{Fore.RESET}
                                    {Fore.LIGHTMAGENTA_EX}║{Fore.RESET}  |    |  \ \__/ / \  |      |  \__/ \__/ |___ {Fore.LIGHTMAGENTA_EX}║{Fore.RESET}
                                    {Fore.LIGHTMAGENTA_EX}║{Fore.RESET}                                               {Fore.LIGHTMAGENTA_EX}║{Fore.RESET}
                                    {Fore.LIGHTMAGENTA_EX}╚═══════════════════════════════════════════════╝{Fore.RESET}
                                             {Fore.LIGHTMAGENTA_EX}  A PowerFull Proxy Checker ! {Fore.RESET}
    """
    print(banner)

def RFile(file,method):
    with open(file,method) as file:
        a = [line.strip('\n') for line in file]
        return a

def CheckProxy(proxy, Website):
	try:
		rqss = requests.get(Website, proxies={'http': 'http://'+proxy, 'https': 'http://'+proxy},timeout=Timeout)
		system(f"title [ Most Powerfull Proxy Checker ] ~ Threads {active_count()-1}")
		if Console_Details == "True":
			print(f"{Fore.LIGHTGREEN_EX}[GOOD] {proxy}\n")
		else:
			pass
		valid = open('Result/Good.txt', 'a')
		valid.write(proxy+"\n")
		valid.close()
	except:
		system(f"title [ Most Powerfull Proxy Checker ] ~ Threads {active_count()-1}")
		if Console_Details == "True":
			print(f"{Fore.RED}[BAD] {proxy}\n")
		else:
			pass
		bad = open('Result/Dead.txt', 'a')
		bad.write(proxy+"\n")
		bad.close()

def Runner(Website,Threads,Timeout,Console_Details):
    menu()
    proxy_list = RFile('Proxy.txt','r')
    proxy_count = len(proxy_list)
    print(f"Loaded {proxy_count} proxy")
    print(f"Config details : Website : {Website} | Threads : {Threads} | Timeout : {Timeout} | Console Details : {Console_Details}\nPress enter to start!")
    system("pause >nul")
    time.sleep(1)
    for proxy in proxy_list:
        a = True
        while a:
            if active_count() <= Threads:
                Thread(target=CheckProxy,args=(proxy, Website, )).start()
                a = False

if __name__ == "__main__":
    try:
        Runner(Website,Threads,Timeout,Console_Details)
        time.sleep(3)
        menu()
        print(Fore.GREEN,"Checked all proxy with succes.")
    except KeyboardInterrupt:
        print("Stopped by user")
    except IndexError:
        print("Put proxy in Proxy.txt file")
    except:
	    print("Something went wrong")

