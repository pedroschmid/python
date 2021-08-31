from random import randint
from time import sleep

game = {
    'player1': randint(1, 6),
    'player2': randint(1, 6),
    'player3': randint(1, 6),
    'player4': randint(1, 6)
}
    
for k, v in game.items():
    print(f'{k}: {v}')   
    sleep(2) 