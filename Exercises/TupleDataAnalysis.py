tupla = (
    int(input('Type a number:')),
    int(input('Type another number:')),
    int(input('Type another number:')),
    int(input('Type another number:'))
)

print(f'\nTuple: {tupla}')
print(f'\nHow many times did the value 9 appear: {tupla.count(9)}')

if 3 in tupla:
    print(f'\nIn which position was entered the first value 3: [{tupla.index(3)+1}]')
else:
    print('\nNo value "3" entered in tuple')    

print('\nWhat were the even numbers: ', end='')
for i in tupla:
    if i % 2 == 0:
        print(i, end='')