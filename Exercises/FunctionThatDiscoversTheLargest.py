from time import sleep

def higher(* values):
    highest = 0
    lowest = 10_000_000
    count = 0

    print('=-' * 20) 

    for i in values:
        if i > highest:
            highest = i
        count += 1

    print('Analyzing passed values...')

    for i in values:
        print(f'{i}', end=' ', flush=True)
        sleep(0.5)

    print(f'Has been passed, {count} values at all.')
    print(f'The highest value is {highest}')          


higher(1, 2, 3, 4, 5, 6, 7, 8, 9, 50)
higher(50, 2, 91, 2000, 353, 1994)