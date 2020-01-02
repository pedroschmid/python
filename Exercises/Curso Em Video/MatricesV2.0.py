from random import randint

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

evenSumm = 0
ThirdColumSumm = 0
highestValue = 0

# for para gerar a matriz
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = randint(0,9)

# for para fazer as logicas
for i in range(0, 3):
    for j in range(0, 3):
        if matriz[i][j] % 2 == 0:
            evenSumm += matriz[i][j]
        if matriz[1][j] > highestValue:
            highestValue = matriz[1][j]  
            
for i in range(0, 3):
    ThirdColumSumm += matriz[i][2]

print('-=' * 30)

for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[i][j]}]', end='')
    print()  

print(f'\nThe summ of all even numbers: {evenSumm}')
print(f'The summ of all third columm values: {ThirdColumSumm}')
print(f'Highest value of the second line: {highestValue}')

print('-=' * 30)