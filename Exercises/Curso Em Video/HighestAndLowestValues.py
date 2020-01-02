answer = 'Y'
summ = 0
count = 0
highest = 0
lowest = 10_000_000

while answer == 'Y':
    number = int(input('Type a number: '))

    summ += number
    count += 1

    if number > highest:
        highest = number

    if number < lowest:
        lowest = number

    answer = str(input('Want to type another number? [Y/N] ')).strip().upper()

average = summ / count

print(f'Average: {average} | Highest value: {highest} | Lowest value: {lowest}')
