import socket
from colorama import Fore, Style
from termcolor import colored
import pyfiglet
import random
import sys
import time
from time import sleep

colors = ['grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white',
          'on_grey', 'on_red', 'on_green', 'on_yellow']

selected_color = random.choice(colors)

text = 'Scan Tracking'

lo = pyfiglet.figlet_format(text)
colored_lo = colored(lo, color=selected_color)

print(colored_lo)

insta_text = (
    "--------------------------------------------------\n"
    f"{Fore.RED}INSTAGRAM{Fore.YELLOW} ==> {Fore.CYAN}https://www.instagram.com/r94xs/{Style.RESET_ALL}   \n"
    f"{Fore.RED}GitHub{Fore.YELLOW} ==> {Fore.CYAN}https://www.github.com/MohmmadALbaqer/{Style.RESET_ALL}   \n"
    "--------------------------------------------------"
)
print(insta_text)


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

server_address = input("Enter the server IP address: ")
server_port = int(input("Enter the server port: "))


def wait_with_spinner(seconds):
    symbols = "/-|\\"

    for _ in range(int(seconds)):
        for symbol in symbols:
            sys.stdout.write(f"\rPlease wait {symbol}  ")
            sys.stdout.flush()
            time.sleep(0.25)

    sys.stdout.write("\r" + " " * 20 + "\r")

wait_time = 2.5
wait_with_spinner(wait_time)


detect_spy_devices(server_address, server_port)
