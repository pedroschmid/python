countHigherAge = 0
countMale = 0
countLowerAgeFemale = 0

while True:
    age = int(input('Type your age: '))
    sex = str(input('Type your sex [M/F]: ')).strip().upper()

    if age > 18:
        countHigherAge += 1

    if sex == 'M':
        countMale += 1

    if sex == 'F' and age < 20:
        countLowerAgeFemale += 1

    anwser = str(input('Want to add another people? [Y/N]: ')).strip().upper()

    if anwser == 'N':   
        break

print(f'Age over 18: {countHigherAge} | Registered men: {countMale} | Women under 20 years: {countLowerAgeFemale}')