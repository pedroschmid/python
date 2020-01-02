player = dict()
goals = list()
team = list()

while True:
    player.clear()

    player['name'] = str(input('Player name: ')).strip()
    match = int(input(f'How many match {player["name"]} played? '))
    goals.clear()

    for i in range(0, match):
        goals.append(int(input(f'How many goals {player["name"]} did in match {i+1}? ')))

    player['goals'] = goals[:]
    player['total'] = sum(goals)
    team.append(player.copy())

    anwser = str(input('Want to add another player? [Y/N] ')).strip().upper()[0]
    if anwser == 'N':
        break

print('-=' * 30)

print('KEY ', end='')
for i in player.keys():
    print(f'{i.upper():<15}', end='')
print()

print('-=' * 30)    

for k, v in enumerate(team):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()    
    
print('-=' * 30)

while True:
    choose = int(input('Show data from which player? [Type 999 to stop the programm] '))

    if choose == 999:
        break

    if choose >= len(team):
        print('Player dont exist!')
    else:
        print(f'Data of player [{choose}]!')
        for i, g in enumerate(team[choose]['goals']):
            print(f'In game {i+1} did {g} goals!') 

    print('-=' * 30)
print('End!')