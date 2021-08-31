def readInt(entry):
    status = False
    value = 0

    while True:
        number = str(input(entry))

        if number.isnumeric():
            value = int(number)
            status = True
        else:
            print('\033[0;31mERROR! Type a valid int number!\033[m')    

        if status == True:
            break

    return value    

print('-=' * 30)

n = readInt('Type a number: ')
print(f'You just entered the number {n}')

print('-=' * 30)