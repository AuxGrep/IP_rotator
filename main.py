#!/usr/bin/env python3
# Author : AuxGrep
# 2023

import random # Tutaitumia kwa ajili ya kugenerate temp IP addresses 
import netifaces as mandonga_mtu_kazi # Tutaitumia kwa ajili kuwasiliana na kernel box , kuview ip-tables
import os # tutaitumia ku interact na command line linux commands
import sys # just nitaitumia kwenye condition statements 
import subprocess # tutaitumia kwenye kuhandle child na parent proc via Linux commands
import time # Tutaitumia kwa ajili ya sleeping time (pause)
import platform # Tutaitumia kwa ajili ya kudetect operating system
import socket # Tutaitumia kwa ajili ya kuview internal ip addr + hostnames

# colors
CYAN = "\033[0;36m"
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
else:
    pass

# checking os
supported_os = ['Linux', 'Ubuntu', 'Parrotsec']
if platform.system() in supported_os:
    pass
else:
    os.system('clear')
    sys.exit(f'{BOLD}{red}{ITALIC}Only Linux can run this program!! Exiting!!{END}')

try:
    # Lazima tujuwe internal IP address + hostname ya Linux Box
    computer_name = socket.gethostname() # hii itaview Linux Box hostname
    ip4nework_ip = socket.gethostbyname(computer_name) # hii itaview Linux internal IP

    os.system('clear')
    print(f'{BOLD}{green}Hello {computer_name} welcome!!{END}'.center(100))
    print('')
    print('Your internal IP is {1}{0}{2}'.format(ip4nework_ip, pink, END))
    chop_ip = str(input('Please Enter first 3 subnet ip (eg: 192.168.43.) based on your internal IP {1}{2}{0}{3}: '.format(ip4nework_ip, BOLD, pink, END))) # USER ataweka 3 subnet internal IP mfano: 192.168.43.
    print('')
    os.system('clear')
    print(f'{BOLD}{UNDERLINE}Generating random Virtual IP ! Wait!{END}'.center(100))
    time.sleep(3)
    for x in range(1, 10): # hapa tunataka idadi ya temp IP 10 tu, unaweza ongeza from 10 to UP
        time.sleep(0.2)
        ip2chop = "{}".format(chop_ip) # Tuna-assign new variable ila sio lazima unaweza endelea nayo ya mwanzo "cho_ip"
        ip2chop += ".".join(map(str, (random.randint(0, 255) for _ in range(1)))) # hapa tuna join ile entered 3 subnet na kugenerate random 4 subnet iwe ip kamili
        print('{1}{2}--> {0}{3}'.format(ip2chop, BOLD, blue, END)) # hapa tutaprint zile generated IP kwa user
    print()
    server_temporary_ip = str(input(f'{BOLD}PLease Enter any of above ip:{END} '))
except KeyboardInterrupt(): # hapa endapo utabonyeza CTRL + C 
    os.system('clear')
    sys.exit('User Cancelled!! Byeee!')

# settings
netmask = '255.255.255.0' # kwa ajili ya kuhandle assigned IP kwenye interface husika
virtual_IP = '{}'.format(server_temporary_ip) # hii ni temporaly IP soon Device ikiwa tyr imeefeed ip 
valid_lft = 10 #ukichange hii to 5 means system itapewa net IP kwa kila 5 seconds
preferred_lft = 10 # ALSO ukichange hii to 5 means system itapewa net IP kwa kila 5 seconds

# IP-LIST: Tutatengeneza List of IPs ambazo server itakuwa ina changes to those IPs kupunguza attacking surface
for x in range(1,50):
    ip_generate = chop_ip
    ip_generate += ".".join(map(str, (random.randint(0, 255) for _ in range(1))))
    os.system('clear')
    print(f'{BOLD}{CYAN}Generating Core Web Server IP -->{END}{BOLD} {ip_generate}{END}')
    while True:
        with open('ip.txt', mode='a') as file:
            file.write(f'\n{ip_generate}')
            time.sleep(1.2)
            break

os.system('clear')
print(f'{BOLD}{red}Making list table{END}'.center(100))
data = open('ip.txt').read().splitlines()
data2 = data[2:]
server_ip_list = data2

