import random

studentA = str(input('Type the name of student A: '))
studentB = str(input('Type the name of student B: '))
studentC = str(input('Type the name of student C: '))
studentD = str(input('Type the name of student D: '))

list = [studentA, studentB, studentC, studentD]

random.shuffle(list)

print(f'The order of presentation will be:\n {list}')