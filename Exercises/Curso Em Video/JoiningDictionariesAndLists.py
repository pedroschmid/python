data = dict()
people = list()

totalAge = 0

while True:
    data.clear()
    data['name'] = str(input('Name: ')).strip().upper()[0]
    while True:
        data['sex'] = str(input('Sex [M/F]: ')).strip().upper()[0]
        if data['sex'] in 'MF':
            break
        print('ERROR! please, type only M or F!')
    data['age'] = int(input('Age: '))

    people.append(data.copy())
    totalAge += data['age']

    while True:
        answer = str(input('Want to add another people? [Y/N]: ')).strip().upper()[0]
        if answer in 'YN':
            break
        print('ERROR! please, type only S or N!')
    if answer == 'N':
        break

averageAge = totalAge / len(people)

print('-=' * 30)

print(f'Registed people: {len(people)}')
print(f'Average age: {averageAge}')

for p in people:
    if p['sex'] == 'F':
        print(f'Registered women were: {p["name"]} ', end=',')

print()

for p in people:
    if p['age'] > averageAge:
        print(f'People above average were: {p["name"]} ', end=',')
          
print('-=' * 30)    