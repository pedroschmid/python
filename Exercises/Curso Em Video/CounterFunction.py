from time import sleep

def counter(start, end, addition):
    print('=-' * 20)
    print(f'Counting {addition} by {addition} of {start} untill {end}')

    if start < end:
        for i in range(start, (end+addition), addition):
            print(f'{i}', end=' ', flush=True)
            sleep(0.5)
    else:
        for i in range(start, (end-addition), -addition):
            print(f'{i}', end=' ', flush=True)
            sleep(0.5)

    print('END!')

counter(1, 10, 1)
counter(10, 0, 2)

print('=-' * 20)

print('Now its your time of personalize the counter!')
start = int(input('Type the counter start: '))
end = int(input('Type the counter end: '))
addition = int(input('Type the counter addition: '))

counter(start, end, addition)