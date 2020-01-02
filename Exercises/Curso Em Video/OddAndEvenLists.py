numbers = [[], []]

for i in range(0, 7):
    value = int(input('Type a number: '))

    if value % 2 == 0:
        numbers[0].append(value)
    else:
        numbers[1].append(value)    

print('-='*30)
print(f'Datalist: {numbers}')
print(f'Even values: {numbers[0]}')
print(f'Odd values: {numbers[1]}')
print('-='*30)