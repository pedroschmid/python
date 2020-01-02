list = []
listOdd = []
listEven = []

while True:
    number = int(input('Type a number: '))
    list.append(number)

    anwser = str(input('Want to add another number? [Y/N]: ')).strip().upper()
    if anwser == 'N':
        break

for i in list:
    if i % 2 == 0:
        listEven.append(i)
    elif i % 2 != 0:
        listOdd.append(i)

print('='*20)
print(f'''List: {list}
Odd List: {listOdd}
Even List: {listEven}''')
print('='*20)