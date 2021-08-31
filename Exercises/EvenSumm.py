total = 0

for number in range(0,6):
    number = int(input(f'Type the number {number+1}: '))
    if number % 2 == 0:
        total += number
print(f'The even summ is {total}')        