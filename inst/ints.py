#!/usr/bin/env python3
# hezron
import sys
import time
import os

# colors
ITALIC = "\033[3m"
purple = '\x1b[38;5;165m'
blue = '\x1b[38;5;33m'
red = '\x1b[38;5;196m'
green = '\x1b[38;5;118m'
grey = '\x1b[38;5;0m'
pink = '\x1b[38;5;199m'
END = "\033[0m"
UNDERLINE = "\033[4m"
BOLD = "\033[1m"
BLINK = "\033[5m"

# checking root privs
if not 'SUDO_UID' in os.environ.keys():
    sys.exit('\n{0}{1}{2}{3}Run this program as root{4}'.format(BOLD, red, ITALIC, BLINK, END))

class setup():
    os.system('clear')
    print(f'{BOLD}{ITALIC}{UNDERLINE}SETUP STARTED!!! WAIT{END}'.center(100))
    print(f'{BOLD}{pink}[1] UPDATING...{END}')
    os.system('sudo apt-get update> /dev/null')
    time.sleep(1)
    print(f'{BOLD}{pink}[2] UPGRADING PACKAGES...{END}')
    print(f'{BOLD}{green}Hey Upgrading sometimes it takes alot of time: Press Enter regurally to fast the upgrading process{END}')
    os.system('sudo apt-get upgrade -y > /dev/null')
    time.sleep(1)
    print(f'{BOLD}{pink}[3] INSTALLING PYTHON3{END}')
    os.system('sudo apt-get install python3 -y > /dev/null')
    time.sleep(1)
    print(f'{BOLD}{pink}[4] INSTALLING PIP3{END}')
    os.system('sudo apt-get install python3-pip -y > /dev/nul')
    time.sleep(1)
    print(f'{BOLD}{pink}[5] INSTALLING netifaces{END}')
    os.system('sudo pip3 install netifaces > /dev/null')
    time.sleep(1)
    os.system('clear')
    print(f'{BOLD}{green}{ITALIC}DONE!!!!!!!{END}')

