list = []

countNumbers = 0
flag = ''

while True:
    number = int(input('Type a number: '))

    list.append(number)
    countNumbers += 1

    anwser = str(input('Want to add another number? [Y/N]: ')).strip().upper()

    if anwser == 'N':
        break

print('='*20)

list.sort(reverse=True)
if 5 in list:
    flag = 'True'

print(f'''
Typed numbers: {countNumbers} 
ReverseSort: {list} 
5 were typed? {flag}
''')

print('='*20)
