from random import randint

temp = list()
gameList = list()

totalGames = int(input('Type how many games will be generated: '))

for i in range(0, totalGames):
    count = 0

    while True:
        number = randint(1,60)

        if number not in temp:
            temp.append(number)
            count += 1
        if count >= 6:
            break

    temp.sort()
    gameList.append(temp[:])
    temp.clear()        

print('\n', '-=' * 3, f'RAFFLING {totalGames} GAMES' , '-=' * 3)

for i, l in enumerate(gameList):
    print(f'Game {i+1}: {l}')

print('-=' * 5, f'< GOOD LUCKY! >' , '-=' * 5)