class network():
    try:
        os.system('clear')
        print(f'{BOLD}{ITALIC}{UNDERLINE}{pink}HEY!!! WELCOME{END}'.center(100))
        print('')
        menu_choice = ['[1] Start a Program', '[2] Installation Setup - (for new users)']
        for menu in menu_choice:
            time.sleep(0.2)
            print(menu)
        print('')
        menu_user = int(input(f'{BOLD}{CYAN}PLease ENter a menu choice(1 or 2){END}: '))
        #menu_user = int(sys.argv[1])
        if menu_user >= 3 or menu_user not in [1,2]: # Lazima tutumie high and powerful techniques to check user inputs
            sys.exit(f'{BOLD}{red}{ITALIC}Invalid choice: choose 1 or 2{END}')    
        if menu_user == int(1):
            interfaces = mandonga_mtu_kazi.interfaces()
            for i in interfaces: # Hiii itackeck on all available interfaceS.
                if i != "lo": # Hii itatoa lo interface kwenye our checks.
                    try:
                        mandonga_mtu_kazi.ifaddresses(i)
                        gws = mandonga_mtu_kazi.gateways()
                        gateway = gws['default'][mandonga_mtu_kazi.AF_INET][0]
                        ip = mandonga_mtu_kazi.ifaddresses(i)[mandonga_mtu_kazi.AF_INET][0]['addr']
                        sm = mandonga_mtu_kazi.ifaddresses(i)[mandonga_mtu_kazi.AF_INET][0]['netmask']
                        os.system('clear')
                        print (f"{purple}{BOLD}{UNDERLINE}Network information for{END}: {BOLD}{green}{ITALIC}{i}{END}"\
                            .center(100))
                        print('')
                        print (f"{BOLD}{ITALIC}IP address: {ip}{END}")
                        print (f"{BOLD}{ITALIC}Subnet Mask: {sm}{END}")
                        print (f"{BOLD}{ITALIC}Gateway: {gateway}{END}")
                        print ()
                    except:
                        pass # hatutaki error handle yoyote so we pass like shadow hehehe !!!
            print('')

            # STEP 1: Tunachukua SERVER ip kutoka kwa user 
            user_input = str(input(f'{BOLD}{pink}Enter server IP:{END} '))
            connected_interface = str(input(f'{BOLD}{pink}Enter interface name:{END} '))

            # lazima tu validate kwamba ip iliyowekwa na user ipo kwenye kernel box yetu
            if user_input in ip:
                os.system('clear')
                print(f'{BOLD}{ITALIC}{green}{UNDERLINE}PROGRAM STARTED!{END}'.center(100))
                print('')
                print('{1}{2}validate the interface {0}{3}'.format(connected_interface, BOLD, ITALIC, END))
                # Sio tu IP bali tunahitaji ku validate interface, Je ni kweli ipo kwenye box yetu
                if connected_interface in i: 
                    print('system: Modfying IP {0}'.format(user_input))
                    time.sleep(2)
                    change_ip = subprocess.run(['ifconfig', connected_interface, virtual_IP, \
                        'netmask', netmask], stderr=subprocess.DEVNULL,\
                        stdout=subprocess.DEVNULL)
                else:
                    # endapo interface haipo kwenye kernal interface 
                    print('{1}{3}{0} is not found in ur kernel! Try Again{2}'.format(connected_interface, red, END, BOLD))
                    time.sleep(2)
                    sys.exit()
                os.system('clear')
                time.sleep(2)
                # STEP 2 ni kustart our main part ya program yetu
                print(f'{BOLD}{pink}{ITALIC}STARTING ROTATING IPS{END}'.center(100))
                print('')
                try:
                    while True:
                        for hacker in server_ip_list:
                            time.sleep(10)
                            os.system('sudo ip addr change {0}/24 dev {1} valid_lft {2} preferred_lft {3}'.format(hacker,\
                                connected_interface, valid_lft, preferred_lft))
                            print('{1}{2}Web Server: IP changed to{4}{2} --> {0}{4}'.format(hacker, green, BOLD, \
                                pink, END))
                except KeyboardInterrupt: # when user press CTRL + C
                    os.system('clear')
                    print(f'{BOLD}{red}{ITALIC}User cancelled!! Exiting! Byee!{END}')
                    time.sleep(2)
                    # restore normal connectivity 
                    subprocess.run('sudo service NetworkManager restart', shell=True)
                    os.system('sudo rm ip.txt')
                    sys.exit()      
            else: 
                print('{1}{2}Hey bro!! You Entered a wrong ip {0} addr!! Exiting!!{3}'.format(user_input, BOLD, red, END))
                sys.exit()
        elif menu_user == int(2):
            from inst.ints import setup
            setup()
    except KeyboardInterrupt:
        os.system('clear')
        print(f'{BOLD}{purple}{ITALIC}Thanks so much!! Take care ! bYEE!{END}'.center(100))
        os.system('sudo rm ip.txt')
        time.sleep(2)
        sys.exit()
