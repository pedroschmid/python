list = []
expression = str(input('Type a mathematical expression: '))

for parentheses in expression:
    if parentheses == '(':
        list.append('(')
    elif parentheses == ')':
        if len(list) > 0:
            list.pop()
        else:
            list.append(')')
            break

if len(list) == 0:
    print('This is a valid expression!')
else:
    print('This is not a valid expression!')
