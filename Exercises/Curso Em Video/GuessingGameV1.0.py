import random

number = int(input('Type a number (Between 1 and 10): '))
randomNumber = random.randrange(1, 10)

if number == randomNumber:
    print('You hit the number!')
else:
    print(f'You missed the number!, the correctly answer was {randomNumber}')