import socket


def indexMenu():
    print(f'\033[1;31m-=' * 35 + '\033[m')

    print(f"""\033[1;31m
      ___ ___    ___   _ _____ _  _ ___ ___ ___ _  _  ___ 
     |_ _| _ \  / __| /_\_   _| || | __| _ \_ _| \| |/ __|
      | ||  _/ | (_ |/ _ \| | | __ | _||   /| || .` | (_ |
     |___|_|    \___/_/ \_\_| |_||_|___|_|_\___|_|\_|\___| 
    \033[m""")

    print(f'\033[1;33m>Author: Sholomon\033[m')
    print(f'\033[1;33m>Version: 1.0\033[m')
    print(f'\033[1;33m>Apresentation: Welcome to IPGathering, follow the instructions below!\033[m')


def chooseMenu():
    print()
    print(f'\033[1;31m-=' * 35 + '\033[m')
    print()

    print(f'\033[1;33m[0]\033[m - Exit the program')
    print(f'\033[1;33m[1]\033[m - Gather IP (BY DOMAIN)')


indexMenu()

while True:
    chooseMenu()
    menuChoose = int(input(f'\033[1;33m==> \033[m'))

    if menuChoose == 0:
        print('\033[1;31mThanks for using the program, exiting ...\033[m')
        break
    elif menuChoose == 1:
        while True:
            try:
                url = str(input('\nType the url domain you want to know the IP\n\033[1;33m==> \033[m'))
            except KeyboardInterrupt:
                print(f'\n\033[1;31ERROR! THE USER DID NOT TYPE ANYTHING\033[m')
            else:
                print(f'\n\033[1;34mDOMAIN: {url}\033[m\n\033[1;34mIP: {socket.gethostbyname(url)}\033[m')
            finally:
                whileChoose = str(input('\nWant to search for another domain? [Y/N]\n\033[1;33m==> \033[m')).upper()[0]

            if whileChoose == 'N':
                break
            else:
                continue
