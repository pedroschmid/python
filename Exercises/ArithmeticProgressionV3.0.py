fisrtTerm = int(input('Type the first term of the PA: '))
ratio = int(input('Type the ratio of the PA: '))

term = fisrtTerm
i = 1
total = 0
more = 10

while more != 0:
    total = total + more
    while i <= total:
        print(f'{term} -> ', end='')
        term += ratio
        i += 1
    print('BREAK!')
    more = int(input('How many terms do you want to show: '))    

print('Finish!')