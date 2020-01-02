from random import randint
from time import sleep

numbers = list()

def raffle():
    for i in range(0, 5):
        numbers.append(randint(0,100))

    print('-=' * 20)
    print(f'Sorting {len(numbers)} values: ', end='')

    for i in numbers:
        print(f'{i}', end=' ', flush=True)
        sleep(0.5)

    print('END!')    
    
def summEven(arr):
    totalSumm = 0

    for i in arr:
        if i % 2 == 0:
            totalSumm += i

    print(f'The sum of all even numbers {arr} is {totalSumm}')
    print('-=' * 20)

raffle()
summEven(numbers)            