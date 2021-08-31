from random import randint

number = int(input('Guess a number (Between 0-10): '))
computer = randint(0,10)
count = 1

while number != computer:
    number = int(input('You missed the number, try to guess again: '))
    count += 1

print(f'You needed {count} attempts to guess the number {computer}')    