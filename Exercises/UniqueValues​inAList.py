list = []

while True:
    number = int(input('Type a number: '))
    if number not in list:
        list.append(number)
    else:
        print('The list already contains the number, so it will not be added!')

    answer = str(input('Want to add another number? [Y/N]: ')).strip().upper()
    if answer == 'N':
        break
    elif answer != 'Y':
        print('Invalid anwser!')

list.sort()
print(f'The ordered list is: {list}')
