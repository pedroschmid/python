fisrtTerm = int(input('Type the first term of the PA: '))
ratio = int(input('Type the ratio of the PA: '))

term = fisrtTerm
i = 1

while i <= 10:
    print(f'{term} -> ', end='')
    term += ratio
    i += 1

print('Finish!')