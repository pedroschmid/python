def readInt(msg):
    while True:
        try:
            number = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERROR! Please type a valid integer number.\033[m')  
            continue
        except KeyboardInterrupt:
            print('\n\033[0;31mThe user prefered not type a value.\033[m')
            return 0
        else:
            return number  

def readFloat(msg):
    while True:
        try:
            number = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERROR! Please type a valid float number.\033[m')
        except KeyboardInterrupt:
            print('\n\033[0;31mThe user prefered not type a value.\033[m')
            return 0
        else:
            return number  
print('=-' * 30)

numberOne = readInt('Type a integer value: ')
numberTwo = readFloat('Type a float value: ')

print(f'Int = {numberOne} | Float = {numberTwo}')

print('=-' * 30)