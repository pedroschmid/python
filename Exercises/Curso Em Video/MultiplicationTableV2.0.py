number = int(input('Type the number you want to know the multiplication table: '))

for i in range(1,11):
    print(f'{number}x{i} = {number * i}')