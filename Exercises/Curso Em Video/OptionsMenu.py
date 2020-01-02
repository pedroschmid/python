numberOne = float(input('Type the first number: '))
numberTwo = float(input('Type the second number: '))
total = 0

print('') # ' '

print('='*10)
print('[1] SUMM')
print('[2] SUBTRACTION')
print('[3] MULTIPLY')
print('[4] DIVIDE')
print('[5] HIGHER')
print('[6] LOWER')
print('[7] NEW NUMBERS')
print('[8] EXIT THE PROGRAM')
print('='*10)

choose = int(input('Type your choose (Between 1-8): '))

while choose != 8:
    if choose == 1:
        total = numberOne + numberTwo
        print(f'{numberOne} + {numberTwo} = {total}')

    elif choose == 2:
        total = numberOne - numberTwo 
        print(f'{numberOne} - {numberTwo} = {total}')

    elif choose == 3:
        total = numberOne * numberTwo  
        print(f'{numberOne} * {numberTwo} = {total}')

    elif choose == 4:
        total = numberOne / numberTwo 
        print(f'{numberOne} / {numberTwo} = {total}')

    elif choose == 5:
        if numberOne > numberTwo:
            total = numberOne
            print(f'The highest number is {total}')
        else:
            total = numberTwo
            print(f'The highest number is {total}') 

    elif choose == 6:
        if numberOne < numberTwo:
            total = numberOne
            print(f'The lowest number is {total}')
        else:
            total = numberTwo
            print(f'The lowest number is {total}')    

    elif choose == 7:
        numberOne = float(input('Type another first number: '))
        numberTwo = float(input('Type another second number: '))

    elif choose == 8:
        print('Exiting the program...')
        break  

    choose = int(input('Type your choose again (Between 1-8): '))