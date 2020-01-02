def readMoney(msg):
    status = False

    while not status:
        entry = str(input(msg)).replace(',', '.')

        if entry.isalpha() or entry.strip() == '':
            print(f'\033[0;31mERROR! \"{entry}\" is a unvalid price!\033[0;31m')
        else:
            status = True
            return float(entry)    