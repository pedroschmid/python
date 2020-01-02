list = [0]

for i in range(0,5):
    number = int(input('Type a number: '))
    if number == 0 or number > list[-1]:
        list.append(number)
    else:
        pos = 0
        while pos < len(list):
            if number <= list[pos]:
                list.insert(pos, number)
                break
            pos += 1

print('='*35)
print(f'{list}')
print('='*35)