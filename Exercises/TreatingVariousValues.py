number = int(input('Type a number: '))
count = 0
summ = 0

while number != 999:
    summ += number
    count += 1
    number = int(input('Type another number: '))

print(f'{count} numbers were typed and the sum of the numbers is {summ}')    