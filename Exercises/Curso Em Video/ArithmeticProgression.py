fisrtTerm = int(input('Type the first term of the PA: '))
ratio = int(input('Type the ratio of the PA: '))

tenthTerm = fisrtTerm + (10 - 1) * ratio

for i in range(fisrtTerm, tenthTerm, ratio):
    print(f'{i}', end = ' => ')
print('Finish!')    