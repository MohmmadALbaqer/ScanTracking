import socket
from colorama import Fore, Style, init
from termcolor import colored
import random
import sys
import os
import time
from time import sleep
os.system

text = '''
.▄▄ ·  ▄▄·  ▄▄▄·  ▐ ▄   ▄▄▄▄▄▄▄▄▄   ▄▄▄·  ▄▄· ▄ •▄ ▪   ▐ ▄  ▄▄ • 
▐█ ▀. ▐█ ▌▪▐█ ▀█ •█▌▐█  ▀•██ ▀▀▄ █·▐█ ▀█ ▐█ ▌▪█▌▄▌▪██ •█▌▐█▐█ ▀ ▪
▄▀▀▀█▄██ ▄▄▄█▀▀█ ▐█▐▐▌    ▐█.▪▐▀▀▄ ▄█▀▀█ ██ ▄▄▐▀▀▄·▐█·▐█▐▐▌▄█ ▀█▄
▐█▄▪▐█▐███▌▐█▪ ▐▌██▐█▌    ▐█▌·▐█•█▌▐█▪ ▐▌▐███▌▐█.█▌▐█▌██▐█▌▐█▄▪▐█
 ▀▀▀▀ ·▀▀▀  ▀  ▀ ▀▀ █▪    ▀▀▀ .▀  ▀ ▀  ▀ ·▀▀▀ ·▀  ▀▀▀▀▀▀ █▪·▀▀▀▀ 
'''

colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan']

random_color = random.choice(colors)

colored_text = colored(text, random_color)
print(colored_text)

print(f'''
 {Fore.RED}<--------------------------------------------------------------------->
 {Fore.RED}|{Fore.GREEN} GitHub{Fore.WHITE} : {Fore.BLUE}MohmmadALbaqer {Fore.WHITE}|{Fore.YELLOW}   https://www.instagram.com/r94xs/        {Fore.RED}|
 {Fore.RED}|{Fore.GREEN} Instagram{Fore.WHITE} :{Fore.BLUE} r94xs {Fore.WHITE}      |{Fore.YELLOW}   https://www.github.com/MohmmadALbaqer/  {Fore.RED}|
 {Fore.RED}+---------------------------------------------------------------------+
''')

os.system("ifconfig")

class TerminalColors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    END = '\033[0m'

def detect_spy_devices(host, port):
    try:

        with socket.create_connection((host, port), timeout=2):
            print(f"{TerminalColors.RED}Warning: Spy device detected!{TerminalColors.END}")

    except (socket.timeout, ConnectionRefusedError):
        print(f"{TerminalColors.GREEN}No problem, the server is secure.{TerminalColors.END}")

server_address = input(f"Enter the server {Fore.GREEN}IP {Fore.WHITE}address: {Style.RESET_ALL}")
server_port = int(input(f"Enter the server {Fore.GREEN}port: {Style.RESET_ALL}"))

def wait_with_spinner(seconds, colors):
    symbols = "/-|\\"

    for _ in range(int(seconds)):
        for symbol in symbols:
            random_color = random.choice(colors)
            colored_symbol = colored(symbol, random_color)
            sys.stdout.write(f"\rPlease wait {colored_symbol}  ")
            sys.stdout.flush()
            time.sleep(0.25)

    sys.stdout.write("\r" + " " * 20 + "\r")

wait_time = 2.5
colors = ['grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
wait_with_spinner(wait_time, colors)

def spin():
    delay = 0.25
    spinner = ['█■■■■', '■█■■■', '■■█■■', '■■■█■', '■■■■█']

    for _ in range(3):
        for i in spinner:
            message = f"{Fore.GREEN}[{Fore.RED}*{Fore.GREEN}] {Fore.BLUE}scanning {Fore.WHITE}please wait.........[{i}]{Style.RESET_ALL}"
            colored_message = colored(message, 'blue', attrs=['bold'])
            sys.stdout.write(f"\r{colored_message}   ")
            sys.stdout.flush()
            time.sleep(delay)

    sys.stdout.write("\r")
    sys.stdout.flush()
    done_message = colored("scan completed", 'yellow', attrs=['bold'])
    sys.stdout.write("\033[K")
    print(done_message)
    time.sleep(3)

spin()

detect_spy_devices(server_address, server_port)
