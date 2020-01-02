people = list()
data = list()

highestAge = 0
lowestWeight = 10_000_000

while True:
    data.append(str(input('Name:')))
    data.append(float(input('Weight: ')))

    if data[1] > highestAge:
        highestAge = data[1]
    if data[1] < lowestWeight:
        lowestWeight = data[1]    

    people.append(data[:])
    data.clear()

    answer = str(input('Want to add another people? [Y/N] ')).strip().upper()
    if answer == 'N':
        break

print('-='*30)
print(f'Datalist: {people}')
print(f'Total registered people: {len(people)}')
print(f'Highest weight: {highestAge}')
print(f'Highest weight: {lowestWeight}')
print('-='*30)