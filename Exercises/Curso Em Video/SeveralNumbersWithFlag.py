summ = 0
count = 0

while True:
    number = int(input('Type a number: (999 to break) '))

    if number == 999:
        break

    summ += number
    count += 1

print(f'{count} numbers were typed, the summ is {summ}')