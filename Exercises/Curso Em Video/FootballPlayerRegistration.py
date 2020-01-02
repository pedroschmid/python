player = dict()
match = list()

player['name'] = str(input('Player name: '))
totalMatch = int(input(f'Type how many matches {player["name"]} played: '))

for i in range(0, totalMatch):
    match.append(int(input(f'Type how many goals in match [{i + 1}]: ')))

player['goals'] = match[:]
player['total'] = sum(match)

print('-=' * 30) # style
print(f'Player: {player}') 

print('-=' * 30) # style
for k, v in player.items():
    print(f'The field {k} has value {v}')

print('-=' * 30) # style
for i, v in enumerate(player['goals']):
    print(f'In match {i+1}, did {v} goals!')
