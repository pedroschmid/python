number = int(input('Type the number you want to convert: '))

print('''\n
[0] CONVERT TO BINARY
[1] CONVERT TO OCTAL
[2] CONVERT TO HEXADECIMAL
''')

choose = int(input('Type your choose: '))

if choose == 0:
    print(f'{number} converted to binary is {bin(number)}')
elif choose == 1:
    print(f'{number} converted to octal is {oct(number)}')
elif choose == 2:
    print(f'{number} converted to hexadecimal is {hex(number)}')
else:
    print(f'{choose} is a invalid option!')
