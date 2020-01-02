import random

studentA = str(input('Type the name of student A: '))
studentB = str(input('Type the name of student B: '))
studentC = str(input('Type the name of student C: '))
studentD = str(input('Type the name of student D: '))

result = random.choice([studentA, studentB, studentC, studentD])

print(f'the student drawn was {result}!')