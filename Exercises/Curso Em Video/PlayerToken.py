def token(name = '', goals = 0):
    print('=-' * 30)
    if name == '':
        return f'The player <Unknow> did {goals} goals in the championship.'
    else:
        return f'The player {name} did {goals} goals in the championship.'

print('=-' * 30)

playerName = str(input('Type the player name: '))
playerGoals = int(input(f'How many goals {playerName} did in the championship? '))

print(f'{token(playerName, playerGoals)}')

print('=-' * 30)