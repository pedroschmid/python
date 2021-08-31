from random import randint

countWin = 0

while True:
    number = int(input('Type a number (Between 1-10): '))
    choose = str(input('Odd or Even? [O/E]: ')).strip().upper()
    computer = randint(1,10)

    summ = number + computer

    if choose[0] == 'E' and (computer % 2) == 0:
        print(f'Player: {number} | Computer: {computer} | Player won!')
        countWin += 1
    elif choose[0] == 'O' and (computer % 2) != 0:
        print(f'Player: {number} | Computer: {computer} | Player won!')
        countWin += 1
    else:
        print(f'Player: {number} | Computer: {computer} | Computer won!')
        break

print(f'GAME OVER! you won {countWin} times!')    