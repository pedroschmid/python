from random import randint

print('=' * 15)
print('[0] TO JO (PEDRA)')
print('[1] TO KEN (PAPEL)')
print('[2] TO PO (TESOURA)')
print('=' * 15)

while True:
    player = int(input('Type your choice (based on the in past instructions): '))
    computer = randint(0,2)

    if player == 0 and computer == 1:
        print(f'Player: {player} | Computer: {computer} | Computer won!')
    elif player == 0 and computer == 2:
        print(f'Player: {player} | Computer: {computer} | Player won!') 
    elif player == 0 and computer == 0:
        print(f'Player: {player} | Computer: {computer} | Draw!')
    elif player == 1 and computer == 0:
        print(f'Player: {player} | Computer: {computer} | Player won!!')        
    elif player == 1 and computer == 2:
        print(f'Player: {player} | Computer: {computer} | Computer won!')
    elif player == 1 and computer == 1:
        print(f'Player: {player} | Computer: {computer} | Draw!')
    elif player == 2 and computer == 0:
        print(f'Player: {player} | Computer: {computer} | Computer won!')
    elif player == 2 and computer == 1:
        print(f'Player: {player} | Computer: {computer} | Player won!')
    elif player == 2 and computer == 2:
        print(f'Player: {player} | Computer: {computer} | Draw!')