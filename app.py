from colorama import Fore, Style
from termcolor import colored
import pyfiglet
import random

colors = ['grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white',
          'on_grey', 'on_red', 'on_green', 'on_yellow']

selected_color = random.choice(colors)

text = 'Application'

lo = pyfiglet.figlet_format(text)
colored_lo = colored(lo, color=selected_color)

print(colored_lo)

from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect_spy_devices')
def detect_spy_devices():

    spy_detected = False

    if spy_detected:
        return "تم اكتشاف جهاز تجسس. يُرجى أخذ الحيطة والحذر."
    
    return "لا توجد مشاكل تجسس."

if __name__ == '__main__':
    app.run(debug=True)
