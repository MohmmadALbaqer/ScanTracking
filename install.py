import os 
from colorama import Fore, Style
from termcolor import colored
import pyfiglet
import random

colors = ['grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

selected_color = random.choice(colors)

text = 'INSTALL'

lo = pyfiglet.figlet_format(text)
colored_lo = colored(lo, color=selected_color)

print(colored_lo)


os.system("pip install socket")
os.system("pip install colorama")
os.system("pip install termcolor")
os.system("pip install pyfiglet")
os.system("pip install Flask")
os.system("pip install sys")
os.system("sudo apt-get install g++")
