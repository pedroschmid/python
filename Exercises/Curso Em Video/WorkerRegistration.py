from datetime import datetime

worker = dict()

worker['name'] = str(input('Type your name: ')).strip()
worker['sex'] = str(input('Type your sex [M/F]: ')).strip().upper()
born = int(input('Type the year you were born: '))
worker['age'] = datetime.now().year - born
worker['workCard'] = int(input('Type your workcard (Type 0 if you dont have): '))

if worker['workCard'] != 0:
    worker['hiringYear'] = int(input('Type the year you were hired: '))
    worker['salary'] = float(input('Type your salary: '))

if worker['sex'] == 'M':
    worker['retireAge'] = 65 - worker['age']
else:
     worker['retireAge'] = 62 - worker['age']

print('-=' * 30)    

for k, v in worker.items():
    print(f'{k.upper()}: {v}')

print('-=' * 30)    