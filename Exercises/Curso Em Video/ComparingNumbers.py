numberOne = int(input('Type the first number: '))
numberTwo = int(input('Type the second number: '))

if numberOne > numberTwo:
    print(f'{numberOne} is higher than {numberTwo}')
elif numberTwo > numberOne:
    print(f'{numberTwo} is higher than {numberOne}')
else:
    print(f'{numberOne} and {numberTwo} are the same number!')